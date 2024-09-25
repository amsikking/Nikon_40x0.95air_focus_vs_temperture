# Imports from the python standard library:
import time
from datetime import datetime

# Third party imports, installable via pip:
import numpy as np
from tifffile import imread, imwrite

# Our code, one .py file per module, copy files to your local directory:
import pi_E_753_1CD         # github.com/amsikking/pi_E_753_1CD
import thorlabs_CS165MU1    # github.com/amsikking/thorlabs_CS165MU1
import thorlabs_TC200       # github.com/amsikking/thorlabs_TC200

# Init devices:
focus_piezo = pi_E_753_1CD.Controller(which_port='COM6', verbose=True)
camera = thorlabs_CS165MU1.Camera(verbose=True)
temp_controller = thorlabs_TC200.Controller(
    'COM13', sensor='NTC10K', verbose=True)

# Settings:
ch = 0
camera.apply_settings(
    ch, num_images=1, exposure_us=int(100e3), height_px='max', width_px='max')
z_steps_um = np.arange(0, 100, 0.25)
t_steps_C = np.arange(22, 42, 1)
settle_time_s = 30*60 # 30min
# temp_controller manually set to 'TUNE' with PID set to: 250, 10, 5

# Acquire:
temp_controller.set_enable(True)
for t in t_steps_C:
    # set temp:
    temp_controller.set_tset(int(t))
    # wait for thermal equilibrium:
    time.sleep(settle_time_s)
    # record temp before z stack:
    t1_C = temp_controller.get_tactual()
    # take z stack:
    z_stack = np.zeros(
        (len(z_steps_um), camera.height_px[ch], camera.width_px[ch]), 'uint16')
    for i, z in enumerate(z_steps_um):
        focus_piezo.move_um(z, relative=False)
        z_stack[i,:] = camera.record_to_memory(ch)
    # record temp after z stack:
    t2_C = temp_controller.get_tactual()
    # save data:
    dt = datetime.strftime(datetime.now(),'%Y-%m-%d_%H-%M-%S')
    filename = 'data\\z_stack_%iC.tif'%t
    with open('data\\metadata.txt', 'a') as file:
        file.write(
            dt + ',' + filename + ',' + str(t1_C) + ',' + str(t2_C) + '\n')
    imwrite(filename, z_stack, imagej=True)
temp_controller.set_enable(False)

# Close devises:
camera.close()
focus_piezo.close()
temp_controller.close()

# Third party imports, installable via pip:
import numpy as np
from tifffile import imread, imwrite

# Copy steps from 'acquisition.py':
t_steps_C = np.arange(22, 42, 1)

# Crop data to reduce storage and compute time:
for t in t_steps_C:
    # Get data:
    z_stack = imread('data\\z_stack_%iC.tif'%t)
    # Crop:
    y_px, x_px = 490, 670
    z_stack = z_stack[:,
                      y_px:z_stack.shape[1] - y_px,
                      x_px:z_stack.shape[2] - x_px]
    # Save:
    filename = 'data_cropped\\z_stack_%iC.tif'%t
    print('saving: %s (shape=%s)'%(filename, z_stack.shape))
    imwrite('data_cropped\\z_stack_%iC.tif'%t, z_stack, imagej=True)

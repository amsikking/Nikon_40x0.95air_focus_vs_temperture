# Nikon_40x0.95air_focus_vs_temperture
Data showing how the focal plane of a Nikon 40x0.95 air objective moves axially with temperature.

## Result:
The focal plane of a Nikon 40x0.95 air objective (MRD00405) moves axially with temperature at a linear rate of **~1.58um/degC**. The parfocal length (flange to image plane) is ~60.06mm, which gives a coefficient of linear thermal expansion (CLTE) of
**~26.4e-6/K**. For reference, typical values of CLTE are ~10-17 for stainless steel, ~18-19 for brass and 21-24 for aluminium (e-6/K).

![social_preview](https://github.com/amsikking/Nikon_40x0.95air_focus_vs_temperture/blob/main/social_preview.png)

## Test setup:
See the numbered photos in the [photos](https://github.com/amsikking/Nikon_40x0.95air_focus_vs_temperture/tree/main/photos) folder or click on the links below:

0) [**Overview:**](https://github.com/amsikking/Nikon_40x0.95air_focus_vs_temperture/blob/main/photos/0_overview.jpg)
    - A minimal microscope was built on a full size optical table (305mm thick, Newport M-RS4000-46-12).
    - The microscope consisted of an objective (Nikon MRD00405), a tube lens (Thorlabs TTL200-A) and a camera (Thorlabs CS165MU1).
    - The optics were carefully aligned onto the same optical axis using an alignment laser, and the camera focus was set using a collimated beam into the tube lens (see 'alignment_laser.tif' for focus). The axial separation of the objective and tube lens was set with a ruler to ~170mm (within spec).
    - The objective is coverslip corrected, so a small ~170um optical window was bonded to the front, and the correction collar was adjusted to 170um. This is an unusual thing to do to but is required for another setup, see [here](https://andrewgyork.github.io/high_na_single_objective_lightsheet/appendix.html#Parts_em_optical) for details on the optical window.
    - The objective was mounted firmly: firstly into a thread adaptor (Thorlabs SM2A33), then into a short 2in lens tube (Thorlabs SM2L05) housed in a 2in flexure mount (Thorlabs SM2RC/M). The flexure mount was attached to a thermally isolating 25mm diameter fiberglass post (Thorlabs RS50G/M) and secured onto the optical table with a non bridging flexure clamp (Thorlabs POLARIS-CA25/M).
    - Using the same mounting method, but with a steel post (Thorlabs RS50/M) instead of fiberglass, a 100um range piezo (PI P-726.1CD) was used to hold a flat sample in the focal plane of the objective.
1) [**Objective heater and insulation:**](https://github.com/amsikking/Nikon_40x0.95air_focus_vs_temperture/blob/main/photos/1_objective_heater_and_insulation.jpg) Heat tape with a built in thermister (Thorlabs TLK-H) was taped onto the body of the objective and driven with a PID controller (Thorlabs TC200).
2) [**Insulated setup:**](https://github.com/amsikking/Nikon_40x0.95air_focus_vs_temperture/blob/main/photos/2_insulated_setup.jpg) An insulated jacket fashioned out of thick foam (Uline S-13715) was secured to the objective with lab tape. This helped reduce heat transfer to the air, which reduced equilibration time and thermal gradients.
3) [**Objective mirror piezo:**](https://github.com/amsikking/Nikon_40x0.95air_focus_vs_temperture/blob/main/photos/3_objective_mirror_piezo.jpg) A silver mirror was mounted into a 1in lens tube and screwed into the 100um piezo. The axial position of the mirror was adjusted to be roughly in focus with the piezo set to 80um. This ensured that as the objective was heated (and expanded) that the piezo could retract towards 0um to find the new position of the focal plane.
4) [**Scratched mirror with light:**](https://github.com/amsikking/Nikon_40x0.95air_focus_vs_temperture/blob/main/photos/4_scratched_mirror_with_light.jpg) To accurately find focus, a flat, bright and thin sample with sharp features is preferable. To achieve this a silver mirror (Thorlabs PF10-03-P01) was gently scratched by rubbing the end of a ball driver over the surface in a rotary fashion. Tape was then used to remove the silver fragments to leave a partial silver/glass interface. A white light source (Thorlabs OSL2) was used to illuminate the frosted back side of the mirror, creating a scattered and uniform illumination profile behind the silver coating.

## Acquisition:
The data was collected programmatically (see '**acquisition.py**') in the following way:
- The temperature was set from 22C (just above room temp) to 42C in steps of 1C.
- A 30min settle time was given after each temperature set point to allow for thermal equilibration. This was proven adequate since an experimental run with a 3min settle time gave almost the same results.
- After waiting the settle time, a z stack of 400 images were acquired over the 100um piezo range with an axial separation of 0.25um (about 2x Nyquist sampling based on a depth of field of ~1um).
- The temperature from the thermistor was recorded before and after each z stack.

## Data:
Both the full 'data' and 'data_cropped' were analyzed. Both gave the same results, but only the cropped data was included in the repository to save on storage and computation time. Cropping was performed according to 'data_cropped.py'.

## Analysis:
The data was analyzed programmatically (see '**analysis.py**') in the following way:
- At each temperature set point, the sum of the gradient magnitude of each image in the z stack was calculated. The image with the highest gradient magnitude sum (i.e. the 'sharpest features') was then selected as the focal plane.
- The temperature used for analysis was the average of the measured before and after z stack temperatures (which measured the same in all cases). The measured range was 21.8-39.5C (see data\metadata.txt).
- The focal plane position (um) was then plotted against the measured temperatures (C) giving a linear trend.
- The linear trend was then fitted with a straight line to give an accurate estimate of the axial shift of the focal plane with temperature and the associated coefficient of linear thermal expansion (CLTE).
- See the included figure '**Nikon_40x0.95air_focus_vs_temperature_data.png**' for the end result.

To reproduce the analysis of the cropped data download the repository and run 'analysis.py'.

## Acknowledgments:
Inspired by, and with contributions from: [jlazzaridean](https://github.com/jlazzaridean) and [AndrewGYork](https://github.com/AndrewGYork).

# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Modules
from FITTING import Fit_Gaussian

# Extract the exposure and the intensities
exposures, intensities = [], []
for i in range(1,31):
    # Define the path
    path = f'Data/20220415_Exposure_curve/vesicle_{i}/vesicle_{i}_MMStack_Default'
    
    # Read the exposure time
    exposure = float(open(f'{path}_metadata.txt').readlines()[56][-7:-2])
    
    # Read the image average without the base line
    img = plt.imread(f'{path}.ome.tif').mean(axis=0)-300
    
    # Fit a Gaussian on the intensity
    intensity, _ = Fit_Gaussian(img.ravel(), normalized=True).hist_fitting(show=False)
    
    # Append the exposure time and the intensity
    exposures.append(exposure)
    intensities.append(intensity)

# Transform them into numpy arrays
exposures = np.array(exposures)
intensities = np.array(intensities)

# Fit a line on the point
m, b = np.polyfit(exposures, intensities, 1)   # m:slope, b:intercept

    
# Show the Results
plt.figure(figsize=(10,10))

plt.scatter(exposures, intensities, label = 'Intensity', alpha=0.5)

plt.plot(exposures, m*exposures + b, label = f'Fitting = ({m:.2f}) X + ({b:.2f})', color='red', alpha=0.5)

plt.title('Intensity vs Exposure', fontsize='x-large')
plt.xlabel('Exposure [ms]', fontsize='x-large')
plt.ylabel('Intensity', fontsize='x-large')
plt.legend(fontsize='x-large')
plt.grid()
plt.savefig('Intensity_vs_Exposure')

# Show the results
plt.show()
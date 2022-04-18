# Libraries
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
    
# Show the Results
plt.figure(figsize=(10,10))

plt.scatter(exposures, intensities, label = 'intensity')
plt.title('Intensity vs Exposure', fontsize='x-large')
plt.xlabel('Exposure [ms]', fontsize='x-large')
plt.ylabel('Intensity', fontsize='x-large')
plt.legend(fontsize='x-large')
plt.grid()
plt.savefig('Intensity_vs_Exposure')

# Show the results
plt.show()
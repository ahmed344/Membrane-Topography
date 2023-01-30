#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import median_abs_deviation

# Enter the heights
h1 = np.array([52.53, 57.34, 52.35, 54.52, 53.43, 49.11, 47.96, 52.94])
h2 = np.array([41.52, 45, 47.94, 58.47, 54.22, 54.23])
h3 = np.array([56.63, 57.38, 55.97, 56.56, 58.3, 53.12, 56.93, 55.21, 57.36, 55.94, 56.14])
ha = np.hstack((h1,h2,h3))


plt.figure(figsize=(16.54,20))

# Define the boxes
bp = plt.boxplot([h1,h2,h3, ha],
                labels = [f'Experiment 1\n  $<h>=$ {h1.mean():.2f}\n $\sigma(h)$  = {h1.std():.2f} \n $med(h)=$ {np.median(h1):.2f}\n$MAD(h)=$ {median_abs_deviation(h1):.2f}',
                          f'Experiment 2\n  $<h>=$ {h2.mean():.2f}\n $\sigma(h)$  = {h2.std():.2f} \n $med(h)=$ {np.median(h2):.2f}\n$MAD(h)=$ {median_abs_deviation(h2):.2f}',
                          f'Experiment 3\n  $<h>=$ {h3.mean():.2f}\n $\sigma(h)$  = {h3.std():.2f} \n $med(h)=$ {np.median(h3):.2f}\n$MAD(h)=$ {median_abs_deviation(h3):.2f}',
                          f'Pool\n  $<h>=$ {ha.mean():.2f}\n $\sigma(h)$  = {ha.std():.2f} \n $med(h)=$ {np.median(ha):.2f}\n$MAD(h)=$ {median_abs_deviation(ha):.2f}'],
                patch_artist=True);

# Customize the boxes
bp['boxes'][0].set(color='purple', hatch='/', linewidth=4, alpha=0.4)
bp['boxes'][1].set(color='green' , hatch='/', linewidth=4, alpha=0.4)
bp['boxes'][2].set(color='brown' , hatch='/', linewidth=4, alpha=0.4)
bp['boxes'][3].set(color='gray'  , hatch='/', linewidth=4, alpha=0.4)

# Customize the Median line
bp['medians'][0].set(color='purple', linewidth=4, alpha=0.6)
bp['medians'][1].set(color='green' , linewidth=4, alpha=0.6)
bp['medians'][2].set(color='brown' , linewidth=4, alpha=0.6)
bp['medians'][3].set(color='gray'  , linewidth=4, alpha=0.6)


# Plot the scattered points
plt.scatter(x = [1] * len(h1), y = h1, color='purple', s=100, alpha=0.6, label='Experiment 1' )
plt.scatter(x = [2] * len(h2), y = h2, color='green' , s=100, alpha=0.6, label='Experiment 2')
plt.scatter(x = [3] * len(h3), y = h3, color='brown' , s=100, alpha=0.6, label='Experiment 3')
plt.scatter(x = [4] * len(ha), y = ha, color='gray'  , s=100, alpha=0.6, label='Pool')

plt.xticks(fontsize='xx-large')
plt.yticks(fontsize='xx-large')
plt.ylabel("Height $_{[nm]}$", fontsize=23)
# plt.title(f'GUV Height $\mu = ${np.mean(ha):.2f}, $\sigma = $ {np.std(ha):.2f}', fontsize=23)
plt.legend(fontsize='xx-large')
plt.grid(alpha=0.5)
plt.tight_layout()
plt.savefig('GUV_Height_Boxplot')
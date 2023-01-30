#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# Enter the heights
h1 = [52.53, 57.34, 52.35, 54.52, 53.43, 49.11, 47.96, 52.94]
h2 = [41.52, 45, 47.94, 58.47, 54.22, 54.23]
h3 = [56.63, 57.38, 55.97, 56.56, 58.3, 53.12, 56.93, 55.21, 57.36, 55.94, 56.14]

# Plots the histograms
plt.figure(figsize=(20,6))

plt.hist(h1, bins=20, range=[40.05, 60.05], width=0.28, label=f'20201023 $\mu = ${np.mean(h1):.2f}, $\sigma = $ {np.std(h1):.2f}', alpha=0.6, color='b')
plt.hist(h2, bins=20, range=[40.35, 60.35], width=0.28, label=f'20201216 $\mu = ${np.mean(h2):.2f}, $\sigma = $ {np.std(h2):.2f}', alpha=0.6, color='g')
plt.hist(h3, bins=20, range=[40.65, 60.65], width=0.28, label=f'20210112 $\mu = ${np.mean(h3):.2f}, $\sigma = $ {np.std(h3):.2f}', alpha=0.6, color='r')

plt.xlim(44,60)
plt.xticks(np.arange(40,60,1), fontsize='xx-large')
plt.yticks(fontsize='xx-large')
plt.xlabel("Height $_{[nm]}$", fontsize='xx-large')
plt.ylabel('Number of GUVs', fontsize='xx-large')
plt.title(f'GUV Height Histogram $\mu = ${np.mean(h1+h2+h3):.2f}, $\sigma = $ {np.std(h1+h2+h3):.2f}', fontsize='xx-large')
plt.legend(fontsize='xx-large')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('GUV_Height_Histogram')

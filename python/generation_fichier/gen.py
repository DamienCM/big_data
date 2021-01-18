import numpy as np
import time 
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

t0=time.time()

path='./data.csv'

taille_de_fichier = 10_000

O3=np.random.uniform(low=0,high=1,size=taille_de_fichier)
NO2=np.random.normal(loc=.5, scale=1,size=taille_de_fichier) 

SO2=np.random.gamma(0.5,scale=1,size=taille_de_fichier) #Parameters shape  : float or array_like of floats ; The shape of the gamma distribution. Must be non-negative.
CO=np.random.exponential(scale=1,size=taille_de_fichier)


#Visualisation des distributions

"""fig,axes=plt.subplots(4,1)
fig.set_size_inches(16,9)
data=[O3,NO2,SO2,CO]
labels=['O3','NO2','SO2','CO']

for i in range(len(labels)):
    axes[i].hist(data[i],bins=200,label=labels[i])
    axes[i].legend()
fig.savefig('distribution.png',dpi=800)"""

np.savetxt(path,np.transpose([O3,NO2,SO2,CO]),delimiter=',',header=f'File generated on : {datetime.now()} by damien-mouad \n O3,NO2,SO2,CO')

print(f'Program executed in {time.time()-t0} seconds')
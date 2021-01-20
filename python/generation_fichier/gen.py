import numpy as np
import time 
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import os 


t0=time.time()

path='./data.csv'

nombre_de_kilo_ligne = 5000

taille_batch = 1_000

file = open(path, 'wb')

for i in  range(nombre_de_kilo_ligne):
    if i%100==0:
        print(f"Progression : {100*float(i/nombre_de_kilo_ligne)} %" )
    O3=np.random.uniform(low=0,high=1,size=taille_batch)
    NO2=np.random.normal(loc=.5, scale=1,size=taille_batch) 

    SO2=np.random.gamma(0.5,scale=1,size=taille_batch) #Parameters shape  : float or array_like of floats ; The shape of the gamma distribution. Must be non-negative.
    CO=np.random.exponential(scale=1,size=taille_batch)


    #Visualisation des distributions

    """fig,axes=plt.subplots(4,1)
    fig.set_size_inches(16,9)
    data=[O3,NO2,SO2,CO]
    labels=['O3','NO2','SO2','CO']

    for i in range(len(labels)):
        axes[i].hist(data[i],bins=200,label=labels[i])
        axes[i].legend()
    fig.savefig('distribution.png',dpi=800)"""

    np.savetxt(file,np.transpose([O3,NO2,SO2,CO]),delimiter=',')

file.close()
print(f'Program executed in {time.time()-t0} seconds')
import numpy as np
import time 
from datetime import datetime


t0=time.time()

path='./data.csv'

taille_de_fichier = 10_000

O3=np.random.uniform(low=0,high=1,size=taille_de_fichier)
NO2=np.random.binomial(0,1,size=taille_de_fichier) # Parameters : -n int or array_like of ints Parameter of the distribution, 
                                        #              >= 0. Floats are also accepted, but they will be truncated to integers. 
                                        #              
										# 	 		   -p float or array_like of floats
                                        # 				Parameter of the distribution, >= 0 and <=1.

SO2=np.random.gamma(0,scale=1,size=taille_de_fichier) #Parameters shape  : float or array_like of floats ; The shape of the gamma distribution. Must be non-negative.
CO=np.random.exponential(scale=1,size=taille_de_fichier)



np.savetxt(path,np.transpose([O3,NO2,SO2,CO]),delimiter=',',header=f'File generated on : {datetime.now()} by damien \n O3,NO2,SO2,CO')

print(f'Program executed in {time.time()-t0} seconds')
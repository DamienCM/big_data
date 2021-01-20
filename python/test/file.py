import os
import time 

to=time.time()


file=open('data.csv','r')
lines=file.readlines()


count=[0,0,0,0]
minis=[10,10,10,10]
maxis=[0,0,0,0]
means=[0,0,0,0]

for line in lines :
	try :
		data_line=line.split(',')
		for i in range(4):
			data=float(data_line[i])
			if data>.5:
				count[i]+=1
				means[i]+=data

				if data < minis[i]:
					minis[i]=data
				
				if data[i] > maxis[i]:
					maxis[i]=data[i]
	except :
		pass
			
file.close()

for i in range(4):
	means[i]/=count[i]

print(count,minis,maxis,means)

print(f"Executed in {time.time()-to} seconds")
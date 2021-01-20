import os
import time

to=time.time()


file=open('/home/hadoop/PycharmProjects/big_data/python/generation_fichier/data_10GB.csv','r')


count=[0,0,0,0]
minis=[10,10,10,10]
maxis=[0,0,0,0]
means=[0,0,0,0]

j = 0
while 1:
	j += 1
	if j % 10000 == 0:
		print(float(j*(100/100_000_000)))
	try:
		line = file.readline()
		if not line:
			break
		data_line = line.split(',')
		for i in range(4):
			data = float(data_line[i])
			if data > .5:
				count[i] += 1
				means[i] += data

				minis[i] = min(minis[i], data)
				maxis[i] = max(maxis[i], data)
	except:
		pass




file.close()

for i in range(4):
	means[i] /= count[i]

print(count, minis, maxis, means)

print(f"Executed in {time.time()-to} seconds")
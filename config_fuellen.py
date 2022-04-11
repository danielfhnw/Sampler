import os
import csv


files = os.listdir('../../../media/pi/SAMPLER')
files.sort()
index = 0

file = open('../../../media/pi/SAMPLER/SamplerConfig.csv', 'r')
reader = csv.reader(file, delimiter=';')
existing = []
for row in reader:
    existing.append(row[1])
existing = existing[1:]
file.close()

file = open('../../../media/pi/SAMPLER/SamplerConfig.csv', 'a')
writer = csv.writer(file, delimiter=';')

for f in files:
    end = f[-4:]
    if end==".wav" and not f in existing:
        row = ['x', f, '1']
        writer.writerow(row)
        print("appended " + f)
file.close()
print("finished")

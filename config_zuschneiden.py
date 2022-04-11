import os
import csv


files = os.listdir('../../../media/pi/SAMPLER')
files.sort()
index = 0

file = open('../../../media/pi/SAMPLER/SamplerConfig.csv', 'r')
reader = csv.reader(file, delimiter=';')
existing_n = []
existing_s = []
existing_v = []
for row in reader:
    existing_n.append(row[0])
    existing_s.append(row[1])
    existing_v.append(row[2])
existing_n = existing_n[1:]
existing_s = existing_s[1:]
existing_v = existing_v[1:]
file.close()

file = open('../../../media/pi/SAMPLER/SamplerConfig.csv', 'w')
writer = csv.writer(file, delimiter=';')
head = (['Nr', 'Sound', 'Volume'])
writer.writerow(head)

sounds = []
for f in files:
    end = f[-4:]
    if end==".wav":
        sounds.append(f)
        
for i in range(len(existing_n)):
    if existing_s[i] in sounds:
        row = [existing_n[i], existing_s[i], existing_v[i]]
        writer.writerow(row)
    else:
        print("removed " + existing_s[i])
               
file.close()
print("finished")


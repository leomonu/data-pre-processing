import csv

data_set1 = []
data_set2 = []

with open("dataset_1.csv","r")as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data_set1.append(row)

with open("sorted_dataset2.csv","r")as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data_set2.append(row)

headers1 = data_set1[0]
planet_data_1 = data_set1[1:]
headers2 = data_set2[0]
planet_data_2 = data_set2[1:]
planet_data = []
headers = headers1+headers2
for index,data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open("final.csv","a+")as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
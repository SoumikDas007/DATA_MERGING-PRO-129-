import csv 

dataset_1 = [] 
dataset_2 = [] 

with open("brightest_stars.csv", "r") as f:
    csvreader = csv.reader(f) 
    for i in csvreader: 
        dataset_1.append(i) 

with open("converted_stars.csv", "r") as f: 
    csvreader = csv.reader(f)   
    for i in csvreader: 
        dataset_2.append(i) 
    
headers_1 = dataset_1[0] 
data_1 = dataset_1[1:] 

headers_2 = dataset_2[0] 
data_2 = dataset_2[1:] 

headers = headers_1 + headers_2 
data = [] 
for i in data_1:
    data.append(i)
for j in data_2:
    data.append(j) 
    
with open("data_merged.csv", "a+") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(data)
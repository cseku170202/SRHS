import csv
import pandas as pd

initial_data = []
textFile = open('initial_incorrect_data.txt', 'w', encoding='utf-8')
textFile1 = open('sorted_initial_incorrect_data.txt', 'w', encoding='utf-8')
textFile2 = open('unique_sorted_initial_incorrect_data.txt', 'w', encoding='utf-8')

with open('result.csv','r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:

        word = line[2].split()
        for i in word:
            textFile.write(i)
            textFile.write('\n')
            initial_data.append(i)
print(initial_data)
initial_data.sort()

for i in initial_data:
    textFile1.write(i)
    textFile1.write('\n')

Unique_data = set(initial_data)
Unique_data = list(Unique_data)
Unique_data.sort()

for i in Unique_data:
    textFile2.write(i)
    textFile2.write('\n')







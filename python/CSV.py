import csv


#CSV -> Comma separated Values
#What separated the values is called a delimeter

#READING FROM A CSV FILE
with open('csvTestFile.csv', 'r') as csvFileObj:
    #csvReader = csv.reader(csvFileObj, delimiter=",")          #Returns value in list format
    csvReader = csv.DictReader(csvFileObj, delimiter=",")       #Returns value in dictionary format

    count = 0
    for line in csvReader:
        if count != 0:
            print(f'{count}. {line}')
        count += 1


#WRITING TO A CSV FILE

with open('csvTestFile.csv', 'r') as csvFileObj:
    csvReader = csv.reader(csvFileObj, delimiter=",")

    with open('csvTestFile2.csv', 'w') as csvFileObj2:
        csvWriter = csv.writer(csvFileObj2, delimiter="%")

        for line in csvReader:
            csvWriter.writerow(line)
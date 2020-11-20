import csv

crime_count = {}

with open('Crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if '2015' in row[2]:
            if row[5] in crime_count:
                crime_count[row[5]] += 1
            else:
                crime_count[row[5]] = 0

print(max(crime_count, key=lambda key: int(crime_count[key])))

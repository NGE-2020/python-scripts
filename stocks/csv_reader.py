import csv

stocks = {'APPL'}

with open('amex.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		stocks.add(row[0])

with open('nasdaq.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
                stocks.add(row[0])

with open('nyse.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
                stocks.add(row[0])


print(len(stocks))




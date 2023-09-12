import csv
with open('Visitor.csv','r') as csvis:
    myreader = csv.reader(csvis)
    for r in myreader:
        print(r)

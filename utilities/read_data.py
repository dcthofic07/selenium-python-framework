import csv


def getCSVData(fileName):
    rows = []
    datafile = open(fileName, "r")
    reader = csv.reader(datafile)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows
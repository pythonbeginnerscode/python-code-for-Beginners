import csv
from datetime import datetime  # for date and time

path = "/Users/kirankumar/Downloads/EQ080120 2.CSV"
file = open(path, newline='')  # empty string for the newline
reader = csv.reader(file)  # to pass csv data from the file

header = next(reader)  # first line is the header
# data =[row for row in reader]  # read the remaining data
# print(header)
# print(data[1])   # data treated as a string
data = []
for row in reader:
    sc_code = int(row[0])
    sc_name = str(row[1])
    open_price = str(row[4])  # open is a built in function so we use open_price
    high = str(row[5])
    low = float(row[6])
    close = float(row[7])
    data.append([sc_code,sc_name,open_price, high, low, close, close])
# compute and store dialy stock returns
print(data[0])
print(data[1])
print(data[2])
print(data[3])







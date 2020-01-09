import csv
from datetime import datetime  # for date and time

path = "/Users/kirankumar/Desktop/Google Stock Market Data - google_stock_data.csv.csv"
file = open(path, newline='')  # empty string for the newline
reader = csv.reader(file)  # to pass csv data from the file

header = next(reader)  # first line is the header
# data =[row for row in reader]  # read the remaining data
# print(header)
# print(data[1])   # data treated as a string
data = []
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])  # open is a built in function so we use open_price
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    data.append([date, open_price, high, low, close, volume, adj_close])
# compute and store dialy stock returns
returns_path = "/Users/kirankumar/Desktop/Google Stock Market Data - google_stock_data.csv.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])
for i in range(len(data) - 1): # here we need only single day so we use -1
    todays_row = data[i] #using i for to get todays data
    todays_date = todays_row[0]   #first element in todays list
    todays_price - todays_row[-1]  #last element in todays list because ates are in decreasing order
    yesterdays_row = data[i+1]  # yesterday data
    yesterdays_price = yesterdays_row[-1]  #yesterday price
    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime("%m/%d/%Y")
    writer.writerow([formatted_date,daily_return])



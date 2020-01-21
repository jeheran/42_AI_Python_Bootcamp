import csv
from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        data = file.getdata()
        header = file.getheader()
        print(data)

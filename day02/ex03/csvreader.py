import csv, json
import pandas as pd
import pprint

class CsvReader():

    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom = 0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

        sep = ' ' if sep == '' else sep

    def __enter__(self):
        self.fd = open(self.filename, 'r')
        return self

    def getdata(self):
        js = []
        i = self.skip_top
        self.reader = csv.DictReader(self.fd, delimiter=self.sep)
        title = self.reader.fieldnames
        for row in self.reader:
            js.extend([{title[i]:row[title[i]] for i in range(len(title))}])
            i += 1
        return js

    def getheader(self):
        header = self.reader.fieldnames
        return header

    def __exit__(self, *args):
        self.fd.close()
        return self


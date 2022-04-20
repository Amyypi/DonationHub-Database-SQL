import pandas as pd
import csv
import sys

def Total(file):
        fp = file
        dataset = pd.read_csv(fp)
        df = pd.DataFrame(dataset)
        column = df[df.columns[1]]
        data = list(column)
        s = 0
        for x in data:
                s = s + int(x)
        return s

def main():
        total = Total(sys.argv[1])
        print(total)
main()



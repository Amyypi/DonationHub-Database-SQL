import pandas as pd
import csv

def Total(file,colIndex):
        fp = file
        dataset = pd.read_csv(fp)
        df = pd.DataFrame(dataset)
        column = df[df.columns[colIndex]]
        data = list(column)
        s = 0
        for x in data:
                s = s + int(x)
        return s

def main():
        #Just change file to any dataset csv file and just enter the column number you want to calculater --- Oh remember that column numbers start at 0 so 3rd column is actually 2 not 3

        #Below are some example you can uncomment and see...

        #Example of County Population
        #file = "CountyPopulations.csv"
        #colnum = 3

        #Example of State Popluation
        #file = "StatePopulations.csv"
        #colnum = 3

        #Example of poverty estimate
        #file = "poverty.csv"
        #colnum = 1

        #Example of Unemployed People
        #file = "unemployment.csv"
        #colnum = 1
        
        total = Total(file,colnum)
        print("SUM: " + str(total))
main()



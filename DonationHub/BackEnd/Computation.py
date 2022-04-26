from statistics import mean
import pandas as pd

def getData(file,colIndex):
        dataset = pd.read_csv(file)
        df = pd.DataFrame(dataset)
        column = df[df.columns[colIndex]]
        data = list(column)
        sizeOfData = len(data)
        return (data,sizeOfData)

def Total(data):
        return sum(data)

def Average(data):
        return mean(data)

def Count(size):
        return size

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

        #Example of Number of Charities
        file = "charities.csv"
        colnum = 1
        
        data,sizeOfData = getData(file,colnum)
        """"
        total = Total(data)
        avg = Average(data)
        print("SUM: " + str(total))
        print("Average: " + str(avg))
        """
        numOfCharities = Count(sizeOfData)
        print("numOfCharities: " + str(numOfCharities))

main()



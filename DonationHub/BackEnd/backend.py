import sqlite3
import pandas as pd
from statistics import mean

statePop = 3
countyPop = 6
povertyEstimate = 7
unemployedPeople = 7
unemploymentRate = 8
charities = 5

con = sqlite3.connect("data.db")
cur = con.cursor()

# View and Retrieve Data
def getOnlyStateAndCountyTable(stateLst,countyLst):
        query1 = "create temp table tb(STATEID INT, STATENAME TEXT, ABBREVIATION TEXT, STATEPOP INT,COUNTYID INT, COUNTYNAME TEXT, COUNTYPOP INT)"
        query2 = "insert into tb select s.*, c.COUNTYID, c.COUNTYNAME, c.COUNTYPOP from states as s natural join counties as c"
        cur.execute(query1)
        cur.execute(query2)
        query3 = f"create temp table tb1 as SELECT * FROM tb WHERE tb.STATENAME in ({','.join(['?']*len(stateLst))})"
        cur.execute(query3, stateLst)
        query4 = f"SELECT * FROM tb1 WHERE tb1.COUNTYNAME in ({','.join(['?']*len(countyLst))})"
        cur.execute(query4, countyLst)
        records = cur.fetchall()
        return records

def getOnlyPovertyTable(stateLst,countyLst):
        query1 = "create temp table tb(STATEID INT,STATENAME TEXT,ABBREVIATION TEXT,STATEPOP INT,COUNTYID INT,COUNTYNAME TEXT,COUNTYPOP INT,POVERTY_ESTIMATE INT)"
        query2 = "insert into tb select s.*, c.COUNTYID, c.COUNTYNAME, c.COUNTYPOP, p.POVERTY_ESTIMATE from states as s natural join counties as c natural join poverty as p"
        cur.execute(query1)
        cur.execute(query2)
        query3 = f"create temp table tb1 as SELECT * FROM tb WHERE tb.STATENAME in ({','.join(['?']*len(stateLst))})"
        cur.execute(query3, stateLst)
        query4 = f"SELECT * FROM tb1 WHERE tb1.COUNTYNAME in ({','.join(['?']*len(countyLst))})"
        cur.execute(query4, countyLst)
        records = cur.fetchall()
        return records

def getOnlyUnemploymentTable(stateLst,countyLst):
        query1 = "create temp table tb(STATEID INT,STATENAME TEXT,ABBREVIATION TEXT,STATEPOP INT,COUNTYID INT,COUNTYNAME TEXT,COUNTYPOP INT,UNEMPLOYED_PEOPLE INT,UNEMPLOYMENT_RATE INT)"
        query2 = "insert into tb select s.*, c.COUNTYID, c.COUNTYNAME, c. COUNTYPOP, u.UNEMPLOYED_PEOPLE, u.UNEMPLOYMENT_RATE from states as s natural join counties as c natural join unemployment as u"
        cur.execute(query1)
        cur.execute(query2)
        query3 = f"create temp table tb1 as SELECT * FROM tb WHERE tb.STATENAME in ({','.join(['?']*len(stateLst))})"
        cur.execute(query3, stateLst)
        query4 = f"SELECT * FROM tb1 WHERE tb1.COUNTYNAME in ({','.join(['?']*len(countyLst))})"
        cur.execute(query4, countyLst)
        records = cur.fetchall()
        return records

def getOnlyCharitiesTable(stateLst):
        query1 = "create temp table tb(STATEID INT,STATENAME TEXT,ABBREVIATION TEXT,STATEPOP INT,ORGID INT,ORGANIZATION_NAME TEXT)"
        query2 = "insert into tb select s.*, c.ORGID, c.ORGANIZATION_NAME from states as s natural join charities as c"
        cur.execute(query1)
        cur.execute(query2)
        query3 = f"SELECT tb.* FROM tb WHERE tb.STATENAME in ({','.join(['?']*len(stateLst))})"
        cur.execute(query3,stateLst)
        records = cur.fetchall()
        return records

def getDefaultTable(stateLst,countyLst):
        query1 = "create temp table tb(STATEID INT,STATENAME TEXT,ABBREVIATION TEXT,STATEPOP INT,COUNTYID INT,COUNTYNAME TEXT,COUNTYPOP INT, POVERTY_ESTIMATE INT,UNEMPLOYED_PEOPLE INT, UNEMPLOYMENT_RATE INT)"
        query2 = "insert into tb select s.*, c.COUNTYID, c.COUNTYNAME, c.COUNTYPOP, p.POVERTY_ESTIMATE, u.UNEMPLOYED_PEOPLE, u.UNEMPLOYMENT_RATE from states as s natural join counties as c natural join poverty as p natural join unemployment as u"
        cur.execute(query1)
        cur.execute(query2)
        query3 = f"create temp table tb1 as SELECT * FROM tb WHERE tb.STATENAME in ({','.join(['?']*len(stateLst))})"
        cur.execute(query3, stateLst)
        query4 = f"SELECT * FROM tb1 WHERE tb1.COUNTYNAME in ({','.join(['?']*len(countyLst))})"
        cur.execute(query4, countyLst)
        records = cur.fetchall()
        return records

def getCountiesList(stateLst):
        query1 = "create temp table tb (STATEID INT, STATENAME TEXT, ABBREVIATION TEXT, STATEPOP INT,COUNTYID INT, COUNTYNAME TEXT, COUNTYPOP INT)"
        query2 = "insert into tb select s.*, c.COUNTYID, c.COUNTYNAME, c.COUNTYPOP from states as s natural join counties as c"
        cur.execute(query1)
        cur.execute(query2)
        query3 = f"SELECT tb.COUNTYNAME FROM tb WHERE tb.STATENAME in ({','.join(['?']*len(stateLst))})"
        cur.execute(query3,stateLst)
        records = cur.fetchall()
        return records

# Computations
def getData(dataset,colIndex):
        df = pd.DataFrame(dataset)
        column = df[df.columns[colIndex]]
        data = list(column)
        return data

def Total(data):
        return sum(data)

def Average(data):
        return mean(data)

def Count(data):
        return len(data)

def getCountiesTotalPopulation(records):
        data = getData(records,countyPop)
        return Total(data)

def getCountiesAveragePopulation(records):
        data = getData(records,countyPop)
        return Average(data)

def getTotalPovertyEstimates(records):
        data = getData(records,povertyEstimate)
        return Total(data)

def getAveragePovertyEstimates(records):
        data = getData(records,povertyEstimate)
        return Average(data)

def getTotalUnEmployedPeople(records):
        data = getData(records,unemployedPeople)
        return Total(data)

def getAverageUnEmployedPeople(records):
        data = getData(records,unemployedPeople)
        return Average(data)

def getAverageUnEmploymentRate(records):
        data = getData(records,unemploymentRate)
        return Average(data)

def getTotalCharities(records):
        data = getData(records,unemploymentRate)
        return Count(data)

def main():
        states = ['Maryland','Alaska']
        records = getOnlyCharitiesTable(states)
        df = pd.DataFrame(records)
        df.to_csv("sol.csv")
        con.commit()
        con.close()

main()

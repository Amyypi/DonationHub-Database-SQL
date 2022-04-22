import sqlite3
import csv

con = sqlite3.connect("data.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS states")
cur.execute("DROP TABLE IF EXISTS counties")
cur.execute("DROP TABLE IF EXISTS poverty")
cur.execute("DROP TABLE IF EXISTS unemployment")
cur.execute("DROP TABLE IF EXISTS charities")
 
# Creating the tables
cur.execute('''CREATE TABLE states(
        STATEID INT PRIMARY KEY,
   	STATENAME TEXT,
	ABBREVIATION TEXT,
        STATEPOP INT);''')

cur.execute('''CREATE TABLE counties(
        STATEID INT,
        COUNTYID INT PRIMARY KEY,
   	COUNTYNAME TEXT,
        COUNTYPOP INT,
        FOREIGN KEY(STATEID) REFERENCES states(STATEID));''')

cur.execute('''CREATE TABLE poverty(
        COUNTYID INT PRIMARY KEY,
        POVERTY_ESTIMATE INT,
        FOREIGN KEY(COUNTYID) REFERENCES counties(COUNTYID));''')

cur.execute('''CREATE TABLE unemployment(
        COUNTYID INT PRIMARY KEY,
        UNEMPLOYED_PEOPLE INT,
        UNEMPLOYMENT_RATE INT,
        FOREIGN KEY(COUNTYID) REFERENCES counties(ID));''')

cur.execute('''CREATE TABLE charities(
        STATEID INT,
        ORGID INT PRIMARY KEY,
        ORGANIZATION_NAME TEXT,
        FOREIGN KEY(STATEID) REFERENCES states(STATEID));''')

#Inserting data into the tables
a_file = open("Database/StatePopulations.csv")
b_file = open("Database/CountyPopulations.csv")
c_file = open("Database/poverty.csv")
d_file = open("Database/unemployment.csv")
e_file = open("Database/charities.csv")

rows = csv.reader(a_file)
cur.executemany("INSERT INTO states (STATEID,STATENAME,ABBREVIATION,STATEPOP) VALUES (?,?,?,?);", rows)
rows = csv.reader(b_file)
cur.executemany("INSERT INTO counties (STATEID,COUNTYID,COUNTYNAME,COUNTYPOP) VALUES (?,?,?,?);", rows)
rows = csv.reader(c_file)
cur.executemany("INSERT OR IGNORE INTO poverty (COUNTYID,POVERTY_ESTIMATE) VALUES (?,?);", rows)
rows = csv.reader(d_file)
cur.executemany("INSERT OR IGNORE INTO unemployment (COUNTYID,UNEMPLOYED_PEOPLE,UNEMPLOYMENT_RATE) VALUES (?,?,?);", rows)
rows = csv.reader(e_file)
cur.executemany("INSERT OR IGNORE INTO charities (STATEID,ORGID,ORGANIZATION_NAME) VALUES (?,?,?);", rows)

con.commit()
con.close()
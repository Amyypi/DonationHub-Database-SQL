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
        ID INT PRIMARY KEY,
   	STATENAME TEXT,
	ABBREVIATION TEXT,
        STATEPOP INT);''')

cur.execute('''CREATE TABLE counties(
        STATEID INT,
        ID INT PRIMARY KEY,
   	COUNTYNAME TEXT,
        COUNTYPOP INT,
        FOREIGN KEY(STATEID) REFERENCES states(ID));''')

cur.execute('''CREATE TABLE poverty(
        COUNTYID INT PRIMARY KEY,
        POVERTY_ESTIMATE INT,
        FOREIGN KEY(COUNTYID) REFERENCES counties(ID));''')

cur.execute('''CREATE TABLE unemployment(
        COUNTYID INT PRIMARY KEY,
        UNEMPLOYED_PEOPLE INT,
        UNEMPLOYED_RATE INT,
        FOREIGN KEY(COUNTYID) REFERENCES counties(ID));''')

cur.execute('''CREATE TABLE charities(
        STATEID INT,
        ID INT PRIMARY KEY,
        ORGANIZATION_NAME TEXT,
        FOREIGN KEY(STATEID) REFERENCES states(ID));''')

#Inserting data into the tables
a_file = open("StatePopulations.csv")
b_file = open("CountyPopulations.csv")
c_file = open("poverty.csv")
d_file = open("unemployment.csv")
e_file = open("charities.csv")

rows = csv.reader(a_file)
cur.executemany("INSERT INTO states (ID,STATENAME,ABBREVIATION,STATEPOP) VALUES (?,?,?,?);", rows)
rows = csv.reader(b_file)
cur.executemany("INSERT INTO counties (STATEID,ID,COUNTYNAME,COUNTYPOP) VALUES (?,?,?,?);", rows)
rows = csv.reader(c_file)
cur.executemany("INSERT OR IGNORE INTO poverty (COUNTYID,POVERTY_ESTIMATE) VALUES (?,?);", rows)
rows = csv.reader(d_file)
cur.executemany("INSERT OR IGNORE INTO unemployment (COUNTYID,UNEMPLOYED_PEOPLE,UNEMPLOYED_RATE) VALUES (?,?,?);", rows)
rows = csv.reader(e_file)
cur.executemany("INSERT OR IGNORE INTO charities (STATEID,ID,ORGANIZATION_NAME) VALUES (?,?,?);", rows)

con.commit()
con.close()
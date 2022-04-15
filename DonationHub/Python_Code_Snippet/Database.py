import sqlite3
import csv

con = sqlite3.connect("data.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS states")
cur.execute("DROP TABLE IF EXISTS counties")
cur.execute("DROP TABLE IF EXISTS poverty")
cur.execute("DROP TABLE IF EXISTS unemployment")
#cur.execute("DROP TABLE IF EXISTS charities")
 
# Creating the tables
cur.execute('''CREATE TABLE states(
        ID INT PRIMARY KEY,
   	NAME TEXT,
	ABBREVIATION TEXT,
        POP INT);''')

cur.execute('''CREATE TABLE counties(
        STATEID INT,
        ID INT PRIMARY KEY,
   	NAME TEXT,
        POP INT,
        FOREIGN KEY(STATEID) REFERENCES states(ID));''')

cur.execute('''CREATE TABLE poverty(
        COUNTYID INT,
        POVERTY INT,
        FOREIGN KEY(COUNTYID) REFERENCES counties(ID));''')

cur.execute('''CREATE TABLE unemployment(
        COUNTYID INT,
        NUMOFPEOPLE INT,
        RATE INT,
        FOREIGN KEY(COUNTYID) REFERENCES counties(ID));''')

"""
cur.execute('''CREATE TABLE charities(
        COUNTYID INT,
        ID INT PRIMARY KEY,
        NAME TEXT,
        FOREIGN KEY(COUNTYID) REFERENCES counties(ID));''')
"""

#Inserting data into the tables
a_file = open("StatePopulations.csv")
b_file = open("CountyPopulations.csv")
c_file = open("poverty.csv")
d_file = open("unemployment.csv")
#e_file = open("charities.csv")

rows = csv.reader(a_file)
cur.executemany("INSERT INTO states (ID,NAME,ABBREVIATION,POP) VALUES (?,?,?,?);", rows)
rows = csv.reader(b_file)
cur.executemany("INSERT INTO counties (STATEID,ID,NAME,POP) VALUES (?,?,?,?);", rows)
rows = csv.reader(c_file)
cur.executemany("INSERT INTO poverty (COUNTYID,POVERTY) VALUES (?,?);", rows)
rows = csv.reader(d_file)
cur.executemany("INSERT INTO unemployment (COUNTYID,NUMOFPEOPLE,RATE) VALUES (?,?,?);", rows)
#rows = csv.reader(e_file)
#cur.executemany("INSERT INTO charities (STATEID,ID,NAME) VALUES (?,?,?);", rows)

con.commit()
con.close()
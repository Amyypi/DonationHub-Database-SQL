import sqlite3
import csv
con = sqlite3.connect("data.db")
cur = con.cursor()

a_file = open("StatePopulations.csv")
rows = csv.reader(a_file)
cur.executemany("INSERT INTO data VALUES (?, ?)", rows)

cur.execute("SELECT * FROM data")
print(cur.fetchall())
con.commit()
con.close()
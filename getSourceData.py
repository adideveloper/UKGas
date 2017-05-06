import sqlite3
import time
import pandas as pd
import matplotlib.pyplot as plt

# SQLLite Connection
#conn = sqlite3.connect('ukGas.sqlite')
#conn.text_factory = str
#cur = conn.cursor()

#cur.execute('''CREATE TABLE IF NOT EXISTS ukgas_usage
#    (id INTEGER UNIQUE, time_used TEXT, usage NUMBER)''')

#cur.execute('''INSERT OR IGNORE INTO ukgas_usage (id, time_used, usage)
#        VALUES ( ?, ?, ? )''', ( start, email, sent_at, subject, hdr, body))

#conn.commit()

dateparse = lambda dates: [pd.datetime.strptime(d, '%H:%M:%S') for d in dates]

rd = pd.read_csv('C:\Users\\adity\Downloads\UKgas.csv', sep=',', encoding='latin1', usecols=[1,2], date_parser=dateparse, index_col='time' )

#print rd.groupby(by=['time'])['UKgas'].sum()
#plt.show(rd.plot())

plt.show(rd.groupby(by=['time'])['UKgas'].sum().plot.bar())

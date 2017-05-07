
import pandas as pd
import matplotlib.pyplot as plt

rd = pd.read_csv('C:\Users\\adity\Downloads\UKgas.csv', sep=',', encoding='latin1', usecols=[1,2], names=['Time', 'Gas'], skiprows=1)

#print rd.groupby(by=['time'])['UKgas'].sum()
#plt.show(rd.plot())

#Display Total Gas usages gropu by Time
plt.show(rd.groupby(by=['Time'])['Gas'].sum().plot())

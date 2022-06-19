import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot

#prova[['Date/time','Total g']]
prova = pd.read_csv('/home/rgb/Documenti/HeaderLog.csv')

meanValue = prova['Total g'].mean()
maxValue = prova['Total g'].max()
indexPeaks=prova.index[prova['Total g'] > (meanValue+0.021)].tolist()
#print(maxValue)
print(indexPeaks)
#print(type(indexPeaks))
#print(meanValue)
j=1
i=0
indexPeaksExtended=[]
indexPeaksExtended1=[]
indexPeaksExtended2=[]
indexPeaksExtended3=[]
indexPeaksExtended4=[]
indexPeaksExtended5=[]

indexPeaksExtended.append(indexPeaks[0])#indexPeaks.copy()
#print(indexPeaksExtended)

for i in range(1):#(len(indexPeaks)):
    #print(indexPeaks[i])
    for j in range(200):  
        indexPeaksExtended.append(indexPeaks[i]-j)
        indexPeaksExtended.append(indexPeaks[i]+j)
        
indexPeaksExtended.sort()
indexPeaksExtended = list(set(indexPeaksExtended))
#print(indexPeaksExtended)  
#prova.reset_index(inplace=True)
#prova[['Date/time','Total g']]
#prova.drop_duplicates(inplace=True)
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 6,
                       ):
    print(prova.iloc[indexPeaksExtended,[0,4,7,8]])
#print("Media", prova.iloc[indexPeaksExtended,[4]].mean())
prova.iloc[indexPeaksExtended,[0,4,7,8]].plot(kind='line', color='red')

indexPeaksExtended1.append(indexPeaks[1])
j=1
for j in range(100):
    indexPeaksExtended1.append(indexPeaks[1]-j)
    indexPeaksExtended1.append(indexPeaks[1]+j)
indexPeaksExtended1.sort()
indexPeaksExtended1 = list(set(indexPeaksExtended1))
print(prova.iloc[indexPeaksExtended1,[0,4,7,8]])
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 6,
                       ):
    print(prova.iloc[indexPeaksExtended1,[0,4,7,8]])
#print(prova.iloc[indexPeaksExtended1,[4]].mean())
prova.iloc[indexPeaksExtended1,[0,4]].plot(kind='line', color='blue')

indexPeaksExtended2.append(indexPeaks[2])
j=1
for j in range(100):
    indexPeaksExtended2.append(indexPeaks[2]-j)
    indexPeaksExtended2.append(indexPeaks[2]+j)
indexPeaksExtended2.sort()
indexPeaksExtended2 = list(set(indexPeaksExtended2))
print(prova.iloc[indexPeaksExtended2,[0,4,7,8]])
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 6,
                       ):
    print(prova.iloc[indexPeaksExtended2,[0,4,7,8]])
#print(prova.iloc[indexPeaksExtended1,[4]].mean())
prova.iloc[indexPeaksExtended2,[0,4]].plot(kind='line', color='green')

indexPeaksExtended3.append(indexPeaks[4])
j=1
for j in range(100):
    indexPeaksExtended3.append(indexPeaks[4]-j)
    indexPeaksExtended3.append(indexPeaks[4]+j)
indexPeaksExtended3.sort()
indexPeaksExtended3 = list(set(indexPeaksExtended3))
print(prova.iloc[indexPeaksExtended3,[0,4,7,8]])
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 6,
                       ):
    print(prova.iloc[indexPeaksExtended3,[0,4,7,8]])
#print(prova.iloc[indexPeaksExtended1,[4]].mean())
prova.iloc[indexPeaksExtended3,[0,4]].plot(kind='line', color='orange')
import pandas as pd
import numpy as np

s=[]
E=[]
b=[]
t=[]
hits=[]
miss=[]
evict=[]
with open('/home/sturla/cCode/verk2/useData/result.txt') as f:
    for Line in f:
        if(Line != "\n"):
            splitLine = np.asarray(Line.split())
            if(len(splitLine) == 14):
            	#print('s='+splitLine[4]+' E='+splitLine[7]+' b='+splitLine[10]+' file='+splitLine[13])
            	s.append(splitLine[4])
            	E.append(splitLine[7])
            	b.append(splitLine[10])
            	t.append(splitLine[13])
            elif(len(splitLine) == 6):
            	#print('hits='+splitLine[1]+' miss='+splitLine[3]+' e='+splitLine[5])
            	hits.append(splitLine[1])
            	miss.append(splitLine[3])
            	evict.append(splitLine[5])
            	
df = pd.DataFrame({'s':s, 'E':E, 'b':b, 'traceFile':t, 'hits':hits, 'misses':miss, 'evictions':evict})
df.to_csv('allResults.csv', index=False, encoding='utf-8')
f.close()

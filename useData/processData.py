import pandas as pd

with open('/home/sturla/cCode/verk2/useData/result.txt') as f:
    for Line in f:
        if(Line != "\n"):
            print(Line)
f.close()
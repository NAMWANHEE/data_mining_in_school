import pandas as pd
import numpy as np
from pandas import Series, DataFrame
# pandas Series
obj = pd.Series([4,7,-5,3])
print(obj)
print(obj.values)
print(obj.index)

obj2 = pd.Series([4,7,-5,3], index=['d','b','a','c'])
print(obj2)

print(obj2['a'])
obj2['d'] = 6
OB = obj2[['c','a','d']]
print(OB)
print(obj2)
print(obj2[obj2>0])
print(obj2 * 2)
print(np.exp(obj2))

sdata={'Ohio': 35000,'Texas' : 71000,'Oregon': 16000,'Utah' : 5000}
obj3 = pd.Series(sdata)
print(obj3)

states = ['California','Ohio','Oregon','Texas']
obj4 = pd.Series(sdata , index=states)
print(obj4)

print(pd.isnull(obj4))
print(pd.notnull(obj4))

obj4.name='population'
obj4.index.name = 'state'
print(obj4)

print(obj)
obj.index = ['Bob','Steve','Jeff','Ryan']
print(obj)
print()

#pandas DataFrame

data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002,2003],
        'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame = pd.DataFrame(data)
print(frame)
print(pd.DataFrame(data,columns=['year','state','pop']))

frame2 = pd.DataFrame(data,columns=['year','state','pop','debt'],
                      index=['one','two','three','four','five','six'])
print(frame2)
print(frame2.columns)

print(frame2.loc['three'])

frame2['eastern'] = frame2['state'] == 'Ohio'
print(frame2)

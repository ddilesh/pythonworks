import pandas as pd
defects=pd.Series([5,8,3,6,10,2,7],index=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
print(defects)
print(defects.max())
print(defects.idxmax())
print(defects.min())
print(defects.idxmin())
print(defects.iloc[4])
print(defects.loc['Wed'])
print(defects.sum())


executiontimes=pd.Series([12,15,20,18,25,30,22],index=['TC1','TC2','TC3','TC4','TC5','TC6','TC7'])
print(executiontimes)
print(executiontimes.head(3))
print(executiontimes.mean())
print(executiontimes.iloc[1])
print(executiontimes.loc['TC3'])

passpercent=pd.Series([80,85,78,90,88],index=['B1','B2','B3','B4','B5'])
print(passpercent)
print(passpercent.mean())
print(passpercent.idxmax())
print(passpercent.iloc[-1])
print(passpercent.loc['B3'])
print(passpercent-passpercent.mean())


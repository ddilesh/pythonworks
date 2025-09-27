import pandas as pd

data={
    "TestCase":["TC1","TC2","TC3","TC4","TC5","TC6"],
    "Module":["Login","Login","Payment","Payment","Reports","Reports"],
    "Status":["Passed","Failed","Passed","Failed","Passed","Passed"],
    "Duration":[12,15,20,18,25,22]

}

df4=pd.DataFrame(data)
print(df4)
print(df4.groupby("Status")["TestCase"].count())
print(df4.groupby("Module")["Duration"].mean())

data1={
    "DefectID":["D1","D2","D3","D4","D5"],
    "Module":["Login","Payment","Reports","Login","Payment"],
    "Severity":["High","Medium","Low","High","Medium"],
    "Status":["Open","Closed","Open","Closed","Open"]

}

df5=pd.DataFrame(data1)
print(df5)
print(df5[df5['Status']=="Open"])
print(df5.groupby("Status")["DefectID"].count())



import pandas as pd

data={
    "TestCase":["TC1","TC2","TC3","TC4","TC5"],

 
    "Status":["Passed","Failed","Passed","Failed","Passed"],
    "Duration":[12,15,20,18,25]

}

df=pd.DataFrame(data)
print(df)
print(df["Status"])
print(df[df["Status"]=="Failed"])

df.to_csv("test_results.csv",index=False)

df_r=pd.read_csv('test_results.csv')
print(df_r)



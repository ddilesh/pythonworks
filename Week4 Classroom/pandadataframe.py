import pandas as pd
import numpy as np
array1=np.array([10,20,30])
array2=np.array([30,40,50])
df=pd.DataFrame([array1,array2],index=["Row1","Row2"])
print(df)

series1=pd.Series([100,200,300])
series2=pd.Series([400,500])
df1=pd.DataFrame({'Column1':series1,'Column2':series2})
print(df1)

dict = {'Mani': pd.Series([10, 20, 30]), 'Bala': pd.Series([20, 30])}
df2=pd.DataFrame(dict)
print(df2)






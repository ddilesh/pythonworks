import pandas as pd
import numpy as np
testexecution=[12,15,20,18,25,30,22]
serieslist=pd.Series(testexecution)
middle_three = serieslist[2:5]
print(middle_three)

defects=np.array([10,20,23,45,50])
defectsseries=pd.Series(defects)
print(defectsseries)
print(defectsseries.iloc[1:4])
print(defectsseries[1:4])

engg={"Alex":500,"Steve":200,"Bob":300}
testcasesseries=pd.Series(engg)
print(testcasesseries)
print(testcasesseries.loc['Alex'])


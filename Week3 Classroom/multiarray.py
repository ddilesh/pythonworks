import numpy as np

arr=np.array([10,20,30,40,50,60])
print(arr[2:])
print(arr[3:5])
print(arr[4])
print(arr[::-1])

twoarray=np.array([[0,1,2,3],[4,5,6,7]])
print(twoarray[0,1])
print(twoarray[1][1])
print(twoarray[0][3])
print(type(twoarray))
print(twoarray.ndim)
print(np.sum(twoarray))

total = 0
for row in twoarray:
    for val in row:
        total += val

print("Total Sum:", total)

trr = np.array([
    [[1, 2, 3, 4],
     [5, 6, 7, 8]],
     

    [[13, 14, 15, 16],
     [17, 18, 19, 20]]
    
])
print(trr[0][0][0])
print(trr[0][1][2])
print(trr[1][1][2])
print(type(trr))
print(trr.ndim)



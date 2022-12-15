import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
arr1=np.array([[[1,2,3,4,5],[4,5,6,7,8,9]],[[12,13,14,15,16],[22,23,24,25,26,27]]])
print(arr1)
print(arr)
print(arr1.ndim)
print(arr.ndim)


arr3=np.arange(45).reshape(5,3,3)
print(arr3)

arr4=arr3.reshape(3,3,5)
print(arr4)

arr6=[11,12,13,14,15,16,17,18,19,20]
print(np.concatenate((arr,arr6)))
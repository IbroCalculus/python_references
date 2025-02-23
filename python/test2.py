import numpy as np

arr = np.ones(4,)
print(arr)
print(arr.shape)

expanded = arr[np.newaxis, :]
print(expanded)
print(expanded.shape)


import numpy as np

data = [1, 3, 2, 0, 3]
num_classes = None

if not num_classes:
    num_classes = max(data) + 1

count = len(data)

categorical = np.zeros([count, num_classes], dtype='int')
categorical[range(count), data] = 1

print(categorical)

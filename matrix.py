
"""
fill the matrix diagonally

[[ 1.  2.  4.  7. 11.]
 [ 3.  5.  8. 12. 16.]
 [ 6.  9. 13. 17. 20.]
 [10. 14. 18. 21. 23.]
 [15. 19. 22. 24. 25.]]

"""

import numpy as np

N = 5
a = np.zeros([N, N])

count = 0

for d in range(N):
    for k in range(d+1):
        count += 1
        a[k, d-k] = count
        print(a)

for d in range(1, N):
    for k in range(N-d):
        count += 1
        a[d+k, N-1-k] = count
        print(a)



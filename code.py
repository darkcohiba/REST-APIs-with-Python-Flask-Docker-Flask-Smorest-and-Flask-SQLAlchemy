from typing import Float


arr = [1, 2, 3, 4, 8, 3.2, 5, 2, 3, .5, ]

print(arr[int((len(arr)/2) -0.5)])

from typing import Float

for num in arr:
  if (type(num) is Float):
    print(num)


from datetime import datetime
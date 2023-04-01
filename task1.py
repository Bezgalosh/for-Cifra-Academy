from collections import deque
n, m = int(input()), int(input())
arr = deque(range(1, n+1))
res = [arr[0]]
arr.rotate(m-1)
while arr[0] != res[0]:
    res.append(arr[0])
    arr.rotate(m-1)
result = ''.join(map(str, res))
print(result)
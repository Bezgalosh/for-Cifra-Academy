import argparse
from collections import deque

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int)
parser.add_argument("m", type=int)
args = parser.parse_args()

arr = deque(range(1, args.n+1))
res = [arr[0]]
arr.rotate(args.m-1)
while arr[0] != res[0]:
    res.append(arr[0])
    arr.rotate(args.m-1)
result = ''.join(map(str, res))
print(result)
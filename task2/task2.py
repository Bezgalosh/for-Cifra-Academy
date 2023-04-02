import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("filename") 
args = parser.parse_args()

with open(args.filename, 'r') as f:
    nums = [int(line.strip()) for line in f]

nums.sort()
if len(nums) % 2 == 0:
    median = (nums[len(nums)//2 - 1] + nums[len(nums)//2]) / 2
else:
    median = nums[len(nums)//2]

moves = int(sum(abs(num - median) for num in nums))

print(moves)
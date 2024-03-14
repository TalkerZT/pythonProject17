from random import randint
k = int(input())
n = int(input())
nums = []
nums_count = n
i = 0
while i < nums_count:
    rand_num = randint(0, k)
    nums.append(rand_num)
    i += 1
for n in nums:
    print(n)
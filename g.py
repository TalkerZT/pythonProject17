from random import randint
nums = []
nums_count = 10
i = 0
while i < nums_count:
    rand_num = randint(0, 100)
    nums.append(rand_num)
    i += 1
for n in nums:
    print(n)
g = max(nums)
j = min(nums)
print(g)
print(j)
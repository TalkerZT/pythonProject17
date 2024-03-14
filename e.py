from random import randint
nums = []
nums_count = 20
i = 0
while i < nums_count:
    rand_num = randint(-100, 100)
    nums.append(rand_num)
    i += 1
print(nums)
p_nums = []
g = 0
for n in nums:
    if n > 0:
        p_nums.append(n)
        g += n
print(g)

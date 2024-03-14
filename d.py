from random import randint
nums = []
nums_count = 20
i = 0
while i < nums_count:
    rand_num = randint(-100, 100)
    nums.append(rand_num)
    i += 1
p_nums = []
n_nums = []
print(nums)
for n in nums:
    if n > 0:
        p_nums.append(n)
    if n < 0:
        n_nums.append(n)
print(n_nums)
print(p_nums)
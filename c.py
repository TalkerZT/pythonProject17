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
new_nums = []
for n in nums:
    if n > 50:
        new_nums.append(n)
for n in new_nums:
    print(n)
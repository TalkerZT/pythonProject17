from random import randint
nums = []
nums_count = 1
i = 0
while i < nums_count:
    rand_num = randint(0, 100)
    nums.append(rand_num)
    i += 1
for n in nums:
    print(n)
a = []
h = 0
a_count = 4
i = 0
while i < a_count:
    rand_a = randint(0, 100)
    a.append(rand_a)
    i += 1
for n in a:
    h += n
    print(n)
l = nums - h
if


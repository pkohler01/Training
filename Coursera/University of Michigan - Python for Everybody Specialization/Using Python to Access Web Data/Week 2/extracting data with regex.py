import re

doc = open("regex_sum_1319579.txt")
lst = list()
for line in doc:
    fnd = re.findall('[0-9]+', line)
    lst = lst + fnd
sum = 0
for x in lst:
    sum = sum + int(x)

print(sum)

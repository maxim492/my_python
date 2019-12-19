from math import sqrt

l = [2, 4, 9, 16, 25]

#1)
res = []
for x in range(len(l)):
    res.append(sqrt(l[x]))   
print(res)


#2)
print(list(map(lambda x: sqrt(x),l)))


#3)
print([sqrt(x) for x in l])

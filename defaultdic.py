from collections import defaultdict
dict_d=(('a','1'),('b','4'),('a','5'),('b','6'),('a','9'))
d=defaultdict(list)
for key,value in dict_d:
    d[key].append(value)
print('d=' + str(d.items()))
dict_e=(('a',1),('b',4),('a',2),('b',5),('a',3))
e=defaultdict(list)
for key,value in dict_e:
    e[key].append(value)
print('e=' + str(e.items()))


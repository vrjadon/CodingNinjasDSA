set1={1,2,3,4}
set2={0,2,3,9,88}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))
set1.intersection_update(set2)
print(set1)

s = {}
s.add(4)
s.add(4)
print(len(s))
s1={101,102,102,101,101}
s2={10,11,10,10,102,111}
s1.add(105)
print("added", s1)
s1.update(s2)
print("update", s1)
s1.union(s2)
print("union", s1)
s1.intersection(s2)
print("intersection",s1)
x=s1.copy()
print("copied", x)
print("s1", s1)
print("s2",s2)
z=s1.difference(s2)
print("difference",z)
s2.add('pacchu')
print(s2)
# s2.add(s1)
# print(s2) TypeError: unhashable type: 'set'
# s1.remove(55)
# print(s1)  KeyError: 55

from NumPyCreator import NumPyCreator
npc = NumPyCreator()

a = npc.from_list([[1, 2, 3], [6, 3, 4]])
print(type(a))

b = npc.from_tuple((1, 5, 6))
print(b)


c = npc.from_iterable(range(5))
print(c)
print(type(c))

t = (5, 7)
d = npc.from_shape(t)
print(d)
print(type(c))

e = npc.random(t)
print(e)

f = npc.identity(5)
print(f)

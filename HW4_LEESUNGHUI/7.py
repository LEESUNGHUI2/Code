a = []
for i in range(0, 50):
    a.append(i)
print(f"a : {a}")

b = []
for i in range(0, 50):
    b.append(i**2)
print(f"b : {b}")

#map함수를 이용하여 구현해야 한다.

c = []
list_c = list(map(lambda x: x, range(50)))
print(f"c : {c}")

d = []
d = list(map(lambda x: x**2, range(50)))
print(f"d : {d}")
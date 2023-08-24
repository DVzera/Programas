a = ["Matheus","Marcelo","Andrey","Pedro"]
#        0         1        2        3
#       -4        -3       -2       -1
print(a)

print(a[0])
print(a[2])
print(a[3])
print(a[-4])
print("---------------------------------")

a.append("Maria Joana") 
print(a)
print("---------------------------------")

a.insert(0, "Joao Augusto")
print(a)
print("---------------------------------")

a[0] = "Andre GAY"
print(a)
print("---------------------------------")

print(a[:3])
print(a[3:])
print(a[1:4])
print("---------------------------------")

del a[0]
print(a)
print("---------------------------------")

del a[4]
print(a)
print("---------------------------------")

a.remove("Pedro")
print(a)
print("---------------------------------")

b = a.pop(0)
print(a)
print("---------------------------------")
print(b)
print("---------------------------------")

a.clear()
print(a)
print("---------------------------------")

c = a.copy()
print(c)
print("---------------------------------")

d = a + c
print(d)
print("---------------------------------")
a.append("Maria Joana") 
a.append("Bruno Costa") 
a.append("Joao Augusto") 
a.append("pedro")
a.append("pedro")

print(a.count("Andre"))

print(len(a))
print("---------------------------------")

print(a.index("Joao Augusto"))
print("---------------------------------")

val = [22, 45, 12, 0, 4, 2, 1, 6, 144, 43]

val.sort()
print(val)

print(sorted(val))

val.reverse()
print(val)

if "Andre" in a :
    print("sim, Andre esta na lista")
else :
    print("andré nao esta da lista :D")

min = min(val)
max = max(val)
soma = sum(val)
print(f"O valor minimo {min}, o valor máximo {max}, a soma dos números {soma}")
print("---------------------------------")

print(a)

for i in a:
    if "pedro" in a:
        a.remove("pedro")
print(a)
print("---------------------------------")

for i in range(0,10,2):
    print(i)
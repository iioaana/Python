f = open("spectacole.txt", "r")
g = open("programe.txt", "w")

s = f.readline()
lista = []

while s != "":
    s = s.split(sep=" ", maxsplit=1)
    s[0] = tuple(s[0].split(sep="-"))
    s[1] = s[1].strip("\n")
    s[0] += (s[1],)
    del(s[1])
    lista.append(*s)
    s = f.readline()

lista = sorted(lista, key= lambda x:x[1], reverse=False)
g.write("{} {} {} \n".format(*lista[0]))

index = 0
n = len(lista)

for i in range(1,n):
    if lista[i][0] >= lista[index][1]:
        g.write("{} {} {} \n".format(*lista[i]))
        index = i

f.close()
g.close()









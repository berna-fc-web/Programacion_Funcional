miLista = [1,2,3,4]
print(miLista) 

listaVacia = []
print(listaVacia)

miLista2 = [1, "Hola", True, 3.14, [1,2,3], (1,2,3), {1,2,3}]
print(miLista2)

print(len(miLista))
print(len(miLista2))
print(miLista[0])

print(f"No. de elementos: {len(miLista)}")
print(f"Primer elemento: {miLista[0]}, {miLista[1]}, {miLista[2]}, {miLista[3]}")
print(f"Primer elemento: {miLista[-1]}, {miLista[-2]}, {miLista[-3]}, {miLista[-4]}")

print(miLista[1:-1])
print(miLista[0:3])

print(miLista[0::])

#Para modificar una lista
##miLista[2] = "tres"
#print(miLista)


#insertar la lista [5,"seis", 7,8] al final de la lista miLista

#miLista[3] = [5,"seis", 7,8]
#print(miLista)

miLista[len(miLista):] = [5,"seis", 7,8]
print(miLista) 

#Slices

miLista=[1,2,3,4]
miLista.append("cinco")
print(miLista)

ml=[]
for i in range(1,5):
    ml.append(i)
    
print(ml)

#ml.append([6,7,8])
#print(ml)
ml.extend([6,7,8])
print(ml)
ml.insert(4,"5")
print(ml)

del ml[4]
print(ml)

ml.remove(4)
print(ml)

ml.reverse()
print(ml)

l1=[1,2,3,4,5,6,7,8,9,10]
l2=l1[:]
#print(l1)
l1.reverse()
print(l1)
print(l2)

#la funcion .short() se usa para ordenar una lista
ld=[[5,6],[7,8,2],[1,3,4],[5,6,7]]
print(f"Desordenado: {ld}")
ld.sort()
print(f"Ordenado: {ld}")
#sanet.me

ld=[5,6,7,8,2,1,3,4,5,6,7]
si= sorted(ld)
print(si)

ld=[5,6,7,8,2,1,3,4,5,6,7]
s2= sorted(ld,reverse=True)
print(s2)

valor_maxi = max(ld)
print(valor_maxi)
valor_min = min(ld)
print(valor_min)

repetidos=[]
for i in range (1,8):
    repetidos.append(ld.count(i))
    
print(repetidos)
#un iterable es una colecion o estructura de datos que contiene varios elementos
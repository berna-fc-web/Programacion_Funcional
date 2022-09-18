#escriba una funcion que reciba como argumentos t, m donde t es el limite de tablas de multiplicar que se decean obtener y m hasta que valor de las tablas se desea 
t=int(input("Define el numero de tablas que quieres:"))
m=int(input("Hasta que numero se calculara:"))
        
def tabla(t:int, n:int, spc:int):
    for i in range(1,t+1):
        for j in range (1,m+1):
           print(f"{i:^{spc}} X {j:^{spc}} = {j*i:^{spc}}")

tabla(t,m,5)
tamano=int(input("ingrese numeros: "))
lista=[]
ceros=0
for i in range(tamano):
    valor=int(input("ingrese un valor: "))
    while(valor==0):
        print("ingrese el valor correcto")
        valor=int(input("ingrese un valor: "))
        ceros=ceros+1
    lista.append(valor)
    print(lista[i])

print("Usted intentó ingresar ", ceros, " veces el número cero")
print("El tamaño de la list es: ",len(lista))

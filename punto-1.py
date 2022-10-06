x = int(input("Ingrese el número de múltiplos que quieres que se impriman en pantalla: "))
n = int(input("Ingrese un número: "))
a = 0
for u in range(1,x+1):
    a = a + 1
    m = n * a
    print(m)

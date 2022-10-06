a = int(input("Ingrese la cantidad de números: "))
b = 0
c = 0

for u in range(1,a+1):
    n = int(input("Ingrese el número: "))
    b = b + n
    c = c + 1

p = b / c
print(f"el promedio de la suma de los números ingresados es: {p}")
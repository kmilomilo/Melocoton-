number = int(input("escribe el numero que deseas convertir: "))
cociente = 1

if number < 257:
  for i in range(1,number+1):
    if cociente != 0:
      cociente = number // 2
      modulo = number % 2
      print(modulo)

      number = cociente
else:
  print("el numero tiene que ser menor a 257")

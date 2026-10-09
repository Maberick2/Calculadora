print("CALCULADORA BÁSICA")

while True:
    print("\n1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "5":
        print("Programa terminado.")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción incorrecta. Intenta de nuevo.")
        continue

    try:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Debes ingresar números válidos.")
        continue

    if opcion == "1":
        print("Resultado:", numero1 + numero2)

    elif opcion == "2":
        print("Resultado:", numero1 - numero2)

    elif opcion == "3":
        print("Resultado:", numero1 * numero2)

    elif opcion == "4":
        if numero2 == 0:
            print("No se puede dividir entre cero.")
        else:
            print("Resultado:", numero1 / numero2)
try:
    numero = int(input("Introduce un número entero: "))
    # Autor: Compañero
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
except ValueError:
    print("Error: Debes introducir un número válido.")
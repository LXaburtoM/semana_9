# Buscar palabra en lista
palabras = ["manzana", "banana", "pera", "uva", "naranja"]
buscar = input("Ingrese una palabra para buscar: ")

if buscar in palabras:
    print(f"La palabra '{buscar}' está en la lista.")
else:
    print(f"La palabra '{buscar}' NO está en la lista.")

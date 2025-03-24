import random

def generar_caso_prueba():
    entrada = random.randint(1, 100)
    salida = entrada * 2
    return entrada, salida

with open("test_cases.txt", "w") as f:
    for _ in range(10):
        entrada, salida = generar_caso_prueba()
        f.write(f"{entrada},{salida}\n")

print("Casos de prueba generados y guardados en test_cases.txt")

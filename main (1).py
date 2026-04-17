import random
import time
import matplotlib.pyplot as plt

# Clase Pedido
class Pedido:
    def __init__(self, tiempo_produccion, tiempo_entrega, prioridad):
        self.tiempo_produccion = tiempo_produccion
        self.tiempo_entrega = tiempo_entrega
        self.prioridad = prioridad

    def __repr__(self):
        return f"(Prod:{self.tiempo_produccion}, Ent:{self.tiempo_entrega}, Pri:{self.prioridad})"

# Bubble Sort con animación
def bubble_sort(pedidos, key, reverse=False):
    n = len(pedidos)

    for i in range(n):
        for j in range(0, n - i - 1):

            if (getattr(pedidos[j], key) > getattr(pedidos[j + 1], key)) ^ reverse:
                pedidos[j], pedidos[j + 1] = pedidos[j + 1], pedidos[j]

                # Mostrar cada intercambio
                plot_pedidos(pedidos, key, f"Intercambio {j} - Iteración {i+1}")
                time.sleep(0.5)

    return pedidos

# Graficar
def plot_pedidos(pedidos, key, title):
    valores = [getattr(p, key) for p in pedidos]
    etiquetas = [f"P{i}" for i in range(len(pedidos))]

    plt.clf()
    plt.bar(etiquetas, valores)

    # Mostrar valores encima de cada barra
    for i, v in enumerate(valores):
        plt.text(i, v + 2, str(v), ha='center')

    plt.title(title)
    plt.xlabel("Pedidos")
    plt.ylabel(key)
    plt.pause(0.5)

# Generar pedidos
def generar_pedidos(n=6):
    return [
        Pedido(
            random.randint(10, 60),
            random.randint(30, 400),
            random.randint(1, 5)
        )
        for _ in range(n)
    ]

# Programa principal
if __name__ == "__main__":

    print("=== SISTEMA DE ORDENAMIENTO DE PEDIDOS ===")

    pedidos = generar_pedidos()

    print("\nPedidos generados:")
    print(pedidos)

    # Selección del criterio
    print("\nSeleccione criterio de ordenamiento:")
    print("1. Tiempo de producción")
    print("2. Tiempo de entrega")
    print("3. Prioridad")

    opcion = input("Opción: ")

    if opcion == "1":
        key = "tiempo_produccion"
    elif opcion == "2":
        key = "tiempo_entrega"
    elif opcion == "3":
        key = "prioridad"
    else:
        print("Opción inválida, se usará producción por defecto")
        key = "tiempo_produccion"

    # Selección del orden
    print("\nSeleccione tipo de orden:")
    print("1. Ascendente")
    print("2. Descendente")

    orden = input("Opción: ")

    reverse = True if orden == "2" else False

    # Activar gráfico interactivo
    plt.ion()

    # Mostrar estado inicial
    plot_pedidos(pedidos, key, "Estado inicial")

    # Ordenar
    ordenados = bubble_sort(pedidos, key, reverse)

    print("\nPedidos ordenados:")
    print(ordenados)

    plt.ioff()
    plt.show()
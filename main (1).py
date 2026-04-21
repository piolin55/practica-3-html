import random
import time
import matplotlib.pyplot as plt

# =========================
# Clase Pedido
# =========================
class Pedido:
    def __init__(self, prod, ent, pri):
        self.tiempo_produccion = prod
        self.tiempo_entrega = ent
        self.prioridad = pri

    def __repr__(self):
        return f"(Prod:{self.tiempo_produccion}, Ent:{self.tiempo_entrega}, Pri:{self.prioridad})"


# =========================
# Generar pedidos
# =========================
def generar_pedidos(n=8):
    return [
        Pedido(
            random.randint(10, 100),
            random.randint(30, 400),
            random.randint(1, 5)
        )
        for _ in range(n)
    ]


# =========================
# Graficar
# =========================
def plot_pedidos(pedidos, key, title, i=None, j=None):
    plt.clf()

    valores = [getattr(p, key) for p in pedidos]
    etiquetas = [f"P{i}" for i in range(len(pedidos))]

    bars = plt.bar(etiquetas, valores)

    # Resaltar comparación
    if i is not None and j is not None:
        bars[i].set_alpha(0.5)
        bars[j].set_alpha(0.5)

    # Mostrar valores
    for idx, v in enumerate(valores):
        plt.text(idx, v + 2, str(v), ha='center')

    plt.title(title)
    plt.xlabel("Pedidos")
    plt.ylabel(key)
    plt.pause(0.3)


# =========================
# Bubble Sort optimizado
# =========================
def bubble_sort(pedidos, key, reverse=False, velocidad=0.3):
    n = len(pedidos)
    comparaciones = 0
    intercambios = 0

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            comparaciones += 1

            plot_pedidos(pedidos, key, f"Comparando {j} y {j+1}", j, j+1)
            time.sleep(velocidad)

            a = getattr(pedidos[j], key)
            b = getattr(pedidos[j + 1], key)

            if (a > b and not reverse) or (a < b and reverse):
                pedidos[j], pedidos[j + 1] = pedidos[j + 1], pedidos[j]
                intercambios += 1
                swapped = True

                plot_pedidos(pedidos, key, f"Intercambio {j} ↔ {j+1}", j, j+1)
                time.sleep(velocidad)

        if not swapped:
            break

    return pedidos, comparaciones, intercambios


# =========================
# Menú
# =========================
def seleccionar_criterio():
    opciones = {
        "1": "tiempo_produccion",
        "2": "tiempo_entrega",
        "3": "prioridad"
    }

    print("\nCriterio:")
    print("1. Producción")
    print("2. Entrega")
    print("3. Prioridad")

    op = input("Opción: ")
    return opciones.get(op, "tiempo_produccion")


def seleccionar_orden():
    print("\nOrden:")
    print("1. Ascendente")
    print("2. Descendente")

    return input("Opción: ") == "2"


def seleccionar_velocidad():
    try:
        v = float(input("\nVelocidad (ej: 0.2 rápido, 1 lento): "))
        return max(0.05, v)
    except:
        return 0.3


# =========================
# Programa principal
# =========================
if __name__ == "__main__":
    print("=== ORDENAMIENTO DE PEDIDOS (MEJORADO) ===")

    pedidos = generar_pedidos()
    print("\nPedidos iniciales:")
    print(pedidos)

    key = seleccionar_criterio()
    reverse = seleccionar_orden()
    velocidad = seleccionar_velocidad()

    plt.ion()
    plot_pedidos(pedidos, key, "Estado inicial")

    pedidos, comp, swaps = bubble_sort(pedidos, key, reverse, velocidad)

    print("\nPedidos ordenados:")
    print(pedidos)

    print(f"\nComparaciones: {comp}")
    print(f"Intercambios: {swaps}")

    plt.ioff()
    plt.show()

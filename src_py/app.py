from benchmarking import Benchmarking
from metodo_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
from datetime import datetime

if __name__ == "__main__":
    print("Funciona")

    bench = Benchmarking()
    metodos = MetodosOrdenamiento()

    tamanios = [5000, 10000, 30000, 50000, 100000]
    resultados = []

    metodoss_dic = {
        "burbuja": metodos.sort_bubble,
        "burbuja mejorado": metodos.sort_burbuja_mejorado_optimizado,
        "seleccion": metodos.sort_seleccion,
        "insercion": metodos.sort_insercion,
        "shell": metodos.sort_shell
    }

    for tam in tamanios:
        arreglo_base = bench.get_subarreglo(tam)

        for nombre, funcion_metodo in metodoss_dic.items():
            arreglo_copia = arreglo_base.copy()
            tiempo_resultado = bench.medir_tiempo(funcion_metodo, arreglo_copia)
            resultados.append((tam, nombre, tiempo_resultado))

    for tam, nombre, tiempo in resultados:
        print(f'Tamaño: {tam} - Metodo: {nombre} - Tiempo: {tiempo:.6f} segundos')

    for nombre in metodoss_dic:
        tiempos = [tiempo for tam, nom, tiempo in resultados if nom == nombre]
        plt.plot(tamanios, tiempos, label=nombre, marker="o")

    plt.title("Comparación de Tiempos de Ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo de ejecucion en segundos")
    plt.legend()
    plt.grid(True)

    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nombre_autor = "ARIEL BADILLO, LEANDRO LOZADO"
    plt.suptitle(f"{nombre_autor} – {ahora}", fontsize=12, fontweight='bold')

    plt.show()

from metodo_ordenamiento import MetodosOrdenamiento
import random
import time

class Benchmarking: 

    def __init__(self):
        print('Benchmarking instanciado')
        self.mO = MetodosOrdenamiento()
        self.arreglo_base = self.build_arreglo(100000)

    def build_arreglo(self, size):
        return [random.randint(0, 100000) for _ in range(size)]

    def get_subarreglo(self, size):
        return self.arreglo_base[:size]

    def medir_tiempo(self, funcion, arreglo):
        inicio = time.perf_counter()
        funcion(arreglo)
        fin = time.perf_counter()
        return fin - inicio
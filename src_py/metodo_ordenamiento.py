class MetodosOrdenamiento:

    def sort_bubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo

    def sort_burbuja_mejorado_optimizado(self, array):  
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n - 1 - i):
                if arreglo[j] > arreglo[j + 1]:       
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j] 
        return arreglo

    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)    
        for i in range(n):
            iM = i
            for j in range(i + 1, n):
                if arreglo[iM] > arreglo[j]:
                    iM = j
            arreglo[i], arreglo[iM] = arreglo[iM], arreglo[i] 
        return arreglo

    def sort_insercion(self, array):
        arreglo = array.copy()
        for i in range(1, len(arreglo)):
            key = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > key:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = key
        return arreglo

    def sort_shell(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo
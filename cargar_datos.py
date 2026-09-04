import numpy as np

def cargar_dlr(ruta):
    datos = np.genfromtxt(ruta, delimiter=',', skip_header=1, usecols=(0, 2, 3))
    return datos

if __name__ == '__main__':
    ruta = r"C:\Users\kevin\OneDrive\Escritorio\Computación Numérica\data\dolar_observado_sii_2022_2025.csv"
    matriz_dlr = cargar_dlr(ruta)
    
    print("Matriz de dólares: ")
    print(matriz_dlr)
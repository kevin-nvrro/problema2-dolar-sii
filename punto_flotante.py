import numpy as np
import matplotlib.pyplot as plt
from errores import redondear_3_cifras
from cargar_datos import cargar_dlr 

if __name__ == '__main__':
    ruta = r"C:\Users\kevin\OneDrive\Escritorio\Computación Numérica\data\dolar_observado_sii_2022_2025.csv"

    print("\n PREGUNTA B1:")
    valor_real = 1000.76
    valor_maquina = redondear_3_cifras(valor_real)
    error_abs = np.abs(valor_real - valor_maquina)
    
    print(f"Valor real del Dólar: {valor_real}")
    print(f"Valor en memoria: {valor_maquina}")
    print(f"Error absoluto: {error_abs}")

    print("\n PREGUNTA B2:")
    matriz = cargar_dlr(ruta) 
    precios = matriz[:, 2]
        
    monto_inicial = np.float32(1000000.0)
    monto_actual = monto_inicial
    historial_deriva = []
        
    print(f"Empezamos con: {monto_inicial} CLP")
        
    for p in precios:
        precio_32 = np.float32(p)
        usd = monto_actual / precio_32
        monto_actual = usd * precio_32
        diferencia_mes = monto_actual - monto_inicial
        historial_deriva.append(diferencia_mes)
            
    diferencia_final = monto_actual - monto_inicial
        
    print(f"Monto al terminar todos los meses: {monto_actual}")
    print(f"Dinero 'fantasma' alterado por la máquina: {diferencia_final} CLP")
    
    # grafico
    plt.figure(figsize=(10, 5))
    plt.plot(historial_deriva, marker='o', color='red')
    plt.title("Deriva de la ida y vuelta en Float32 (Ejercicio B2)")
    plt.xlabel("Meses transcurridos")
    plt.ylabel("Dinero fantasma (CLP)")
    plt.grid(True)
    plt.savefig(r"C:\Users\kevin\OneDrive\Escritorio\Computación Numérica\graficos\5_deriva_B2.png")
    print("grafico guardado")
    
    print("\n PREGUNTA B4:")
    v1_real = 874.67  # Dic 2023
    v2_real = 875.66  # Dic 2022
    
    v1_32 = np.float32(v1_real)
    v2_32 = np.float32(v2_real)
    resta_32 = v1_32 - v2_32
    
    v1_64 = np.float64(v1_real)
    v2_64 = np.float64(v2_real)
    resta_64 = v1_64 - v2_64
    
    resta_manual = -0.99
    
    print(f"Resta manual: {resta_manual}")
    print(f"Resta del PC en 32 bits: {resta_32}")
    print(f"Resta del PC en 64 bits: {resta_64}")
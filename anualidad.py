import numpy as np
from cargar_datos import cargar_dlr
from errores import redondear_2_cifras

if __name__ == '__main__':
    ruta = r"C:\Users\kevin\OneDrive\Escritorio\Computación Numérica\data\dolar_observado_sii_2022_2025.csv"
    matriz = cargar_dlr(ruta)
    
    anios = matriz[:, 0]
    meses = matriz[:, 1]
    precios = matriz[:, 2]
    
    lista_anios = [2022, 2023, 2024, 2025]
    resultados = []
    
    print("RESULTADO A4")
    
    for anio in lista_anios:
        ene = np.where((anios == anio) & (meses == 1))[0][0]
        dic = np.where((anios == anio) & (meses == 12))[0][0]
        
        precio_ene_real = precios[ene]
        precio_dic_real = precios[dic]
        
        precio_ene_aprox = redondear_2_cifras(precio_ene_real)
        precio_dic_aprox = redondear_2_cifras(precio_dic_real)
        
        ea_ene = np.abs(precio_ene_real - precio_ene_aprox)
        ea_dic = np.abs(precio_dic_real - precio_dic_aprox)
    
        delta_p = precio_dic_aprox - precio_ene_aprox
        ea_delta_p = ea_ene + ea_dic
        er_delta_p = (ea_delta_p / np.abs(delta_p)) * 100
        
        resultados.append([er_delta_p, anio, delta_p, ea_delta_p])
    
    resultados.sort()
    
    print("\nAños ordenados por confiabilidad (del más seguro al menos seguro):")
    
    for r in resultados:
        er = r[0]
        anio = r[1]
        delta = r[2]
        ea = r[3]
        
        print(f"Año: {anio}")
        print(f"Variación: {delta} +/- {ea:.2f} CLP")
        print(f"Error Relativo: {er:.2f}%")
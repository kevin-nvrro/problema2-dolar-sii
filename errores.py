import numpy as np
import matplotlib.pyplot as plt
from cargar_datos import cargar_dlr

def redondear_2_cifras(valores):
    magnitud = np.floor(np.log10(np.abs(valores)))
    factor = 10 ** (magnitud - 1)
    
    valores_cortados = np.round(valores / factor) * factor
    return valores_cortados

def calcular_errores(valor_verdadero, valor_aprox):
    ea = np.abs(valor_verdadero - valor_aprox)
    er = (ea / valor_verdadero) * 100
    return ea, er

def ej_compra_venta(monto, p_compra, er_compra, p_venta, er_venta):
    usd = monto / p_compra # comprar dolares
    pesos_final = usd * p_venta # vender el dolar
    
    er_pesos_final = er_compra + er_venta
    ea_pesos_final = pesos_final * (er_pesos_final / 100)
    ganancia = pesos_final - monto
    
    ea_ganancia = ea_pesos_final
    er_ganancia = (ea_ganancia / np.abs(ganancia)) * 100
    
    return ganancia, ea_ganancia, er_ganancia

def redondear_3_cifras(valores):
    magnitud = np.floor(np.log10(np.abs(valores)))
    factor = 10 ** (magnitud - 2)
    valores_cortados = np.round(valores / factor) * factor
    return valores_cortados

if __name__ == '__main__':
    ruta = r"C:\Users\kevin\OneDrive\Escritorio\Computación Numérica\data\dolar_observado_sii_2022_2025.csv"
    matriz = cargar_dlr(ruta)
    
    anios = matriz[:, 0]
    meses = matriz[:, 1]
    precios_reales = matriz[:, 2]

    # aquí guardamos el punto flotante
    precios_aprox = redondear_2_cifras(precios_reales)
    
    # calculamos el error relativo y absoluto
    errores_abs, errores_rel = calcular_errores(precios_reales, precios_aprox)
    
    # aquí esta el mes con mayor error relativo
    mayor_error = np.argmax(errores_rel)
    
    print("\n Resultados A1")
    print(f"El mayor error relativo ocurrió en el mes {int(meses[mayor_error])} del año {int(anios[mayor_error])}")
    print(f"Valor real del SII: {precios_reales[mayor_error]}")
    print(f"Redondeo a 2 cifras: {precios_aprox[mayor_error]}")
    print(f"Error Absoluto: {errores_abs[mayor_error]:.2f} pesos")
    print(f"Error Relativo: {errores_rel[mayor_error]:.4f}%")

    print("\n Resultados A2")
    monto_inicial = 1000000

    # abril 2022 y junio 2022 como ejemplos
    compra = 3
    venta = 5
    
    precio_compra = precios_aprox[compra]
    err_rel_compra = errores_rel[compra]
    
    precio_venta = precios_aprox[venta]
    err_rel_venta = errores_rel[venta]
    
    ganancia, error_abs_ganancia, error_rel_ganancia = ej_compra_venta(monto_inicial, precio_compra, err_rel_compra, precio_venta, err_rel_venta)
    
    print(f"Compra en: Mes {int(meses[compra])} Año {int(anios[compra])} (Precio aprox: {precio_compra})")
    print(f"Venta en: Mes {int(meses[venta])} Año {int(anios[venta])} (Precio aprox: {precio_venta})")
    print(f"Ganancia obtenida: {ganancia:.2f} +/- {error_abs_ganancia:.2f} CLP")
    print(f"Error porcentual de la ganancia: {error_rel_ganancia:.2f}%")

    print("\n RESULTADO A3")
    precio_dic_22_real = 875.66
    precio_dic_23_real = 874.67
    
    # redondeamos a 3 cifras significativas
    precio_dic_22_aprox = redondear_3_cifras(precio_dic_22_real)
    precio_dic_23_aprox = redondear_3_cifras(precio_dic_23_real)
    
    # calculamos los errores absolutos de cada uno
    ea_dic_22 = np.abs(precio_dic_22_real - precio_dic_22_aprox)
    ea_dic_23 = np.abs(precio_dic_23_real - precio_dic_23_aprox)
    
    # calculamos la variación
    delta_p = precio_dic_23_aprox - precio_dic_22_aprox
    
    # propagación en la resta
    ea_delta_p = ea_dic_22 + ea_dic_23
    
    # error relativo porcentual de la variación
    er_delta_p = (ea_delta_p / np.abs(delta_p)) * 100
    
    print(f"Dic 2022 (Aprox): {precio_dic_22_aprox} (Ea: {ea_dic_22:.2f})")
    print(f"Dic 2023 (Aprox): {precio_dic_23_aprox} (Ea: {ea_dic_23:.2f})")
    print(f"Variación (Delta P): {delta_p:.2f} +/- {ea_delta_p:.2f} CLP")
    print(f"Error Relativo del resultado: {er_delta_p:.2f}%")


    print("\n RESULTADO A5")
    pos_min = np.argmin(precios_reales)
    pos_max = np.argmax(precios_reales)
    
    precio_min_real = precios_reales[pos_min]
    anio_min = anios[pos_min]
    mes_min = meses[pos_min]
    
    precio_max_real = precios_reales[pos_max]
    anio_max = anios[pos_max]
    mes_max = meses[pos_max]
    
    precio_compra_aprox = redondear_2_cifras(precio_min_real)
    precio_venta_aprox = redondear_2_cifras(precio_max_real)
    
    ea_compra, er_compra = calcular_errores(precio_min_real, precio_compra_aprox)
    ea_venta, er_venta = calcular_errores(precio_max_real, precio_venta_aprox)
    
    monto = 1000000
    ganancia_a5, ea_ganancia_a5, er_ganancia_a5 = ej_compra_venta(monto, precio_compra_aprox, er_compra, precio_venta_aprox, er_venta)
    
    rentabilidad = (ganancia_a5 / monto) * 100
    ea_rentabilidad = (ea_ganancia_a5 / monto) * 100
    
    print("COMPRA IDEAL:")
    print(f"Mes: {int(mes_min)} del Año: {int(anio_min)}")
    print(f"Precio Real: {precio_min_real} | Precio Máquina: {precio_compra_aprox}\n")
    print("VENTA IDEAL:")
    print("Mes:", int(mes_max), "del Año:", int(anio_max))
    print(f"Precio Real: {precio_max_real} | Precio Máquina: {precio_venta_aprox}\n")
    print("RESULTADO FINANCIERO:")
    print(f"Ganancia: {ganancia_a5} +/- {ea_ganancia_a5:.2f} CLP")
    print(f"Rentabilidad: {rentabilidad} % +/- {ea_rentabilidad:.2f} %")

    print("\nGENERANDO GRÁFICOS")
    # Gráfico 1
    plt.figure(figsize=(10, 5))
    plt.plot(precios_reales, marker='o', linestyle='-')
    plt.title("1. Serie mensual del dólar observado (2022-2025)")
    plt.xlabel("Meses")
    plt.ylabel("Precio (CLP)")
    plt.grid(True)
    plt.savefig(r"C:\Users\kevin\OneDrive\Escritorio\Computación Numérica\graficos\1_serie_mensual.png")
    plt.close()
    
    # Gráfico 2
    variacion_mes = np.diff(precios_reales)
    plt.figure(figsize=(10, 5))
    plt.bar(range(1, len(variacion_mes) + 1), variacion_mes)
    plt.title("2. Variación mes a mes (Delta P)")
    plt.xlabel("Meses")
    plt.ylabel("Variación (CLP)")
    plt.grid(True)
    plt.savefig(r"C:\Users\kevin\OneDrive\Escritorio\Computación Numérica\graficos\2_variacion_mes.png")
    plt.close()
    
    # Gráfico 3
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(errores_rel)), errores_rel, color='orange')
    plt.title("3. Error relativo de representación (2 cifras significativas)")
    plt.xlabel("Meses")
    plt.ylabel("Error Relativo (%)")
    plt.grid(True)
    plt.savefig(r"C:\Users\kevin\OneDrive\Escritorio\Computación Numérica\graficos\3_error_representacion.png")
    plt.close()
    
    # Gráfico 4
    precios_futuros = precios_reales[pos_min:]
    rentabilidades = []
    errores_rent = []
    
    for p_venta in precios_futuros:
        p_v_aprox = redondear_2_cifras(p_venta)
        ea_v = np.abs(p_venta - p_v_aprox)
        er_v = (ea_v / p_venta) * 100
        
        usd_comprados = monto / precio_compra_aprox
        pesos_obtenidos = usd_comprados * p_v_aprox
        ganancia_obtenida = pesos_obtenidos - monto
        rent = (ganancia_obtenida / monto) * 100
        
        er_pesos = er_compra + er_v
        ea_pesos = pesos_obtenidos * (er_pesos / 100)
        ea_rent_final = (ea_pesos / monto) * 100
        
        rentabilidades.append(rent)
        errores_rent.append(ea_rent_final)
        
    plt.figure(figsize=(10, 5))
    plt.errorbar(range(pos_min, pos_min + len(rentabilidades)), rentabilidades, yerr=errores_rent, fmt='-o', color='green', ecolor='red', capsize=5)
    plt.title("4. Rentabilidad de comprar en el mínimo y vender después")
    plt.xlabel("Meses desde el inicio")
    plt.ylabel("Rentabilidad (%)")
    plt.grid(True)
    plt.savefig(r"C:\Users\kevin\OneDrive\Escritorio\Computación Numérica\graficos\4_rentabilidad.png")
    plt.close()
    
    print("Los 4 gráficos se guardaron")


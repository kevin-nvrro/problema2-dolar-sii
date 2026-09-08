# Conclusión Final: Análisis de Error en el Dólar Observado (2022-2025)

**Sección 6**
***A1. Error de representación mes a mes***
Al pasar todos los datos por el código y redondearlos a 2 cifras significativas, el mes que se llevó la peor parte fue Abril de 2022. Su valor real era de 815.12 CLP, pero la máquina lo cortó a 820.0 CLP. Esto nos dejó con un error absoluto de 4.88 pesos y un error relativo del 0.5987%.

A continuación, se muestra lo que salió por consola:
 Resultados A1
El mayor error relativo ocurrió en el mes 4 del año 2022
Valor real del SII: 815.12
Redondeo a 2 cifras: 820.0
Error Absoluto: 4.88 pesos
Error Relativo: 0.5987%

A2. Evaluación entre dos puntos (una compra-venta)
Para probar esto, elegí comprar en Abril de 2022 y vender en Junio de 2022 con un monto inicial de 1.000.000 CLP.
Al hacer la propagación (sumando los errores relativos de la compra y la venta y arrastrándolos a absoluto), nos dio una ganancia de 48.780,49 +/- 9.005,47 CLP.
El error porcentual de esta jugada en específico quedó en un 18.46%.

**1. ¿Cuándo conviene comprar?**
Conviene comprar en Febrero de 2023, cuando el dólar alcanzó su mínimo real de 798.26 CLP. Esta es una decisión matemáticamente segura. Al compararlo con sus meses vecinos (por ejemplo, Marzo de 2023 con 809.50 CLP), la diferencia real es de más de 11 pesos. Como el error de representación de la máquina ronda los 2 a 4 pesos, la diferencia real supera por mucho la incertidumbre. El mínimo es real, no un producto del ruido.

**2. ¿Cuándo conviene vender?**
La mejor opción es vender en Enero de 2025, donde se registró el máximo de 1000.76 CLP. Al igual que en la compra, este máximo es totalmente confiable frente al error. La caída hacia el mes siguiente (Febrero 2025 con 956.62 CLP) es de más de 40 pesos, lo que sobrevive holgadamente a cualquier margen de error introducido por las cifras significativas.

**3. La mejor jugada completa**
La inversión ideal es comprar en Febrero de 2023 y vender en Enero de 2025. 
Al invertir $1.000.000 CLP bajo las restricciones de punto flotante, obtenemos una rentabilidad del 25.0% +/- 0.36%. 
Sí, es una recomendación absolutamente sólida. La ganancia es tan grande que el pequeño error propagado (menos del 0.4%) no alcanza a poner en duda el éxito de la operación.

**4. Los tramos donde NO se puede recomendar**
Es irresponsable tomar decisiones financieras comparando meses casi idénticos, como Diciembre de 2022 (875.66) y Diciembre de 2023 (874.67). En este tramo, la variación calculada con 3 cifras significativas nos dio -1.00 peso, pero con un error propagado de +/- 0.67 pesos (un error relativo del 67%). La diferencia real es tan diminuta que se ahoga dentro de la incertidumbre de la máquina; no podemos asegurar con certeza si el precio realmente subió o bajó.

**5. La lección de método**
Al restar dos números grandes y parecidos ocurre el efecto de "cancelación catastrófica": los dígitos precisos se anulan entre sí y el resultado final queda compuesto únicamente por el error matemático, volviendo cualquier análisis inútil.

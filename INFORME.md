# Informe de Laboratorio: Análisis de Error (Dólar Observado 2022-2025)
**Estudiante:** Kevin Alonso Navarro Silva

## Sección 6: Preguntas del error a contestar

**A1. Error de representación mes a mes**
Al pasar todos los datos por el código y redondearlos a 2 cifras significativas, el mes que se llevó la peor parte fue Abril de 2022. Su valor real era de 815.12 CLP, pero la máquina lo cortó a 820.0 CLP. Esto nos dejó con un error absoluto de 4.88 pesos y un error relativo del 0.5987%.

A continuación, se muestra lo que salió por consola:
```text
 Resultados A1
El mayor error relativo ocurrió en el mes 4 del año 2022
Valor real del SII: 815.12
Redondeo a 2 cifras: 820.0
Error Absoluto: 4.88 pesos
Error Relativo: 0.5987%
```

**A2. Evaluación entre dos puntos (una compra-venta)**
Para probar esto, elegí comprar en Abril de 2022 y vender en Junio de 2022 con un monto inicial de 1.000.000 CLP. Al hacer la propagación (sumando los errores relativos de la compra y la venta y arrastrándolos a absoluto), nos dio una ganancia de 48.780,49 +/- 9.005,47 CLP. El error porcentual de esta jugada en específico quedó en un 18.46%.

A continuación, se muestra lo que salió por consola:
```text
 Resultados A2
Compra en: Mes 4 Año 2022 (Precio aprox: 820.0)
Venta en: Mes 6 Año 2022 (Precio aprox: 860.0)
Ganancia obtenida: 48780.49 +/- 9005.47 CLP
Error porcentual de la ganancia: 18.46%
```

**A3. Cancelación (dos meses casi iguales)**
Aquí restamos Diciembre 2023 (874.67) menos Diciembre 2022 (875.66) pero limitados a 3 cifras significativas (875.0 y 876.0). La variación (Delta) nos dio -1.0 CLP, pero sumando los errores absolutos de los redondeos (0.33 y 0.34) nos quedó un margen de +/- 0.67 CLP. Esto significa un tremendo error relativo del 67.0%. Con ese margen es imposible afirmar con seguridad si el dólar bajó o subió. El error es tan grande en proporción al resultado que se come cualquier conclusión. Podría haber subido o bajado en la realidad, el ruido no deja ver nada.

A continuación, se muestra lo que salió por consola:
```text
 RESULTADO A3
Dic 2022 (Aprox): 876.0 (Ea: 0.34)
Dic 2023 (Aprox): 875.0 (Ea: 0.33)
Variación (Delta P): -1.00 +/- 0.67 CLP
Error Relativo del resultado: 67.00%
```

**A4. Anualidad (variación enero diciembre)**
Al ordenar los años del más seguro al menos seguro nos quedó así: el año 2025 tuvo una variación de -80.0 +/- 4.60 CLP (Error: 5.75%), seguido por el año 2024 con 70.0 +/- 4.31 CLP (Error: 6.16%), luego el año 2022 con 60.0 +/- 6.39 CLP (Error: 10.65%), y finalmente el año 2023 con 40.0 +/- 8.33 CLP (Error: 20.82%). Lo que tienen en común los años poco confiables (especialmente el 2023) es que la diferencia real de precio entre enero y diciembre es más chica. Al restar números tan parecidos, el resultado se achica pero el error absoluto se sigue sumando, lo que hace que el error relativo se dispare por las nubes.

A continuación, se muestra lo que salió por consola:
```text
RESULTADO A4

Años ordenados por confiabilidad (del más seguro al menos seguro):
Año: 2025
Variación: -80.0 +/- 4.60 CLP
Error Relativo: 5.75%
Año: 2024
Variación: 70.0 +/- 4.31 CLP
Error Relativo: 6.16%
Año: 2022
Variación: 60.0 +/- 6.39 CLP
Error Relativo: 10.65%
Año: 2023
Variación: 40.0 +/- 8.33 CLP
Error Relativo: 20.82%
```

**A5. Mejor compra y mejor venta**
El mes más barato de la tabla fue Febrero de 2023 (798.26) y el más caro fue Enero de 2025 (1000.76). Al simular la inversión del millón, la ganancia nos dio 250.000,0 +/- 3.673,95 CLP, lo que es una rentabilidad brutal del 25.0% +/- 0.37%. Acá la conclusión sí sobrevive al error totalmente. La ganancia es tan gigante que la incertidumbre de la máquina (que no llega ni a un 1%) no alcanza a poner en duda la operación. Es una jugada segura.

A continuación, se muestra lo que salió por consola:
```text
 RESULTADO A5
COMPRA IDEAL:
Mes: 2 del Año: 2023
Precio Real: 798.26 | Precio Máquina: 800.0

VENTA IDEAL:
Mes: 1 del Año: 2025
Precio Real: 1000.76 | Precio Máquina: 1000.0

RESULTADO FINANCIERO:
Ganancia: 250000.0 +/- 3673.95 CLP
Rentabilidad: 25.0 % +/- 0.37 %
```

## Sección 7: Preguntas del punto flotante

**B1. Cifras significativas = mantisa corta**
Tomar un precio con solo 2 o 3 cifras significativas es básicamente lo mismo que pasa cuando el computador guarda un número usando pocos bits de memoria. Al tener una "mantisa corta", al PC físicamente no le caben más datos y tiene que mochar el número. Por ejemplo, al guardar el 1000.76 a 3 cifras, la máquina solo retiene el 1000.0, perdiéndose esos 0.76 pesos en el limbo y generando un error de entrada.

A continuación, se muestra lo que salió por consola:
```text
Valor real del Dólar: 1000.76
Valor en memoria: 1000.0
Error absoluto: 0.7599999999999909
```

**B2. La ida y vuelta que no vuelve**
Si compras y vendes dólares al mismo precio todos los meses empezando con 1.000.000 CLP, la matemática pura dice que deberías terminar con tu millón exacto. Sin embargo, al correr nuestro ciclo for, terminamos con 1000000.0000000003 CLP. Se nos generó un dinero fantasma de 3.49e-10 CLP (0.000000000349 pesos inventados). No es un error gigante gracias a que Python usa 64 bits y aguanta hartos decimales, pero el gráfico de deriva confirma el punto: al dividir y multiplicar tantas veces seguidas, la máquina se marea redondeando en binario, la basura residual se va acumulando y nunca nos devuelve la misma plata con la que empezamos.

A continuación, se muestra lo que salió por consola:
```text
 PREGUNTA B2:
Empezamos con: 1000000.0 CLP
Monto al terminar todos los meses: 1000000.0000000003
Dinero 'fantasma' alterado por la máquina: 3.4924596548080444e-10 CLP
```

**B4. Cancelación en la máquina**
Al restar 874.67 menos 875.66 directo en código los resultados son reveladores. La resta manual da -0.99, pero en 32 bits arroja -0.989990234375 y en 64 bits entrega -0.9900000000000091. En float32 a duras penas sobreviven 2 cifras antes de empezar a escupir decimales falsos a lo loco. En float64 resiste harto más, pero al final igual la máquina inventa un 91 de la nada. Esto se conecta directo con lo que nos pasó en la cancelación del A3: al restar dos números grandes y casi iguales, los dígitos precisos se mueren entre sí, y el resultado final que nos entrega la pantalla queda hecho casi al 100% de pura basura de memoria.

A continuación, se muestra lo que salió por consola:
```text
 PREGUNTA B4:
Resta manual: -0.99
Resta del PC en 32 bits: -0.989990234375
Resta del PC en 64 bits: -0.9900000000000091
```

## Conclusión Final

**1. ¿Cuándo conviene comprar?**
Conviene comprar en Febrero de 2023, cuando el dólar alcanzó su mínimo real de 798.26 CLP. Esta es una decisión matemáticamente segura. Al compararlo con sus meses vecinos (por ejemplo, Marzo de 2023 con 809.50 CLP), la diferencia real es de más de 11 pesos. Como el error de representación de la máquina ronda los 2 a 4 pesos, la diferencia real supera por mucho la incertidumbre. El mínimo es real, no un producto del ruido.

**2. ¿Cuándo conviene vender?**
La mejor opción es vender en Enero de 2025, donde se registró el máximo de 1000.76 CLP. Al igual que en la compra, este máximo es totalmente confiable frente al error. La caída hacia el mes siguiente (Febrero 2025 con 956.62 CLP) es de más de 40 pesos, lo que sobrevive holgadamente a cualquier margen de error introducido por las cifras significativas.

**3. La mejor jugada completa**
La inversión ideal es comprar en Febrero de 2023 y vender en Enero de 2025. Al invertir $1.000.000 CLP bajo las restricciones de punto flotante, obtenemos una rentabilidad del 25.0% +/- 0.36%. Sí, es una recomendación absolutamente sólida. La ganancia es tan grande que el pequeño error propagado (menos del 0.4%) no alcanza a poner en duda el éxito de la operación.

**4. Los tramos donde NO se puede recomendar**
Es irresponsable tomar decisiones financieras comparando meses casi idénticos, como Diciembre de 2022 (875.66) y Diciembre de 2023 (874.67). En este tramo, la variación calculada con 3 cifras significativas nos dio -1.00 peso, pero con un error propagado de +/- 0.67 pesos (un error relativo del 67%). La diferencia real es tan diminuta que se ahoga dentro de la incertidumbre de la máquina; no podemos asegurar con certeza si el precio realmente subió o bajó.

**5. La lección de método**
Al restar dos números grandes y parecidos ocurre el efecto de "cancelación catastrófica": los dígitos precisos se anulan entre sí y el resultado final queda compuesto únicamente por el error matemático, volviendo cualquier análisis inútil.

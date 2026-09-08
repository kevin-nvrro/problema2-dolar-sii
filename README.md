# Laboratorio 1: Análisis de Error (Dólar Observado)

Este repositorio contiene la evaluación del laboratorio N°1 donde se hace un análisis del error (cifras significativas, punto flotante, error absoluto, relativo y propagación) utilizando el dólar observado del SII (2022-2025).

## Estructura del Repositorio

```text
problema2-dolar-sii/
├── README.md                <- descripción + resultados
├── INFORME.md               <- respuestas a las preguntas y conclusiones
├── requirements.txt         <- numpy, matplotlib
├── data/
│   └── dolar_observado_sii_2022_2025.csv  <- datos
├── SIC/
│   ├── cargar_datos.py      <- cargamos los datos del CSV
│   ├── errores.py           <- error absoluto, relativo y propagado entre puntos
│   ├── anualidad.py         <- variación y error año a año
│   └── punto_flotante.py    <- float32/float64, ida y vuelta, cancelación
└── graficos/                <- imágenes PNG generadas
│   ├── 1_serie_mensual.png
│   ├── 2_variacion_mes.png
│   ├── 3_error_representacion.png
│   └── 4_rentabilidad.png
│   └── 5_deriva_B2.png


# Laboratorio 1: Análisis de Error (Dólar Observado)

Este repositorio contiene la evaluación sobre cancelación catastrófica y propagación del error en operaciones de punto flotante utilizando el dólar observado del SII (2022-2025).

## Estructura del Repositorio

```text
problema2-dolar-sii/
├── README.md                <- descripción + resultados
├── INFORME.md               <- documento de entrega (ver sección 9)
├── requirements.txt         <- numpy, matplotlib
├── data/
│   └── dolar_observado_sii_2022_2025.csv
├── SIC/
│   ├── cargar_datos.py      <- carga el CSV con numpy (np.genfromtxt)
│   ├── errores.py           <- error absoluto, relativo y propagado entre puntos
│   ├── anualidad.py         <- variación y error año a año
│   └── punto_flotante.py    <- float32/float64, ida y vuelta, cancelación
└── graficos/                <- imágenes PNG generadas

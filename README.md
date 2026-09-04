# Laboratorio 1: Análisis de Error (Dólar Observado)
Este repositorio contiene la evaluación sobre cancelación catastrófica y propagación del error en operaciones de punto flotante.

## Estructura del Repositorio
* `data/`: Contiene el archivo CSV con los precios del dólar del SII.
* `graficos/`: Carpeta con los 5 gráficos generados por el código.
* `cargar_datos.py`: Script base que limpia y carga la matriz numérica.
* `errores.py`: Calcula los errores absolutos/relativos y encuentra la mejor jugada.
* `anualidad.py`: Evalúa la variación anual aislando el efecto cancelación.
* `punto_flotante.py`: Demuestra la pérdida de memoria en 32 bits y la deriva matemática.
* `INFORME.md`: Contiene las respuestas formales a las preguntas de la sección 9.

## Cómo ejecutar el código
Cada script fue construido de forma modular y cuenta con su propio bloque `if __name__ == '__main__':`. Para revisar los resultados, simplemente ejecuta cada archivo `.py` de forma individual en la terminal.

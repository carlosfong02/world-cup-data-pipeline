# ⚽ FIFA World Cup ETL Pipeline (1930-2022)

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Pandas](https://img.shields.io/badge/Library-Pandas-150458) ![SQLite](https://img.shields.io/badge/Database-SQLite-003B57) ![Status](https://img.shields.io/badge/Status-Completed-green)

### 📋 Descripción del Proyecto
Este proyecto es un **Pipeline de Ingeniería de Datos (ETL)** diseñado para procesar el histórico completo de partidos de la Copa Mundial de la FIFA (1930-2022).

El objetivo principal fue tomar un dataset crudo (`CSV`), limpiar inconsistencias históricas, normalizar la estructura de datos y cargarlo en una **Base de Datos SQL (SQLite)** para permitir análisis de negocio complejos que no serían posibles en una hoja de cálculo tradicional.

### ⚙️ Arquitectura del Pipeline

El proceso sigue la metodología **ETL (Extract, Transform, Load)**:

1.  **Extracción (Extract):** * Ingesta de datos históricos desde archivo plano (`FIFA-World-Cup-1930-2022`).
    * Detección automática de encoding (`latin1`) y separadores.
2.  **Transformación (Transform):**
    * **Data Quality:** Detección de nulos y corrección de formatos de fecha.
    * **Estandarización:** Conversión de nombres de columnas a `snake_case`.
    * **Enriquecimiento:** Traducción de variables clave al español (ej. `home_team` -> `equipo_local`) para facilitar el consumo de datos.
    * **Limpieza:** Eliminación de espacios en blanco (`trim`) en campos de texto.
3.  **Carga (Load):**
    * Creación automatizada de base de datos **SQLite**.
    * Persistencia de datos en la tabla `fact_partidos`.

### 📂 Estructura del Proyecto

```text
fifa-etl-pipeline/
│
├── FIFA World Cup 1930-2022.csv  # Dataset Original (Fuente de Datos)
├── etl_pipeline.py               # Script Principal (ETL Process)
├── analisis.ipynb                # Jupyter Notebook (Análisis SQL)
├── fifa_world_cup.db             # Base de Datos Generada (Output)
└── README.md                     # Documentación del Proyecto

### 🛠️ Tecnologías Utilizadas
* **Lenguaje:** `Python 3.11`
* **Librerías:** `Pandas`, `NumPy`
* **Base de Datos:** `SQLite3`
* **Entorno de Desarrollo:** `Visual Studio Code`
* **Control de Versiones:** `Git` & `GitHub`
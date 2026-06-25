# Actividad 1 - MLOps OpenRate

## Integrantes

1. Marua Beltran
2. Martha Forero

## Objetivo

Desarrollar un proyecto MLOps para la predicción de apertura de campañas utilizando un conjunto de datos sintético, aplicando buenas prácticas de control de versiones, gestión de datos y seguimiento de experimentos.

## Tecnologías utilizadas

* Python 3.13
* Poetry
* Git y GitHub
* DVC
* MLflow
* Scikit-Learn
* Pandas

## Estructura del proyecto

* data/: datos utilizados en el proyecto.
* src/: scripts de generación de datos y entrenamiento.
* models/: modelos generados.
* outputs/: resultados y artefactos.
* notebooks/: análisis exploratorios.

## Ejecución

Generar datos:

python src/make_dataset.py

Entrenar modelo:

python src/train_model.py

## Seguimiento de experimentos

Los experimentos fueron registrados utilizando MLflow.

## Control de datos

Los datos fueron versionados mediante DVC.


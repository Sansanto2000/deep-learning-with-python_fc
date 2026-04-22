# Libro DLWP

Este repositorio contiene la implementación práctica de los códigos y actividades del libro *"Deep Learning with Python"* de François Chollet.

## Estructura del repositorio

Los cuadernos siguen una nomenclatura estricta para facilitar la navegación siguiendo el hilo del libro:

- Formato: `x.x.x.nombre.ipynb`
- Convención: `x.x.x` indica el número de capítulo, sección y subsección. El `nombre` es un identificador descriptivo del contenido.

Cada notebook incluye explicaciones teóricas intercaladas con los bloques de código, sirviendo como una guía de estudio completa que conecta la teoría con la implementación en **Keras/TensorFlow**.

## Datasets

Los datasets necesarios para cada módulo ya están descargados en el propio repositorio, en formato `.zip`.

## Configuración del Entorno

Para ejecutar los notebooks con soporte de aceleración por hardware (GPU), asegúrate de tener configurado tu entorno virtual:

```
# Activar el entorno virtual
source tf-gpu/bin/activate
```
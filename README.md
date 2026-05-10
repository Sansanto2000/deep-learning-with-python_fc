# Libro DLWP

Este repositorio contiene la implementación práctica de los códigos y actividades del libro *"Deep Learning with Python"* de François Chollet.

## Estructura del repositorio

Los cuadernos siguen una nomenclatura estricta para facilitar la navegación siguiendo el hilo del libro:

- Formato: `x.x.x.nombre.ipynb`
- Convención: `x.x.x` indica el número de capítulo, sección y subsección. El `nombre` es un identificador descriptivo del contenido.

Cada notebook incluye explicaciones teóricas intercaladas con los bloques de código, sirviendo como una guía de estudio completa que conecta la teoría con la implementación en **Keras/TensorFlow**.

## Datasets

Por cuestiones de límite de tamaño de archivo en GitHub los las carpetas `datasets/` y `embeddings/` son inicializadas sin contenido. No obstante todo lo necesario para descargar sus respectivos archivos se muestra en los bloques de código que lo usan.

## Configuración del Entorno

Para ejecutar el codigo se usa *Docker*. 

```
# Levantar el contenedor
docker compose up

# Comprobar ejecucion
docker compose ps

# Levantar
docker compose exec tensorflow bash
```

# Ejecutar `ipynb` desde VSC

Para ejecutar: 
1. Instalar la extension *Dev Containers*.
2. Presionar `Ctrl+Shift+P`.
3. Seleccionar *"Attach to Running Container"*.

Se abrira un nuevo contenedor donde se puede ejecutar los archivos.
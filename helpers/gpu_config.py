import tensorflow as tf

# Funcion a ejecutar cuando la GPU esta reservando toda la memoria innecesariamente
def configure_gpu_memory_growth():
    gpus = tf.config.list_physical_devices("GPU")
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
    return gpus
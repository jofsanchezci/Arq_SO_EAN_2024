import numpy as np
import matplotlib.pyplot as plt

# Parameter
frecuencia = 5  # Frequency in Hz
amplitud = 1  # Signal amplitude
duracion = 1  # Duration in seconds
frecuencia_muestreo = 20  # Sampling frequency in Hz

# Discrete time
n = np.arange(0, duracion, 1 / frecuencia_muestreo)

# Discrete sinusoidal signal
senal_senoidal_discreta = amplitud * np.sin(2 * np.pi * frecuencia * n)

# Discrete Square
senal_cuadrada_discreta = amplitud * np.sign(np.sin(2 * np.pi * frecuencia * n))

# Discreta Triangular
senal_triangular_discreta = 2 * amplitud / np.pi * np.arcsin(np.sin(2 * np.pi * frecuencia * n))

# Signal graph
plt.figure(figsize=(10, 8))


plt.subplot(3, 1, 1)
plt.stem(n, senal_senoidal_discreta, basefmt=" ", use_line_collection=True)
plt.title('Discrete sinusoidal ')
plt.xlabel('Samples')
plt.ylabel('Amplitude')


plt.subplot(3, 1, 2)
plt.stem(n, senal_cuadrada_discreta, basefmt=" ", use_line_collection=True)
plt.title('Discrete Square')
plt.xlabel('Samples')
plt.ylabel('Amplitude')


plt.subplot(3, 1, 3)
plt.stem(n, senal_triangular_discreta, basefmt=" ", use_line_collection=True)
plt.title('Discrete Triangular')
plt.xlabel('Samples')
plt.ylabel('Amplitude')


plt.tight_layout()
plt.show()

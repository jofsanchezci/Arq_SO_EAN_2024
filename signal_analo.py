import numpy as np
import matplotlib.pyplot as plt

# parameters
frecuencia = 5  # Frequency in Hz
amplitud = 1  # Signal amplitude
duracion = 1  # Duration in seconds
frecuencia_muestreo = 1000  # Sampling frequency in Hz

# Time
t = np.linspace(0, duracion, int(frecuencia_muestreo * duracion), endpoint=False)

# Sinusoidal signal
senal_senoidal = amplitud * np.sin(2 * np.pi * frecuencia * t)

# Square signal
senal_cuadrada = amplitud * np.sign(np.sin(2 * np.pi * frecuencia * t))

# Triangular signal
senal_triangular = 2 * amplitud / np.pi * np.arcsin(np.sin(2 * np.pi * frecuencia * t))

# Signal graph
plt.figure(figsize=(10, 8))


plt.subplot(3, 1, 1)
plt.plot(t, senal_senoidal)
plt.title('Sinusoidal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')


plt.subplot(3, 1, 2)
plt.plot(t, senal_cuadrada)
plt.title('Square')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')


plt.subplot(3, 1, 3)
plt.plot(t, senal_triangular)
plt.title('Triangular ')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Show
plt.tight_layout()
plt.show()

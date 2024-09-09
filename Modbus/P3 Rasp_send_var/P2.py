import serial
import time

# Configurar el puerto serial
ser = serial.Serial(
    port='/dev/serial0',  # Cambia a /dev/ttyUSB0 si usas un adaptador USB-RS-485
    baudrate=38400,  # Configuración de la velocidad de transmisión
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

# Simular el estado del botón (0 = no pulsado, 1 = pulsado)
# Aquí podrías leer desde un GPIO en una aplicación real
button1 = 0

# Función para transmitir el estado del botón por RS-485
try:
    print("Transmisión RS-485 iniciada. Presiona Ctrl+C para finalizar.")
    while True:
        # Cambia el estado del botón según tu lógica
        # Aquí, sólo alternamos el valor de button1 como ejemplo
        button1 = 1 if button1 == 0 else 0

        # Transmitir el estado del botón por RS-485
        ser.write(str(button1).encode())  # Convertir la cadena a bytes

        print(f"Estado del botón enviado: {button1}")

        # Pausa entre transmisiones para simular intervalos de tiempo
        time.sleep(1)

except KeyboardInterrupt:
    print("Transmisión interrumpida por el usuario.")
finally:
    ser.close()  # Cerrar el puerto serial al finalizar

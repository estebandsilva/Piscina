import serial

# Configurar el puerto serial
ser = serial.Serial(
    port='/dev/serial0',  # Cambia a /dev/ttyUSB0 si usas un adaptador USB-RS-485
    baudrate=38400,  # Configuración de la velocidad de transmisión
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

# Función para transmitir datos desde la terminal a través de RS-485
try:
    print("Transmisión RS-485 iniciada. Escribe algo para enviar:")
    while True:
        # Leer datos desde la terminal
        input_data = input(">> ")  # Leer texto desde la terminal

        if input_data.lower() == 'exit':
            print("Finalizando la transmisión.")
            break

        # Transmitir datos por RS-485
        ser.write(input_data.encode())  # Convertir la cadena a bytes

        print(f"Datos enviados: {input_data}")
except KeyboardInterrupt:
    print("Transmisión interrumpida por el usuario.")
finally:
    ser.close()  # Cerrar el puerto serial al finalizar

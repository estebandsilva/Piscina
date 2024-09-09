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

# Simulación de la variable 'button1'
button1 = False  # Cambia a True o False según el estado


def enviar_estado_button1(button_state):
    estado = 'HIGH' if button_state else 'LOW'
    ser.write(estado.encode())  # Convertir la cadena a bytes y enviarla
    print(f"Estado de button1 enviado: {estado}")


# Función para transmitir el estado de button1 a través de RS-485
try:
    print("Transmisión RS-485 iniciada.")
    while True:
        input_data = input("Escribe 'enviar' para transmitir el estado de button1 o 'exit' para salir: ")

        if input_data.lower() == 'exit':
            print("Finalizando la transmisión.")
            break

        if input_data.lower() == 'enviar':
            enviar_estado_button1(button1)

except KeyboardInterrupt:
    print("Transmisión interrumpida por el usuario.")
finally:
    ser.close()  # Cerrar el puerto serial al finalizar

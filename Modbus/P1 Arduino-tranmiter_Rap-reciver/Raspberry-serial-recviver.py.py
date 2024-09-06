import serial

# Configurar la conexión serial
ser = serial.Serial(
    port='/dev/serial0',  # Puerto serial, puede variar dependiendo del adaptador o la conexión
    baudrate=38400,       # Velocidad de transmisión (debe coincidir con la configuración del transmisor)
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1             # Tiempo de espera para la lectura
)

# Loop para leer los datos recibidos por RS-485
try:
    while True:
        if ser.in_waiting > 0:  # Si hay datos disponibles
            received_data = ser.read()  # Leer un byte
            # Mostrar el valor en hexadecimal y decimal
            print(f"HEX: {received_data.hex()}, DEC: {int.from_bytes(received_data, byteorder='big')}")
except KeyboardInterrupt:
    print("Finalizando la lectura de RS-485")
    ser.close()  # Cerrar el puerto serial al finalizar

from pymodbus.client import ModbusSerialClient  # Import correcto en pymodbus 2.5+
import time

# Configuración Modbus RTU
client = ModbusSerialClient(
    port='/dev/serial0',  # Cambia según tu configuración (puede ser /dev/ttyUSB0 si usas un adaptador USB)
    baudrate=38400,       # Debe coincidir con la configuración del Arduino
    parity='E',           # 'E' para paridad par (even), 'N' para sin paridad (none)
    stopbits=1,           # 1 bit de parada
    bytesize=8,           # Tamaño de byte de 8 bits
    timeout=1             # Tiempo de espera
)

# Intentar conectar con el esclavo
if client.connect():
    print("Conexión establecida con el esclavo.")
    try:
        while True:
            # Leer entrada del terminal (esperar hasta que el usuario escriba "high" o "low")
            user_input = input("Escribe 'high' para 1 o 'low' para 0: ").strip().lower()

            # Convertir la entrada a un valor para enviar
            if user_input == 'high':
                button_state = 1
            elif user_input == 'low':
                button_state = 0
            else:
                print("Entrada inválida. Escribe 'high' o 'low'.")
                continue

            # Dirección del esclavo Modbus (debe coincidir con el ID del Arduino)
            slave_id = 31

            # Escribir el valor en el registro de retención 0 del esclavo
            response = client.write_register(0, button_state, slave=slave_id)  # Cambiar 'unit' a 'slave'

            # Verificar si la respuesta fue exitosa
            if response.isError():
                print(f"Error al escribir en el esclavo {slave_id}")
            else:
                print(f"Valor {button_state} enviado al esclavo {slave_id} en el holding register 0.")

    except KeyboardInterrupt:
        print("Programa detenido por el usuario.")
    finally:
        client.close()
else:
    print("No se pudo establecer la conexión con el esclavo.")

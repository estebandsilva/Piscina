from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
##
# Configurar la comunicación Modbus RTU
client = ModbusClient(
    method='rtu',
    port='/dev/serial0',  # Cambia esto según tu configuración (puede ser /dev/ttyUSB0 si usas un adaptador USB)
    baudrate=38400,
    parity='E',
    stopbits=1,
    bytesize=8,
    timeout=1
)

# Intentar conectar con el esclavo
connection = client.connect()

if connection:
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

            # Dirección del esclavo Modbus
            slave_id = 31  # Asegúrate de que coincide con la dirección del esclavo en el Arduino

            # Escribir el valor en el holding register 0 del esclavo
            client.write_register(0, button_state, unit=slave_id)

            print(f"Valor {button_state} enviado al esclavo {slave_id} en el holding register 0.")

    except KeyboardInterrupt:
        print("Programa detenido por el usuario.")
    finally:
        client.close()
else:
    print("No se pudo establecer la conexión con el esclavo.")

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time

# Configurar la comunicación Modbus RTU
client = ModbusClient(
    method='rtu',
    port='/dev/serial0',  # Cambia según tu configuración
    baudrate=38400,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=1
)

# Intentar conectar con el esclavo
connection = client.connect()

if connection:
    print("Conexión establecida con esclavos.")
    try:
        while True:
            # Enviar una solicitud de lectura al esclavo 1 (por ejemplo, dirección 1)
            # Esto es un ejemplo de lectura de registros de entrada (input register)
            slave_id = 1  # Dirección del esclavo Modbus
            response = client.read_input_registers(0, 1, unit=slave_id)

            if not response.isError():
                print(f"Respuesta del esclavo {slave_id}: {response.registers}")
            else:
                print(f"Error en la comunicación con el esclavo {slave_id}")

            # Pausa antes de enviar la siguiente solicitud
            time.sleep(2)

    except KeyboardInterrupt:
        print("Detenido por el usuario.")
    finally:
        client.close()
else:
    print("No se pudo establecer la conexión con el esclavo.")

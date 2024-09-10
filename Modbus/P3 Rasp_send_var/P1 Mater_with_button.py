import serial
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.exceptions import ModbusIOException

# Configurar el cliente Modbus RTU sobre el puerto serial
modbus_client = ModbusClient(
    method='rtu',
    port='/dev/serial0',  # Cambia a /dev/ttyUSB0 si usas un adaptador USB-RS-485
    baudrate=38400,
    parity='N',  # Ninguna paridad
    stopbits=1,
    bytesize=8,
    timeout=1
)

# Conectar al dispositivo esclavo (slave)
connection = modbus_client.connect()
if connection:
    print("Conexión Modbus establecida.")
else:
    print("Error al conectar al dispositivo esclavo.")
    exit()

try:
    while True:
        input_data = input("Escribe el número del registro Modbus a leer (o 'exit' para salir): ")

        if input_data.lower() == 'exit':
            print("Finalizando la transmisión.")
            break

        # Intentar convertir el input a un número de registro
        try:
            register_address = int(input_data)
        except ValueError:
            print("Por favor, ingresa un número de registro válido.")
            continue

        # Leer el valor del registro Modbus
        try:
            result = modbus_client.read_holding_registers(register_address, 1, unit=1)
            if not isinstance(result, ModbusIOException):
                print(f"Valor del registro {register_address}: {result.registers[0]}")
            else:
                print(f"Error al leer el registro {register_address}")
        except Exception as e:
            print(f"Error durante la lectura: {e}")

except KeyboardInterrupt:
    print("Transmisión interrumpida por el usuario.")
finally:
    modbus_client.close()
    print("Conexión cerrada.")

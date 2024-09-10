#include <ModbusRTUSlave.h>

// Crear espacio para los registros de almacenamiento
uint16_t holdingRegisters[1];  // Un solo registro, índice 0

// Configurar el esclavo Modbus en la dirección 31
#if defined HAVE_RS485_HARD
#include <RS485.h>
ModbusRTUSlave modbus(RS485, 31);
#elif defined HAVE_RS232_HARD
#include <RS232.h>
ModbusRTUSlave modbus(RS232, 31);
#else
ModbusRTUSlave modbus(Serial1, 31);
#endif

const uint32_t baudrate = 38400UL;

void setup() {
  Serial.begin(9600UL);  // Iniciar la comunicación serial para depuración

  // Configurar el puerto RS-485
#if defined HAVE_RS485_HARD
  RS485.begin(baudrate, HALFDUPLEX, SERIAL_8N1);
#elif defined HAVE_RS232_HARD
  RS232.begin(baudrate, SERIAL_8E1);
#else
  Serial1.begin(baudrate, SERIAL_8E1);
#endif

  // Iniciar el esclavo ModbusRTU
  modbus.begin(baudrate);

  // Configurar los registros de retención (holding registers)
  modbus.setHoldingRegisters(holdingRegisters, 1);  // Un registro
}

void loop() {
  // Procesar las solicitudes Modbus
  modbus.update();

  // Leer el valor del holding register 0
  uint16_t value = holdingRegisters[0];  // Leer el valor escrito por el maestro

  // Mostrar el valor en el monitor serial
  Serial.print("Valor del registro 0: ");
  Serial.println(value);

  // Realizar una acción con base en el valor
  if (value == 1) {
    Serial.println("Acción: LED encendido.");
  } else {
    Serial.println("Acción: LED apagado.");
  }

  delay(1000);  // Pausa de 1 segundo
}


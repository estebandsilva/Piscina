// Include Industrial Shields libraries
#include <RS485.h>
//RECIVER

//// IMPORTANT: check switches configuration

////////////////////////////////////////////////////////////////////////////////////////////////////
void setup() {
  // Begin serial port
  Serial.begin(9600);

  // Begin RS485 port
  RS485.begin(38400);
}
////////////////////////////////////////////////////////////////////////////////////////////////////
void loop() {
  // Print received byte when available
  if (RS485.available()) {
    byte rx = RS485.read();

    // Hexadecimal representation
    Serial.print("HEX: ");
    Serial.print(rx, HEX);

    // Decimal representation
    Serial.print(", DEC: ");
    Serial.println(rx, DEC);
  }
}

// Include Industrial Shields libraries
#include <RS485.h>
//RECIVER

//// IMPORTANT: check switches configuration(plc)

////////////////////////////////////////////////////////////////////////////////////////////////////
void setup() {
  // Begin serial port
  Serial.begin(9600);
  delay(1000);

  // Begin RS485 port
  RS485.begin(38400);
  delay(1000);
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

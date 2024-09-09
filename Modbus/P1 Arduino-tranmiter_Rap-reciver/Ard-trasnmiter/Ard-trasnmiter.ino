// Include Industrial Shields libraries
#include <RS485.h>
//TRANSMITER
//// IMPORTANT: check switches configuration(plc)

////////////////////////////////////////////////////////////////////////////////////////////////////
void setup() {
  // Begin serial port
  Serial.begin(9600);

  // Begin RS485 port
  RS485.begin(38400);
}

////////////////////////////////////////////////////////////////////////////////////////////////////
void loop() {
  // Wait bytes in the serial port
  if (Serial.available()) {
    byte tx = Serial.read();

    // Echo the byte to the serial port again
    Serial.write(tx);

    // And send it to the RS-485 port
    RS485.write(tx);
  }
}



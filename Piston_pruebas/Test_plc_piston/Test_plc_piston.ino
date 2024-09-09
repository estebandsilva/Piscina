volatile long encoder1Count = 0;  // Contador de pulsos del encoder 1
volatile long encoder2Count = 0;  // Contador de pulsos del encoder 2
volatile byte lastEncoderStateA1 = LOW;
volatile byte lastEncoderStateB1 = LOW;
volatile byte lastEncoderStateA2 = LOW;
volatile byte lastEncoderStateB2 = LOW;

void setup() {
  Serial.begin(9600);  // Initialize serial communication at 9600 bits per second
  delay(2000);
  Serial.println("Ready to receive commands");
  Serial.println("1. PISTON OUT");
  Serial.println("2. PISTON IN");
  Serial.println("3.  STOP");

  digitalWrite(R1,LOW);
  digitalWrite(R2,LOW);
  digitalWrite(R3,LOW);
  digitalWrite(R4,LOW);


  // Configurar Timer1 para que interrumpa cada 5ms
  noInterrupts();           // Deshabilitar interrupciones globales
  TCCR1A = 0;               // Limpiar registro de control A
  TCCR1B = 0;               // Limpiar registro de control B
  TCNT1 = 0;                // Inicializar el contador del Timer1

  // Configurar el comparador de salida para que interrumpa a intervalos regulares
  OCR1A = 1249;             // Comparar con este valor para 5ms a 16 MHz con prescaler 64
  TCCR1B |= (1 << WGM12);   // Modo CTC (Clear Timer on Compare Match)
  TCCR1B |= (1 << CS11) | (1 << CS10); // Prescaler 64
  TIMSK1 |= (1 << OCIE1A);  // Habilitar interrupción por comparación con OCR1A

  interrupts();             // Habilitar interrupciones globales

  Serial.begin(9600);
}

void loop() {
  // Mostrar las cuentas de vueltas cada cierto tiempo
  noInterrupts();  // Deshabilitar interrupciones mientras se leen las variables
  long count1 = encoder1Count;
  long count2 = encoder2Count;
  interrupts();    // Habilitar interrupciones nuevamente

  Serial.print("Encoder 1 Count: ");
  Serial.println(count1);

  Serial.print("Encoder 2 Count: ");
  Serial.println(count2);

  delay(100);  // Muestra el resultado cada 100ms
}

ISR(TIMER1_COMPA_vect) {
  // Esta función es llamada cada vez que el Timer1 alcanza el valor de OCR1A (5ms en este caso)
  
  // Leer el estado actual del encoder 1
  byte currentStateA1 = digitalRead(I0_0);
  byte currentStateB1 = digitalRead(I0_2);

  if (currentStateA1 != lastEncoderStateA1 || currentStateB1 != lastEncoderStateB1) {
    if (currentStateA1 != lastEncoderStateA1) {
      if (currentStateA1 == currentStateB1) {
        encoder1Count++;  // Incrementar si A y B son iguales
      } else {
        encoder1Count--;  // Decrementar si A y B son diferentes
      }
    }
    lastEncoderStateA1 = currentStateA1;
    lastEncoderStateB1 = currentStateB1;
  }

  // Leer el estado actual del encoder 2
  byte currentStateA2 = digitalRead(I0_4);
  byte currentStateB2 = digitalRead(I0_5);

  if (currentStateA2 != lastEncoderStateA2 || currentStateB2 != lastEncoderStateB2) {
    if (currentStateA2 != lastEncoderStateA2) {
      if (currentStateA2 == currentStateB2) {
        encoder2Count++;  // Incrementar si A y B son iguales
      } else {
        encoder2Count--;  // Decrementar si A y B son diferentes
      }
    }
    lastEncoderStateA2 = currentStateA2;
    lastEncoderStateB2 = currentStateB2;
  }
  // Reles activation
  if (Serial.available() > 0) {   // Check if data is available to read
    String command = Serial.readStringUntil('\n');  // Read the incoming command as a string
   

    //Finales de carrera FC1S HIGH (Final de carrera piston1 Superior/out activado)
    // Check the command and call the corresponding function
    if (command == "1") {
      Serial.println("PISTON SALIENDO ...");   

      digitalWrite(R1,HIGH);
      digitalWrite(R2,LOW);

    } else if (command == "2") {
      Serial.println("PISTON ENTRANDO ...");

      digitalWrite(R1,LOW);
      digitalWrite(R2,HIGH);


    } else if (command == "3") {

      Serial.println("PARADA");
      digitalWrite(R1,LOW);
      digitalWrite(R2,LOW);
      digitalWrite(R3,LOW);
      digitalWrite(R4,LOW);

    } else if (command == "4") {
      digitalWrite(R2,LOW);
      Serial.println("Final de carrera del P1 inferior");
      Serial.println("Desactivado");

    } else {
      Serial.println("Unknown command");
    }
  
}
}

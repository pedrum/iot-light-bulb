int led = 13;
char incoming = ' ';
// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  if (Serial.available() > 0) {
      incoming = Serial.read();
      //Serial.print("Rx: ");
      //Serial.println(incoming);
      
      if (incoming == '0') {
        digitalWrite(led, LOW);
      } else if (incoming == '1') {
        digitalWrite(led, HIGH);
      } else if (incoming =='q') {
        Serial.print(digitalRead(led));
      }
      incoming = ' ';
  }
}

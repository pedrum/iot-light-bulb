//IoT Light Bulb - Arduino Controller
int led = 13;
char incoming = ' ';

void setup() {                
  pinMode(led, OUTPUT);     
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
      incoming = Serial.read();
      
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

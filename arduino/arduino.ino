//IoT Light Bulb - Arduino Controller
int led = 13;
int relay = 7;
char incoming = ' ';

void setup() {                
  pinMode(led, OUTPUT);
  pinMode(relay, OUTPUT);  
  digitalWrite(relay, HIGH);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
      incoming = Serial.read();
      
      if (incoming == '0') {
        digitalWrite(led, LOW);
        digitalWrite(relay, HIGH);  
      } else if (incoming == '1') {
        digitalWrite(led, HIGH);
        digitalWrite(relay, LOW);
      } else if (incoming =='q') {
        Serial.print(digitalRead(led));
      }
      incoming = ' ';
    }
}

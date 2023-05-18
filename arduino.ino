String command ;

void setup() {
  
  Serial.begin(9600);

  pinMode(13, OUTPUT);
  
}

void loop() {

  if (Serial.available() > 0) {

  command = Serial.readStringUntil('\n');

    if (command == "on") {
    
      digitalWrite(13, HIGH);

    }

    else if (command == "off") {

      digitalWrite(13, LOW);

    }  
  }
}

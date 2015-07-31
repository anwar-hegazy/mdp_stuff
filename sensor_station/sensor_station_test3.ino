//sensor station version 1 million

int s1, s2, s3, s4, s5, s6;
int numLEDs = 11;
int numSENSORS = 6;

void setup() {

  //set all output pins for LEDs
  for ( int i = 0 ; i < numLEDs; i++ ) {
    pinMode( i + 2, OUTPUT);
  }

  //set all input pins for Sensors
  for ( int i = 0; i < numSENSORS; i++ ) {
    pinMode(i, INPUT );
  }
  Serial.begin(9600);
}

void loop() {

  for ( int i; i < numSENSORS; i++) {
    sensor = analogRead(0);
    Serial.print("sensor" + String(i) + " ");
    Serial.println(sensor);
  }

}

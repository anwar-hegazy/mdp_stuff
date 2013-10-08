/*
Sensor Station Test
 */

// super rough way to test sensor station
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  int sensorValue1 = analogRead(A0);
  int sensorValue2 = analogRead(A1);
  Serial.print( "pot1 = " );
  Serial.println(sensorValue1);
  Serial.print( "pot2 = " );
  Serial.println(sensorValue2);  
  delay(1);
}

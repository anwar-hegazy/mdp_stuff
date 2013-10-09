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
  int sensorValue3 = analogRead(A2);
  Serial.print( "pot1 = " );
  Serial.print(sensorValue1);
  Serial.print("\t");
  Serial.print( "pot2 = " );
  Serial.print(sensorValue2);
  Serial.print("\t");
  Serial.print( "slider = " );
  Serial.print( sensorValue3 );
  Serial.println("");
  delay(1);
}

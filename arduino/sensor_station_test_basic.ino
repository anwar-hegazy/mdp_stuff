/*
Sensor Station Test
 */

 int sensorValue1;
 int sensorValue2;
 int sensorValue3;
 int sensorValue4;
 int sensorValue5;
 int sensorValue6;

// super rough way to test sensor station
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  sensorValue1 = analogRead(A0);
  sensorValue2 = analogRead(A1);
  sensorValue3 = analogRead(A2);
  sensorValue4 = analogRead(A3);
  sensorValue5 = analogRead(A4); 
  Serial.print( "pot1 = " );
  Serial.print(sensorValue1);
  Serial.print("\t");
  Serial.print( "pot2 = " );
  Serial.print(sensorValue2);
  Serial.print("\t");
  Serial.print( "slider = " );
  Serial.print( sensorValue3 );
  Serial.print("\t");
  Serial.print( "photo = " );
  Serial.print( sensorValue4 );
  Serial.print("\t");
  Serial.print( "bend = " );
  Serial.print( sensorValue5;
  Serial.print("\t");
  Serial.print( "force = " );
  Serial.print( sensorValue6 );
  Serial.println("");
  delay(1);
}
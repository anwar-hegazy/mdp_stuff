/*
Sensor Station Test
 this is purely to test power issues across a ton of sensors on the arduino mega
 */

int sensorValue0;
int sensorValue1;
int sensorValue2;
int sensorValue3;
int sensorValue4;
int sensorValue5;
int sensorValue6;
int sensorValue7;
int sensorValue8;
int sensorValue9;

int pirPin = 2;
int pirVal;

// super rough way to test sensor station
void setup() {

  Serial.begin(9600);
  pinMode(pirPin, INPUT);

}

void loop() {
  //read sensors
  sensorValue0 = analogRead(A0);  //270 deg pot
  sensorValue1 = analogRead(A1);  //continuous
  sensorValue2 = analogRead(A2);  //10 turn
  sensorValue3 = analogRead(A3);  //slider
  sensorValue4 = analogRead(A4);   //force
  sensorValue5 = analogRead(A5);  //photo
  sensorValue6 = analogRead(A6); //ir
  sensorValue7 = analogRead(A7);
  //  sensorValue9 = analogRead(A8);
  //  sensorValue10 = analogRead(A9);
  //  pirVal = digitalRead(pirPin);

  Serial.print( "pot1 = " );
  Serial.print(sensorValue0);
  Serial.print("\t");
  Serial.print( "pot2 = " );
  Serial.print(sensorValue1);
  Serial.print("\t");
  Serial.print( "10 turn = " );  //doesnt work? blown out, i think
  Serial.print( sensorValue2 );
  Serial.print("\t");
  Serial.print( "slider = " );    //noisy?
  Serial.print( sensorValue3 );
  Serial.print("\t");
  Serial.print( "force = " );
  Serial.print( sensorValue4);
  Serial.print("\t");
  Serial.print( "photo = " );
  Serial.print( sensorValue5 );
  Serial.print("\t");
  Serial.print( "ir = " );
  Serial.print( sensorValue6 );
  Serial.print("\t");
//  Serial.print( "accel x = ");
//  Serial.print(sensorValue7);
//  Serial.print( ", y = ");
  Serial.println("");
  //  Serial.print(sensorValue9 );
  //  Serial.print( ", z = ");
  //  Serial.print(sensorValue10);
  //  Serial.println("");
  //  if( pirVal ==   LOW) {
  //    Serial.println( "MOTION DETECTED!!!!!");
  //  }
  delay(1);
}









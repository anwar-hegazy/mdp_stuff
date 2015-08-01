/*
Sensor Station plus MUX, test file for just one 4051
Casey Anderson, 2015

Based on this help doc: http://playground.arduino.cc/Learning/4051

 */

int r0 = 0;
int r1 = 0;
int r2 = 0;

int mux1, sensorValue1, which1;

void setup() {

  pinMode(A0, INPUT);       // mux1 input
  pinMode(A1, INPUT);       // mux1 sensor selector input

  //ino to mux 1 (changes what input shows up at 4051 output, attached to A0)
  pinMode(2, OUTPUT);    // s0
  pinMode(3, OUTPUT);    // s1
  pinMode(4, OUTPUT);    // s2

  // //output LEDs
  pinMode( A2, OUTPUT );

  Serial.begin (115200);
}

void loop () {

  sensorValue1 = analogRead(A1);

  which1 = map(sensorValue1, 0, 1023, 0, 7);

  // select the bit (MUX1)
  r0 = bitRead(which1, 0);
  r1 = bitRead(which1, 1);
  r2 = bitRead(which1, 2);

  // write the bit (MUX1)
  digitalWrite(2, r0);
  digitalWrite(3, r1);
  digitalWrite(4, r2);

  mux1 = analogRead(A0);     // MUX1 ouputs here

  // LED output
  analogWrite(A2, mux1);

  Serial.print("MUX 1: sensor number ");
  Serial.print(which1);
  Serial.print('\t');
  Serial.print("val is ");
  Serial.println(mux1);

  delay(2);
}

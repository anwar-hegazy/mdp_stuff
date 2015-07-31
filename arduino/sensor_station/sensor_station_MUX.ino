/*
Sensor Station plus MUX
Casey Anderson, 2015

Based on this help doc: http://playground.arduino.cc/Learning/4051

 */

int r0 = 0;
int r1 = 0;
int r2 = 0;

int  r3 = 0;
int  r4 = 0;
int  r5 = 0;

int mux1, sensorValue1, which1;
int mux2, sensorValue2, which2;


void setup() {
  pinMode(A0, INPUT);       // mux1 input
  pinMode(A1, INPUT);       // mux2 input

  pinMode(A2, INPUT);       // mux1 sensor selector input
  pinMode(A3, INPUT);       // mux2 sensor selector input

  //ino to mux 1 (changes what input shows up at 4051 output, attached to A0)
  pinMode(2, OUTPUT);    // s0
  pinMode(3, OUTPUT);    // s1
  pinMode(4, OUTPUT);    // s2

  //ino to mux 2 (changes what input shows up at 4051 output, attached to A1)
  pinMode(5, OUTPUT);    // s0
  pinMode(6, OUTPUT);    // s1
  pinMode(7, OUTPUT);    // s2

  Serial.begin (115200);
}

void loop () {

  //  which = (7);              // just for testing
  sensorValue1 = analogRead(A2);
  sensorValue2 = analogRead(A3);

  which1 = map(sensorValue1, 0, 1023, 0, 7);
  which2 = map(sensorValue2, 0, 1023, 0, 7);

  // select the bit (MUX1)
  r0 = bitRead(which1, 0);
  r1 = bitRead(which1, 1);
  r2 = bitRead(which1, 2);

  // select the bit (MUX2)
  r3 = bitRead(which2, 0);
  r4 = bitRead(which2, 1);
  r5 = bitRead(which2, 2);

  // write the bit (MUX1)
  digitalWrite(2, r0);
  digitalWrite(3, r1);
  digitalWrite(4, r2);

  // write the bit (MUX2)
  digitalWrite(5, r0);
  digitalWrite(6, r1);
  digitalWrite(7, r2);

  mux1 = analogRead(A0);     // MUX1 ouputs here
  mux2 = analogRead(A1);     // MUX2 ouputs here

  Serial.print("MUX 1: sensor number ");
  Serial.print(which1);
  Serial.print('\t');
  Serial.print("val is ");
  Serial.print(mux1);
  Serial.print('\t');
  Serial.print("MUX 2: sensor number ");
  Serial.print(which2);
  Serial.print('\t');
  Serial.print("val is ");
  Serial.print(mux2);

  delay(2);
}

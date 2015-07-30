/*
Sensor Station plus MUX

 * codeexample for useing a 4051 * analog multiplexer / demultiplexer
 * by david c. and tomek n.* for k3 / malmï¿½ hï¿½gskola
 *
 * edited by Ross R.
 */

int r0 = 0;      //value of select pin at the 4051 (s0)
int r1 = 0;      //value of select pin at the 4051 (s1)
int r2 = 0;      //value of select pin at the 4051 (s2)
int which = 0;   //which y pin we are selecting
int val, sensorValue;

void setup() {
  pinMode(A0, INPUT);       // mux1 input
  pinMode(2, OUTPUT);    // s0
  pinMode(3, OUTPUT);    // s1
  pinMode(4, OUTPUT);    // s2

  Serial.begin (115200);
}

void loop () {

  //  which = (7);              // just for testing
  sensorValue = analogRead(A2);
  which = map(sensorValue, 0, 1023, 0, 7);

  // select the bit
  r0 = bitRead(which, 0);
  r1 = bitRead(which, 1);
  r2 = bitRead(which, 2);    // use this with arduino 0013 (and newer versions)

  digitalWrite(2, r0);
  digitalWrite(3, r1);
  digitalWrite(4, r2);

  //Either read or write the multiplexed pin here
  // refactor, this should be digitalWrite with millis or something
  val = analogRead(A0);     // MUX ouputs here

  Serial.print("sensor number ");
  Serial.print(which);
  Serial.print('\t');
  Serial.print("val is ");
  Serial.println(val);

  delay(2);
}

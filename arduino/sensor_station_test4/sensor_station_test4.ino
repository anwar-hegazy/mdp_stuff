//sensor station version 1 million

int s1, s2, s3, s4, s5, s6;
int numLEDs = 11;
int numSENSORS = 6;

void setup() {

  //set all input pins for Sensors
  //  for ( int i = 0; i < numSENSORS; i++ ) {
  //    pinMode(i, INPUT );
  //  }

  //there is definitely a better way to do this...refactor with for loop, make sure to hold onto letters (A, D)

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);

  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  s1 = analogRead(A0);
  s2 = analogRead(A1);
  s3 = analogRead(A2);
  s4 = analogRead(A3);
  s5 = analogRead(A4);
  //  s6 = analogRead(A5);

  analogWrite( 2, map( s1, 0, 1023, 0, 255 ) );
  analogWrite( 3, map( s2, 0, 1023, 0, 255 ) );
  analogWrite( 4, map( s3, 0, 1023, 0, 255 ) );
  analogWrite( 5, map( s4, 0, 1023, 0, 255 ) );
  analogWrite( 6, map( s5, 0, 1023, 0, 255 ) );
  //  analogWrite( 7, map( s6, 0, 1023, 0, 255 ) );

  Serial.println(s5);

  delay(2);
}

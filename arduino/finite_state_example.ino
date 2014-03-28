// finite_state_example.ino

long randNumber;

void setup() {
	Serial.begin(9600);
}

void loop() {
	int number = random(3);		//random number from 0 - 4
	Serial.println( number );
	if( number == 0){
		//movement 1
		Serial.println( "movement 1!");
		//servo.write( 30 );
	} else if( number == 1) {
		//movement 2
		Serial.println( "movement 2!");
		//servo.write( 127);
	} else if( number == 2){
		//movement 3
		Serial.println( "movement 3!");
		//servo.write( 0 );
	}
	delay(100);		// remember, this is not what you want on the galileo (use millis!)
}

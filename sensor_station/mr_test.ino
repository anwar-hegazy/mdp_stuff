/*
ino sensor station tests/notes for flex, ir, sonar, etc.

*/

int val;

void setup(){
    
    pinMode(A0, INPUT);
    pinMode(A1, OUTPUT);

    Serial.begin(9600);

}

void loop(){

    val = analogRead(A0);

    analogWrite(A1, val);

    Serial.print("val is ");
    Serial.print('/t');
    Serial.println(val);

    delay(2);
}

/*minimal millis example
this is the bare minimum to get a timer in arduino
*/

int previousMillis = 0;

long interval = 1000;// we want to know when 1 second has passed

void setup(){
  //since we are only using a timer right now, there is nothing here (other than serial)
  Serial.begin(9600);
}

void loop(){
 unsigned long currentMillis = millis();// how long has the program been running? store that length in currentMillis
 
 //check to see if we have run out of time
 if( currentMillis - previousMillis > interval ) {
   previousMillis = currentMillis;
   
   Serial.print( "it has been " );
   Serial.print( String(interval) );
   Serial.println( " milliseconds!" );
 } else {
   Serial.print( "current time = " );
   Serial.println( String(currentMillis) );
 }
}

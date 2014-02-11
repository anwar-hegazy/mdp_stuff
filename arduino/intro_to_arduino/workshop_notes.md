Intro to Arduino
Media Design Practices, 2/12

The Electronics
(assumes usage of the Arduino Uno)

This is meant as a basic overview of the Uno. For a more comprehensive overview, see this page: http://arduino.cc/en/Main/ArduinoBoardUno.

The Uno is based on the ATmega328, the datasheet for which you can find here: http://www.atmel.com/Images/doc8161.pdf

Get used to looking for datasheets. They are generally published by the manufacturer as a complete resource for how a particular Integrated Circuit functions, containing things like detailed information regarding Current, Voltage, etc. features/requirements, as well as the role of each pin. Any time you are trying to build something that requires an IC you have not used before your first step should be to look for the datasheet. This is almost always accomplished via a simple Google search (example: ATmega328 datasheet).

void setup() vs. void loop()
Whatever code is placed in void setup() will be called once immediately when the application starts. It will not be called again. Therefore, this is a good place to declare variables, pin modes, start using libraries, etc.

The loop() function is called repeatedly from then on. So, any component of your code that accepts changing values (for example, monitoring live sensor input) should go here.

Here is the basic structure for almost every Arduino program you will need to implement:
''''
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly: 
  
}
''''
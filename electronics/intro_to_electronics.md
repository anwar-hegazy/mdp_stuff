## Intro to Electronics
*Summer 2014, Casey Anderson*

Electricity = the flow of electrons.

In order to measure electricity, one needs to be able to figure out the number of electroncs in "the flow."

*Example 1*
There is a large tank of water (atop a very tall building). This tank has a pipe coming out of it that is capable of distributing water to a small bucket on the ground below (next to the building). For the time being, the pipe has a stopper of some sort in one end.

The water in the tank has an evenly distributed number of dust particles in it (in this case, 10 specks of dust in ever cubic centimeter of water).

Since the dust particles are evenly distributed, one can confidently deduce the following:

1. If x amount of water flows through the pipe, one can calculate the number of specks of dust which have flowed through the pipe.
2. By knowing the number of specks of dust which have flowed through the pipe, one can calculate the volume of water.

This example is analagous to electricity, however the "dust specks" are electrons.

### "Flow Rate"
  * Measured as a volume of water flowing through the pipe during a defined period of time.
  * In electronics, the flow rate is referred to as Current (symbol: I)
  * Current is measured in amperes (or amps, symbol: A)
  * 1 amp = the quantity of 1 coulomb (unit of measurement describing the number of electrons, i.e. amount of "charge") passing a point in one second

### "Flow Pressure"
  * Imagine that the building, in Example 1, is three stories in one scenario and one story in another. How would one described the difference between these two scenarios?
  * The energy contained in the water in the tank defines the water pressure. In other words, the higher the water tank, the more energy potentially exists if it were to flow.
  * In electronics, flow pressure is defined by the difference in numbers of electrons between two points.
  * This is referred to as the potential difference, but is generally simply denoted by the term Voltage (symbol: V). Potential Difference and Voltage refer to the SAME electrical characteristic.
  * The word "potential" is key in one's understanding of Voltage. Example, regardless of whether or not a 9V battery is in use, it POTENTIALLY has a 9V difference between its two terminals regardless of whether it is in use or not.
  * In other words, the battery has the potential to drive an electron through a circuit due to its 9V difference in charge.

*Example 2*
A battery powers a small lightbulb.
This could be described as series of related actions:

  * The battery generates electrons at one terminal and takes in electrons at the other terminal
  * The bulb lights up as electrons flow around the circuit
  * The electrons flow around the circuit due to potential difference of battery

Batteries force electrons around a circuit only when the circuit is complete. If one end of the battery is not connected there will be no electron flow, but the battery will still have the POTENTIAL to cause such a flow upon completion of the circuit. The higher the battery's voltage, the harder a cell can force electrons around a circuit.

As a subtle alteration to this example, disconnect the battery from the lightbulb. Such an action results in the following changes to our circuit:

  * The bulb does not light up
  * There is no electron flow
  * Air, an insulator, prevents electrons from jumping from one conductor (i.e. wire) to the other.

### "Flow ease"


Resistors
used to control current and voltage in specified ways

it would be impractical to have resistors of every possible value...there would be millions

so, there is an agreed upon range of values, however made within a certain tolerance

  RESISTOR TOLERANCE – specified as a plus or minus percentage

  A 10ohm plus/minus 10% resistor

    -so, what is the actual range?
    9-11ohms

  resistors are also rated by the amount of power they can safely dissipate as heat without being   damaged.
    -this is the power rating, measured in watts
    typical resistors – 1/4W, 1/3W, 1/2W, etc.
    in other words, exceeding this value will likely melt the componen

  generally – higher the resister, the less current flows...

Ohm's Law
  volts - “pushing power”
  amps - “rate of electron flow”

  3V
  vs
  4V

  V/I = a constant
    -where the constant depends on the substance through which current flows and voltage is 
    applied across

  Draw picture
1. Cell has 2V
2. current of 0.4A
3. substance with a resistance of 5ohms

  cell has a voltage of 2V, so the voltage applied across the substance is also 2V.

  The current through the substance is 0.4A

  Ohm's Law:
    2V/0.4A = 5ohms
  the constant is commonly called the substance's resistance and is given the unit omega
    -pronounced ohm

  So the resistance is 5ohms
    -sometimes people use the letter R instead of omega

  So, if a voltage (V, measured in volts) is applied across a resistance (R, measured in ohms), a current (I, measured in amps) will flow.

  In other words: V/I = R

  What does the current depend on?
    -values of resistance and voltage
  
  How would you determine the current if you already knew the voltage?
    How would we do this with our example?
    V/R = I
    2V/5ohms = 0.4A

  So, what would a voltage of 10V, applied across a resistance of 20ohms, produce a current of?

    First, let's write this out:
    10V/20ohms = 0.5A

  What if we know the resistance and current and want to deduce the voltage?
    -in other words, if we have a resistance, and a current is made to flow through it, then a 
    voltage is produced across it
      how would we write this?
      V = IR
      5ohms x 0.4A = 2V

  What if we had a current of 1A flowing through a resistance of 5ohms
    how would we write this?
      1A * 5ohms = 5V
  
  Another way to remember
    draw triangle
    Cover up the missing one and do the calculation
    V/R = I
    V/I = R
    IR = V
    RI = V

  Note: voltage always applied ACROSS
    why?
      It is the force that pushes electrons...the pushing power
    
    current always flows THROUGH
    why?
      It is the rate at which electrons flow through
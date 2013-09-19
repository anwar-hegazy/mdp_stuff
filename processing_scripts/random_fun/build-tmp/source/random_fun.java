import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class random_fun extends PApplet {

float fxPos;
int ixPos;

float fyPos;
int iyPos;

float fSwitch;
int iSwitch;
int prob = 500;
int ellipseR = 1;  // sets the radius of all elipses and keeps them from falling off the screen
int lineWeight = 1;
int movingLinex = 0;
int randomY = 0;
int cVal1, cVal2, cVal3;

public void setup() {
  size( 500, 500 );
  background( 255, 255, 255 );
}

public void draw() {

  movingLinex++;    // increment x position for line, or other ball
  randomY = PApplet.parseInt( random( 0, ( height - ellipseR ) ) );  // random y for line or other ball
  noStroke();

  //get a random xposition on the screen
  fxPos = random( 0, (width - ellipseR ) );
  ixPos = PApplet.parseInt( fxPos );
  //println(ixPos);

  //get a random yposition on the screen
  fyPos = random( 0, (height - ellipseR ) );
  iyPos = PApplet.parseInt( fyPos );
  //println(ixPos);

  fSwitch = random( prob );    //1/5's chance that the value will be used
  iSwitch = PApplet.parseInt( fSwitch );
  println( "iSwitch is " + iSwitch );
  //randomly allows that position to be used
  if ( iSwitch == (prob/2) ) {
    println( "RANDOMLY CHANGED POSITION," + " new xposition is " + ixPos + "new yposition is " + iyPos );
    background( 255, 255, 255 );
    ellipse( ixPos, iyPos, ellipseR, ellipseR );
  }
  else if ( iSwitch == (prob/ 5) ) {
    println( "RANDOMLY CHANGED COLOR" );
    background( 255, 255, 255 );
    cVal1 = PApplet.parseInt( random( 255 ) );
    cVal2 = PApplet.parseInt( random( 255 ) );
    cVal3 = PApplet.parseInt( random( 255 ) );
    fill( cVal1, cVal2, cVal3 );
    ellipse( ixPos, iyPos, ellipseR, ellipseR );
  }
  //background( 255, 255, 255 );
  stroke( cVal1, cVal2, cVal3 );
  strokeWeight( lineWeight );
  line( ixPos, iyPos, movingLinex, randomY );
  noStroke();
  fill( cVal1, cVal2, cVal3 );
  ellipse( movingLinex, randomY, ellipseR, ellipseR );

  if ( movingLinex >= width ) {
    movingLinex = 0;
    println( "RESET X TO 0!!!!!!" );
  }
}

/*
//scale that position to a smaller range with map()
 */
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "random_fun" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}

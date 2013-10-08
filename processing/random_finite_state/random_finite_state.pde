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

void setup() {
  size( 500, 500 );
  background( 255, 255, 255 );
}

void draw() {

  movingLinex++;    // increment x position for line, or other ball
  randomY = int( random( 0, ( height - ellipseR ) ) );  // random y for line or other ball
  noStroke();

  //get a random xposition on the screen
  fxPos = random( 0, (width - ellipseR ) );
  ixPos = int( fxPos );
  //println(ixPos);

  //get a random yposition on the screen
  fyPos = random( 0, (height - ellipseR ) );
  iyPos = int( fyPos );
  //println(ixPos);

  fSwitch = random( prob );    //1/5's chance that the value will be used
  iSwitch = int( fSwitch );
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
    cVal1 = int( random( 255 ) );
    cVal2 = int( random( 255 ) );
    cVal3 = int( random( 255 ) );
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

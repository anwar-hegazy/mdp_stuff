//read csv file, format an array with all of our data, hacky sanitization example

/*the sample csv file im using has an \n character at the end of the line, which was getting stored at position 3
im only going to use position 1 and 2 (or 0 and 1), so im just creating a two position second dimension as a quick hack.
there is most certainly a better way to do this (in python this is super easy: array[position].pop, in java it is annoyingly more complicated),
i just cannot remember right now and this way works too so whatever...
*/

int counter = 0;
String[] pieces;                //we will use this to store the first line of our array prior to sanitization
String[][] newPieces;              //this is where all of our data will go
int numLines;                  //this gives us a counter that we can access (if we need one)
// int numItems = 

void setup(){
	size(500, 500);

String [] lines = loadStrings("/Users/cta/Desktop/core_a_datacopy1.csv");
numLines = (lines.length);
println("there are " + numLines + " lines!");
newPieces = new String[numLines][3];
println("newPieces is an array of length " + str(newPieces.length));

//this for loop splits each line from the csv file at the comma, resulting in a three position array for each line
for ( String line : lines ) {
  // println("line number " + counter);    //checking to make sure this is all working correctly
  pieces = split(line, ',');          //splits each line at the comma

  for ( int i = 0; i < 2; i++ ){
                        // println("pos number " + str(i));    //checking to make sure this is all working correctly
    newPieces[counter][i] = pieces[i];
                        // println(newPieces[counter][i]);    //again, this is used as another check
    }

  counter++;                  //increments counter, used to properly insert sanitized data into newPieces
  }
noLoop();					//noLoop disables void draw's default looping behavior
}

void draw(){

  // this just reads through all of newPieces and prints the sanitized array to, again, check to make sure this is all working
  for (int i = 0; i < numLines; i++){
    //int x = int(random( numLines ));
    println(newPieces[i][0] + ", " + newPieces[i][1]);
    ellipse( int(newPieces[i][1]), int(newPieces[i][0]), 50, 50 );
  }
}
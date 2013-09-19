ArrayList balls = new ArrayList();
ArrayList vels = new ArrayList();
int noAnimalTypes = 3;
int sW = 1000;
int sH = 500;

void setup() {
  for (int i = 0; i<10;i++) {
    float r = random( 1, 10 );
    balls.add(new Ball((int) random( 0, noAnimalTypes-.0000001 ), 1, random( 0, sW ), random( 0, sH), r));
    vels.add(new PVector(random( -2, 1 ), random( -2, 1 )) );
  };
  size(sW, sH);
  smooth();
  noStroke();
}

void draw() {
  background(51);
  fill(204);
  for (int i=0; i< balls.size(); i++) {
    ((Ball) balls.get(i)).x += ((PVector) vels.get(i)).x;
    ((Ball) balls.get(i)).y += ((PVector) vels.get(i)).y;
    ellipse(((Ball) balls.get(i)).x, ((Ball) balls.get(i)).y, ((Ball) balls.get(i)).r*2, ((Ball) balls.get(i)).r*2);
    checkBoundaryCollision(((Ball) balls.get(i)), ((PVector) vels.get(i)));
  }
  checkObjectCollision(balls, vels);
}

void checkObjectCollision(ArrayList bList, ArrayList vList) {

  int[] noNewAnimals = new int[noAnimalTypes];

  for ( int i = 0; i < noAnimalTypes; i++ ) {
    noNewAnimals[i]=0;
  }

  Ball[] b = new Ball[bList.size()];
  PVector[] v = new PVector[vList.size()];

  for ( int i = 0; i < b.length; i++ ) {
    b[i] = ((Ball) bList.get(i));
    v[i] = ((PVector) vList.get(i));
  }

  for ( int i = 0; i < b.length; i++ ) {
    for ( int j = i + 1; j < b.length; j++ ) {

      // get distances between the balls components
      PVector bVect = new PVector();
      bVect.x = b[i].x - b[j].x;
      bVect.y = b[i].y - b[j].y;

      // calculate magnitude of the vector separating the balls
      float bVectMag = sqrt(bVect.x * bVect.x + bVect.y * bVect.y);
      if (bVectMag < b[j].r + b[i].r) {

        //Breed
        if (b[i].a == b[j].a) {
          noNewAnimals[b[i].a] += 1;
        } 
        else if (b[i].a > b[j].a) {
          ((Ball) bList.get(j)).s-=1;
        } 
        else {
          ((Ball) bList.get(i)).s-=1;
        }

        // get angle of bVect
        float theta  = atan2(bVect.y, bVect.x);
        // precalculate trig values
        float sine = sin(theta);
        float cosine = cos(theta);

        /* bTemp will hold rotated ball positions. You 
         just need to worry about bTemp[1] position*/
        Ball[] bTemp = {  
          new Ball(), new Ball()
          };

          /* b[i]'s position is relative to b[j]'s
           so you can use the vector between them (bVect) as the 
           reference point in the rotation expressions.
           bTemp[0].x and bTemp[0].y will initialize
           automatically to 0.0, which is what you want
           since b[i] will rotate around b[j] */
          bTemp[1].x  = cosine * bVect.x + sine * bVect.y;
        bTemp[1].y  = cosine * bVect.y - sine * bVect.x;

        // rotate Temporary velocities
        PVector[] vTemp = { 
          new PVector(), new PVector()
          };
          vTemp[0].x  = cosine * v[j].x + sine * v[j].y;
        vTemp[0].y  = cosine * v[j].y - sine * v[j].x;
        vTemp[1].x  = cosine * v[i].x + sine * v[i].y;
        vTemp[1].y  = cosine * v[i].y - sine * v[i].x;

        /* Now that velocities are rotated, you can use 1D
         conservation of momentum equations to calculate 
         the final velocity along the x-axis. */
        PVector[] vFinal = {  
          new PVector(), new PVector()
          };
          // final rotated velocity for b[j]
          vFinal[0].x = ((b[j].m - b[i].m) * vTemp[0].x + 2 * b[i].m * 
            vTemp[1].x) / (b[j].m + b[i].m);
        vFinal[0].y = vTemp[0].y;
        // final rotated velocity for b[j]
        vFinal[1].x = ((b[i].m - b[j].m) * vTemp[1].x + 2 * b[j].m * 
          vTemp[0].x) / (b[j].m + b[i].m);
        vFinal[1].y = vTemp[1].y;

        // hack to avoid clumping
        bTemp[0].x += vFinal[0].x;
        bTemp[1].x += vFinal[1].x;

        /* Rotate ball positions and velocities back
         Reverse signs in trig expressions to rotate 
         in the opposite direction */
        // rotate balls
        Ball[] bFinal = { 
          new Ball(), new Ball()
          };
          bFinal[0].x = cosine * bTemp[0].x - sine * bTemp[0].y;
        bFinal[0].y = cosine * bTemp[0].y + sine * bTemp[0].x;
        bFinal[1].x = cosine * bTemp[1].x - sine * bTemp[1].y;
        bFinal[1].y = cosine * bTemp[1].y + sine * bTemp[1].x;

        // update balls to screen position
        ((Ball) bList.get(i)).x = ((Ball) bList.get(j)).x + bFinal[1].x;
        ((Ball) bList.get(i)).y = ((Ball) bList.get(j)).y + bFinal[1].y;
        ((Ball) bList.get(j)).x = ((Ball) bList.get(j)).x + bFinal[0].x;
        ((Ball) bList.get(j)).y = ((Ball) bList.get(j)).y + bFinal[0].y;
        //        b[i].x = b[j].x + bFinal[1].x;
        //        b[i].y = b[j].y + bFinal[1].y;
        //        b[j].x = b[j].x + bFinal[0].x;
        //        b[j].y = b[j].y + bFinal[0].y;

        // update velocities
        ((PVector) vList.get(j)).x = cosine * vFinal[0].x - sine * vFinal[0].y;
        ((PVector) vList.get(j)).y = cosine * vFinal[0].y + sine * vFinal[0].x;
        ((PVector) vList.get(i)).x = cosine * vFinal[1].x - sine * vFinal[1].y;
        ((PVector) vList.get(i)).y = cosine * vFinal[1].y + sine * vFinal[1].x;
        //        v[j].x = cosine * vFinal[0].x - sine * vFinal[0].y;
        //        v[j].y = cosine * vFinal[0].y + sine * vFinal[0].x;
        //        v[i].x = cosine * vFinal[1].x - sine * vFinal[1].y;
        //        v[i].y = cosine * vFinal[1].y + sine * vFinal[1].x;
      }
    }
  }
  
  int k = 0;
  while(k < bList.size()){
    if(((Ball) bList.get(k)).s == 0){
      bList.remove(k);
    } else {
      k++;
    }
  }

  for ( int i = 0; i < noAnimalTypes; i++ ) {
    for ( int j = 0; j < noNewAnimals[i]; j++ ) {
      float r = random( 5, 50 );
      balls.add(new Ball(i, 1, random( 0, 640 ), random( 0, 360), r));
      vels.add(new PVector(random( -2, 1 ), random( -2, 1 )) );
    }
  }
}

void checkBoundaryCollision(Ball ball, PVector vel) {
  if (ball.x > width-ball.r) {
    ball.x = width-ball.r;
    vel.x *= -1;
  } 
  else if (ball.x < ball.r) {
    ball.x = ball.r;
    vel.x *= -1;
  } 
  else if (ball.y > height-ball.r) {
    ball.y = height-ball.r;
    vel.y *= -1;
  } 
  else if (ball.y < ball.r) {
    ball.y = ball.r;
    vel.y *= -1;
  }
}


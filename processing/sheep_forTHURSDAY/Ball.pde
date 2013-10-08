class Ball{
  float x, y, r, m;
  int a;
  int s;

  // default constructor
  Ball() {
  }

  Ball(int a, int s, float x, float y, float r) {
    this.a = a;
    this.s = s;
    this.x = x;
    this.y = y;
    this.r = r;
    m = r*.1;
  }
}



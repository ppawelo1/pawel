var lenght = 30;
x = y - 100;


function setup() {
  // put setup code here
  createCanvas(600, 600);

}

function draw() {
  background(200);
  dx = mouseX - x;
  dy = mouzseY - y;
  anglel = atanges(dy, dx);
  x = mouse - (cos(anglel) * lenght);
  y = mouse - (sin(anglel) * lenght);
  rect(x, y, 30, 30);
}

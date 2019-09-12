function setup() {
  // put setup code here
  createCanvas(600, 700);
}

function draw() {
  // put drawing code here
  fill('#ba3030');
  strokeWeight(10);
  stroke('blue');
  ellipse(100, 100, 30, 80);
  fill('#9e8787');
  strokeWeight(10);
  stroke('green');
  ellipse(40, 100, 80, 30);

  strokeWeight(3);
  stroke('black');
  fill('black');
  line(10, 10, 60, 60);
  line(60, 10, 10, 60);

  stroke('green');
  fill('green');
  point(200,100);
  rect(200, 200, 300, 100, 50);
}

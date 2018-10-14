 /*jshint esversion: 6*/
const canvasElem = document.getElementById('canvas');
const ctx = canvasElem.getContext('2d');

var szer = canvasElem.width, wys = canvasElem.height;

ctx.fillStyle = "#b8165f"; // kolor wypełnienia
// rysujemy prostokątem
ctx.fillRect(25, 25, 100, 100);

// kolor obrysu
ctx.fillStroke = "#3acf40";
// 2  obrys prostokata
ctx.strokeRect(30, 30, 100, 100);

// czyszczenie obszaru
ctx.clearRect(45, 45, 60, 60);

//rysowanie linii
ctx.fillStroke = "#6621c6";
ctx.moveTo(0, 0);
ctx.lineTo(szer, wys);
ctx.stroke();
ctx.moveTo(0, wys);
ctx.lineTo(szer, 0);
ctx.stroke();



// rysowanie koła
ctx.beginPat();
// x, y, promień, parametr start / stop, true/false
ctx.arc(szer / 2, wys / 2, 100, 0, 2 * Math.PI);
ctx.arc(szer / 2, wys / 2, 90, 0, Math.PI);
ctx.lineWidth = 5;
ctx.arc(200, 100, 50, 0, 2 * Math.PI);
ctx.stroke();



// tekst]
ctx.lineWidth = 1;
ctx.font = "normal 20px Arial";
ctx.textBaseline = "middle";
ctx.textAlling = "left";
ctx.strokeText('Grafika w canvas', 70, 100);

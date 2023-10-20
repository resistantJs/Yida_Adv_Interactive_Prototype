import js as p5
from js import document

data = None
angle = 0

def setup():
  p5.createCanvas(300, 300)
  print('hello p5!')

def draw():
  p5.background(255)

  global data, angle
  data = document.getElementById("data").innerText
  
  circle_size = int(data)
  p5.noStroke()
  p5.fill(150)
  #p5.ellipse(150, 150, circle_size, circle_size)
  p5.push()
  
  #set angle var to int of data
  angle = int(data)
  #move to middle of canvas
  p5.translate(pt.width/2, pt.height/2)
  #rotate canvas with angle converted from degrees to radians:
  p5.rotate(p5.radians(angle))
  # change mode to drawr rectangels from center:
  p5.rectMode(p5.CENTER)
  #draw rect at coordinate 0, 0 and 100 width and height
  p5.rect(0,0,100,100)
  #rectore graphical transformation
  p5.pop()


  

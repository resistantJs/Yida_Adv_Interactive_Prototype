import js as p5
from js import document
import time
import math

data = None
angle = 0

state = 'done'
statetimer = 0
lasttime = 0
velocity = 4
y = 0
a = 0



def setup():
  p5.createCanvas(300, 300)
  print('hello p5!')

def draw():
  p5.background(255)

  global data, angle, state, statetimer, lasttime, y, a
  data_String = document.getElementById("data").innerText
  data_list = data_String.split(',')
  data = data_list[0]
  button_val = int(data_list[1])

  p5.text(int(data), 10, 20)
  p5.text(button_val, 10, 30)
  p5.text(state, 10, 40)
  p5.text('time:'+ str(time.time()), 10, 50)
  p5.text('statetime:'+ str(statetimer), 10, 60)
  p5.text('lasttime:'+ str(lasttime), 10, 70)
  p5.text('y:'+ str(y), 10, 80)


  circle_size = int(data)
  p5.noStroke()
  p5.fill(150)
  #p5.ellipse(150, 150, circle_size, circle_size)

  if button_val == 1 :
    state = 'shoot'
    lasttime = time.time()
    a = abs(90 - angle)

    
  if state == 'shoot' :
    displayed = False
    if not displayed:
      display()
      displayed = True
    shoot()
  p5.push()
  #set angle var to int of data
  angle = int(data)
  #move to middle of canvas
  p5.translate(20, p5.height-20)
  #rotate canvas with angle converted from degrees to radians:
  p5.rotate(p5.radians(angle))
  # change mode to drawr rectangels from center:
  p5.rectMode(p5.CENTER)
  #fill rect with red color
  p5.fill(0,250,250)
  #fill rect with shades of gray base on angle change
  #p5.fill(angle)
  #draw rect at coordinate 0, 0 and 100 width and height
  p5.rect(0,0,50,100)
  #rectore graphical transformation
  p5.pop()

  

def display():
  global y
  p5.push()
  p5.translate(statetimer*200, -y*200)
  p5.fill(0,0,0)
  p5.ellipse(20, p5.height-20, 20, 20)
  p5.pop()
  
def shoot():
  global a, state, statetimer, lasttime, velocity, y
  if state == 'shoot':
    statetimer = time.time() - lasttime
    v = velocity
    x = statetimer
    #a = angle
    y = 0 - 4.9 * (x / (v*math.cos(a* math.pi / 180)) ) * (x / (v*math.cos(a* math.pi / 180)) ) + math.tan(a* math.pi / 180) * x
    
    if y < -1 :
      state = 'done'
    




  

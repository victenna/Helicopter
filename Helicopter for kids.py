import turtle,time,random
wn=turtle.Screen()
wn.bgpic('road.gif')
t=turtle.Turtle()
t.up()
imag1=['helicopter11.gif','helicopter12.gif'] 
imag2=['helicopter21.gif','helicopter22.gif']

def helic(img):
    wn.addshape(img)
    t.shape(img)
helic(imag1[0])

turtle.tracer(2)
turtle.bgcolor('brown')
Xposition=0
Yposition=0

t.showturtle()
for i in range (100):
    t.goto(0,Yposition)
    Yposition=Yposition+2
    time.sleep(0.015)
t.hideturtle()

t.goto(0,200)
t.setheading(0)
t.showturtle()
i=0
q=1
    
while True:
    time.sleep(0.05)
    X=t.xcor()
    
    
    i1=i%2
    if q>0:
        helic(imag1[i1])
        t.fd(5)
    i=i+1
    time.sleep(0.02)
    
    if X>=480:
        q=-1
    if q<0:
        helic(imag2[i1])
        t.fd(-5)

    if X<-480:
        q=1
    if q>0:
        helic(imag1[i1])
        t.fd(5)
    
  
        


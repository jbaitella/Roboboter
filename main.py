from ev3robot import *
import time
import threading 


# Initialisierung des Roboters und seiner Komponenten
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)

cs = ColorSensor(SensorPort.S3)
robot.addPart(cs)

us = UltrasonicSensor(SensorPort.S4)
robot.addPart(us)

ts = TouchSensor(SensorPort.S1)
robot.addPart(ts)

# Definition der Geschwindigkeit und des Drehwinkels
geschwindigkeit = 25
drehwinkel = 20
distance = us.getDistance()

#Frequenzen für den Song
G5 = 784
C6 = 1047 
D6 = 1175 
E6 = 1319
A5 = 880 

# Funktionen für die Threads
def color_thread():
    global cs
    while True:
        color_id = cs.getColorID()
        if color_id == 1 or color_id == 2:
           gear.stop()
           gear.backward(400)
           gear.right(15*drehwinkel)


# Funktion zum Abspielen der Melodie
def play_the_song():
    robot.playTone(G5, 500)
    robot.playTone(C6, 500)
    robot.playTone(D6, 500)
    robot.playTone(D6, 1000)
    robot.playTone(E6, 500)
    robot.playTone(D6, 500)
    robot.playTone(C6, 500)
    robot.playTone(A5, 1000)
    robot.playTone(G5, 500)
    robot.playTone(C6, 500)
    robot.playTone(D6, 500)
    robot.playTone(D6, 1000)
    robot.playTone(E6, 500)
    robot.playTone(D6, 500)
    robot.playTone(C6, 500)
    robot.playTone(A5, 1000)
     

# definition des Tanz-Threads
def dance_thread():
        repeat 50:
            gear.left(drehwinkel)
            gear.right(drehwinkel)
            gear.left(500)
            gear.right(500)
            
            
#definition des button-Threads
def button_thread():
     global ts
     while True:
        if ts.isPressed():
            # Starten des Tanz-Threads
            tanz_thread = threading.Thread(target=dance_thread)
            tanz_thread.start()
            # Starten vom Song
            play_the_song()
            # Stoppen des Roboters
            gear.stop()
            robot.exit()

# Starten der color & button Threads
color_thread = threading.Thread(target=color_thread)
color_thread.start()

button_thread = threading.Thread(target=button_thread)
button_thread.start()


while not robot.isEscapeHit():
    #Roboter suchen 
    distance = us.getDistance()
    if distance <= 50:
        gear.setSpeed(5*geschwindigkeit)
        gear.forward(15*distance)
    else:
        gear.right(drehwinkel)

        
# Stoppen des Roboters
gear.stop()
robot.exit()

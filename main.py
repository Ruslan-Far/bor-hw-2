#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
speed = 20
angle = 90

motor_a = Motor(Port.A)
motor_b = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
motor_c = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

def return_to_start_pos_motor_a():
	motor_a.run_until_stalled(100, Stop.COAST, 50)
	motor_a.reset_angle(0)
	wait(2000)
	motor_a.run_target(100, -90)
	motor_a.reset_angle(0)
	wait(2000)

def return_to_start_pos_motor_b():
	motor_b.run_until_stalled(10, Stop.COAST, 50)
	motor_b.reset_angle(0)
	wait(2000)

def return_to_start_pos_motor_c():
	motor_c.run_until_stalled(-10, Stop.COAST, 50)
	motor_c.reset_angle(0)
	wait(2000)
	motor_c.run_target(10, 125)
	motor_c.reset_angle(0)
	wait(2000)

def run_motor(motor, angle):
	ev3.speaker.beep()
	motor.run_target(speed, angle)
	ev3.speaker.beep()

# return_to_start_pos_motor_a()
# return_to_start_pos_motor_b()
# return_to_start_pos_motor_c()
# ev3.speaker.beep(frequency = 1000, duration = 500)

# ---------------------------- Port C
run_motor(motor_c, -angle)
wait(2000)
run_motor(motor_c, 0)
wait(3000)

# ---------------------------- Port B
run_motor(motor_b, -angle)
wait(2000)
run_motor(motor_b, 0)
wait(3000)

# ---------------------------- Port A
run_motor(motor_a, angle)
wait(3000)
run_motor(motor_a, 0)

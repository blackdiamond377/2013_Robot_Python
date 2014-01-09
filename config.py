import wpilib

import drive

from utils import Button

# Joysticks
leftJoy = wpilib.Joystick(1)
rightJoy = wpilib.Joystick(2)

leftMotor = wpilib.Jaguar(1)
rightMotor = wpilib.Jaguar(2)


componets = []


class DriveConfig(object):
    robot_drive = wpilib.RobotDrive(leftMotor, rightMotor)

    drive_joy = rightJoy

    # Buttons
    hs_button = Button(rightJoy, 1)
    sqrd_button = Button(rightJoy, 4)

class ShooterConfig(object):
	shooter_joy = leftJoy
	presets = [Button(leftJoy, x+5) for x in range(6)]
	ss_up_button = Button(leftJoy, 3)
	ss_down_button = Button(leftJoy, 4)

	shooter_motor = wpilib.Jaguar(3)
	lift = wpilib.Talon(4)

	lift_halls = wpilib.Encoder(5, 6)
	shooter_hall = wpilib.Counter(1)
	hall_source = wpilib.CounterPIDSource(shooter_hall)
	
	top_hall = wpilib.DigitalInput(2)
	bottom_hall = wpilib.DigitalInput(3)

	LOADER_COUNT = -195
	LOADER_SPEED = 0

	BACK_COUNT = -294
	BACK_SPEED = .92

	FRONT_COUNT = 0
	FRONT_SPEED = .7

	TOWER_COUNT = -460
	TOWER_SPEED = .365


componets.append(drive.Drive(DriveConfig))
componets.append(shooter.Shooter(ShooterConfig))


# Core Functions
def CheckRestart():
    pass
    # We need to do something about this at some point.....

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

    drive_joy = leftJoy

    # Buttons
    align_button = Button(rightJoy, 3)
    hs_button = Button(leftJoy, 1)

class ShooterConfig(object):
	shooter_joy = leftJoy


componets.append(drive.Drive(DriveConfig))


# Core Functions
def CheckRestart():
    return
    # We need to do something about this at some point.....

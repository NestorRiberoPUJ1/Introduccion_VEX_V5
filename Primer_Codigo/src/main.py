# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Rivar Drone Labs                                             #
# 	Created:      3/15/2024, 6:22:11 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *


class TankDrive():
    def __init__(self):
        self.leftSide=None
        self.rightSide=None

    def config_single_motors(self, leftSide: Motor, rightSide: Motor):
        self.leftSide = leftSide
        self.rightSide = rightSide
    def config_motor_groups(self, leftSide: MotorGroup, rightSide: MotorGroup):
        self.leftSide = leftSide
        self.rightSide = rightSide


# Brain should be defined by default
brain = Brain()

# Robot configuration code
left_drive = Motor(Ports.PORT10, GearSetting.RATIO_36_1, False)
right_drive = Motor(Ports.PORT12, GearSetting.RATIO_36_1, True)

tank_drive = TankDrive()
tank_drive.config_single_motors(left_drive, right_drive)
print(tank_drive.leftSide)

brain.screen.print("Hello V5 from masters")


def pre_autonomous():
    print("PRE-AUTO")


def autonomous():
    print("AUTO")
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Velocity:", "drivetrain.velocity(PERCENT)")
    brain.screen.next_row()


def user_controlled():
    print("DRIVER")
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Velocity:", "drivetrain.velocity(PERCENT)")
    brain.screen.next_row()


comp = Competition(user_controlled, autonomous)
pre_autonomous()

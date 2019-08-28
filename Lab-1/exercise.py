import robot
robot.init()


def swap_left_and_middle():
    robot.drive_right()
    robot.lift_up()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()
    robot.drive_right()
    robot.drive_right()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.drive_left()
    robot.drive_left()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    robot.drive_right()
    robot.drive_right()
    robot.lift_down()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_folded()
    robot.drive_left()
    robot.drive_left()
    robot.drive_left()
    robot.lift_down()
    
    
def swap_right_and_middle():
    robot.drive_right()
    robot.drive_right()
    robot.drive_right()
    robot.drive_right()
    robot.drive_right()
    robot.lift_up()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()
    robot.drive_left()
    robot.drive_left()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.drive_right()
    robot.drive_right()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    robot.drive_left()
    robot.drive_left()
    robot.lift_down()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_folded()
    robot.drive_left()
    robot.drive_left()
    robot.drive_left()
    robot.lift_down()

def swap_left_and_right():
    swap_left_and_middle()
    swap_right_and_middle()
    swap_left_and_middle()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
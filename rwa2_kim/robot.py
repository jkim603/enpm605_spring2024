"""
This module contains the functions that control the robot's movement.
"""

# from maze import maze, OBSTACLE, BOOM
from maze import MAZE_SIZE

# def obstacle_check():
#     global robot_position
#     if maze[robot_position[0]][robot_position[1]] is OBSTACLE:
#         maze[robot_position[0]][robot_position[1]] = BOOM
    
def move_forward(robot_position, robot_orientation):
    """
    TODO: Write documentation and implement this function
    """
    row, col = robot_position
    global MAZE_SIZE
    if robot_orientation == "up":
        if row > 0:
            row -= 1
    elif robot_orientation == "down":
        if row < MAZE_SIZE-1:
            row += 1
    elif robot_orientation == "left":
        if col > 0:
            col -= 1
    elif robot_orientation == "right":
        if col < MAZE_SIZE-1:
            col += 1
    else:
        print("Unknown error occured, try again.")
    robot_position = [row,col]
    return robot_position

def move_backward(robot_position, robot_orientation):
    """
    TODO: Write documentation and implement this function
    """
    row, col = robot_position
    if robot_orientation == "up":
        if row < MAZE_SIZE-1:
            row += 1
    elif robot_orientation == "down":
        if row > 0:
            row -= 1
    elif robot_orientation == "left":
        if col < MAZE_SIZE-1:
            col += 1
    elif robot_orientation == "right":
        if col > 0:
            col -= 1
    else:
        print("Unknown error occured, try again.")
    robot_position = [row,col]
    return robot_position

def turn_left(robot_orientation):
    """
    TODO: Write documentation and implement this function
    """
    if robot_orientation == "up":
        new_orientation = "left"
        ROBOT = "⏪"
    elif robot_orientation == "left":
        new_orientation = "down"
        ROBOT = "⏬"
    elif robot_orientation == "down":
        new_orientation = "right"
        ROBOT = "⏩"
    elif robot_orientation == "right":
        new_orientation = "up"
        ROBOT = "⏫"
    else:
        print("Unknown error occured, try again.")
    return new_orientation, ROBOT

def turn_right(robot_orientation):
    """
    TODO: Write documentation and implement this function
    """
    if robot_orientation == "up":
        new_orientation = "right"
        ROBOT = "⏩"
    elif robot_orientation == "right":
        new_orientation = "down"
        ROBOT = "⏬"
    elif robot_orientation == "down":
        new_orientation = "left"
        ROBOT = "⏪"
    elif robot_orientation == "left":
        new_orientation = "up"
        ROBOT = "⏫"
    else:
        print("Unknown error occured, try again.")
    return new_orientation, ROBOT

def update_robot(action, ROBOT, robot_position, robot_orientation):
    if action == "w":
        robot_position = move_forward(robot_position, robot_orientation)
    elif action == "s":
        robot_position = move_backward(robot_position, robot_orientation)
    elif action == "a":
        robot_orientation, ROBOT = turn_left(robot_orientation)
    elif action == "d":
        robot_orientation, ROBOT = turn_right(robot_orientation)
    return ROBOT, robot_position, robot_orientation
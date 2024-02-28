"""
This module contains the functions that control the robot's movement.
"""

# import maze size so that wall checks will work for any size maze
# import ROBOT to use and update global variable as necessary in functions
from maze import MAZE_SIZE, ROBOT

# create function to move robot forward
def move_forward(robot_position, robot_orientation):
    '''
    This function moves the robot forward in its given orientation as long as there is not a wall in front of the robot.

    Args:
        robot_position (list[int]): The current position of the robot in the maze.
        robot_orientation (str): The current orientation of the robot.

    Returns:
        robot_position(list[int]): The updated position of the robot in the maze.
    '''
    # pull row and col out of robot position in order to update values
    row, col = robot_position
    # use global variable for maze size
    global MAZE_SIZE
    # if robot orientation is up, subtract 1 from row to redefine robot position as one row up
    if robot_orientation == "up":
        # only move the robot if it will not drive off the maze (into a wall)
        if row > 0:
            row -= 1
    # if the robot orientation is down, add 1 to row to redefine robot posiiton as one row down
    elif robot_orientation == "down":
        # only move the robot if it will not drive off the maze (into a wall)
        if row < MAZE_SIZE-1:
            row += 1
    # if the robot orientation is left, subtract 1 from col to redefine robot position as one col to the left
    elif robot_orientation == "left":
        # only move the robot if it will not drive off the maze (into a wall)
        if col > 0:
            col -= 1
    # if the robot orientation is right, add 1 to col to redefine robot position as one col to the right
    elif robot_orientation == "right":
        # only move the robot if it will not drive off the maze (into a wall)
        if col < MAZE_SIZE-1:
            col += 1
    # print error message if for some reason all conditional statements above are skipped (this should not occur)
    else:
        print("Unknown error occured, try again.")
    # redfine robot position with the updated row/col value
    robot_position = [row,col]
    # return the new robot position  (note that this will be unchanged if the robot is facing a wall)
    return robot_position

# create function to move robot backward
def move_backward(robot_position, robot_orientation):
    '''
    This function moves the robot backward in its given orientation as long as there is not a wall behind the robot.

    Args:
        robot_position (list[int]): The current position of the robot in the maze.
        robot_orientation (str): The current orientation of the robot.

    Returns:
        robot_position (list[int]): The updated position of the robot in the maze.
    '''
    # pull row and col out of robot position in order to update values
    row, col = robot_position
    # use global variable for maze size
    global MAZE_SIZE
    # if robot orientation is up, add 1 to row to redefine robot position as one row down
    if robot_orientation == "up":
        # only move the robot if it will not drive off the maze (into a wall)
        if row < MAZE_SIZE-1:
            row += 1
    # if the robot orientation is down, subtract 1 from row to redefine robot posiiton as one row up
    elif robot_orientation == "down":
        # only move the robot if it will not drive off the maze (into a wall)
        if row > 0:
            row -= 1
    # if the robot orientation is left, add 1 to col to redefine robot position as one col to the right
    elif robot_orientation == "left":
        # only move the robot if it will not drive off the maze (into a wall)
        if col < MAZE_SIZE-1:
            col += 1
    # if the robot orientation is right, subtract 1 from col to redefine robot position as one col to the left
    elif robot_orientation == "right":
        # only move the robot if it will not drive off the maze (into a wall)
        if col > 0:
            col -= 1
    # print error message if for some reason all conditional statements above are skipped (this should not occur)
    else:
        print("Unknown error occured, try again.")
    # redfine robot position with the updated row/col value
    robot_position = [row,col]
    # return the new robot position  (note that this will be unchanged if the robot is backed up to a wall)
    return robot_position

# create function to turn robot left
def turn_left(robot_orientation):
    '''
    This function turns the robot left from its current orientation.

    Args:
        robot_orientation (str): The current orientation of the robot.

    Returns:
        new_orientation (str): The updated orientation of the robot.
        ROBOT (str): The updated emoji showing robot orientation in the maze.
    '''
    # if current orientation is up, redefine orientation to left
    if robot_orientation == "up":
        new_orientation = "left"
        # update robot emoji to show left arrow in maze
        ROBOT = "⏪"
    # if current orientation is left, redefine orientation to down
    elif robot_orientation == "left":
        new_orientation = "down"
        # update robot emoji to show down arrow in maze
        ROBOT = "⏬"
    # if current orientation is down, redefine orientation to right
    elif robot_orientation == "down":
        new_orientation = "right"
        # update robot emoji to show right arrow in maze
        ROBOT = "⏩"
    # if current orientation is right, redefine orientation to up
    elif robot_orientation == "right":
        new_orientation = "up"
        # update robot emoji to show up arrow in maze
        ROBOT = "⏫"
    # print error message if for some reason all conditional statements above are skipped (this should not occur)
    else:
        print("Unknown error occured, try again.")
    # return new orientation and robot emoji
    return new_orientation, ROBOT

# create function to turn robot right
def turn_right(robot_orientation):
    '''
    This function turns the robot right from its current orientation.

    Args:
        robot_orientation (str): The current orientation of the robot.

    Returns:
        new_orientation (str): The updated orientation of the robot.
        ROBOT (str): The updated emoji showing robot orientation in the maze.
    '''
    # if current orientation is up, redefine orientation to right
    if robot_orientation == "up":
        new_orientation = "right"
        # update robot emoji to show right arrow in maze
        ROBOT = "⏩"
    # if current orientation is right, redefine orientation to down
    elif robot_orientation == "right":
        new_orientation = "down"
        # update robot emoji to show down arrow in maze
        ROBOT = "⏬"
    # if current orientation is down, redefine orientation to left
    elif robot_orientation == "down":
        new_orientation = "left"
        # update robot emoji to show left arrow in maze
        ROBOT = "⏪"
    # if current orientation is left, redefine orientation to up
    elif robot_orientation == "left":
        new_orientation = "up"
        # update robot emoji to show up arrow in maze
        ROBOT = "⏫"
    # print error message if for some reason all conditional statements above are skipped (this should not occur)
    else:
        print("Unknown error occured, try again.")
    # return new orientation and robot emoji
    return new_orientation, ROBOT

# create function to move/update the robot depending on given action
def update_robot(action, robot_position, robot_orientation):
    '''
    This function updates the robot position and orientation based on the action given by the user.

    Args:
        action (str): User input directing movement and turning of robot based on 'wasd' controls.
        robot_position (list[int]): The current position of the robot in the maze.
        robot_orientation (str): The current orientation of the robot.
        
    Returns:
        ROBOT (str): Emoji representing robot's orientation after completing action.
        robot_position(list[int]): The position of robot after completing action.
        robot_orientation (str): The orientation of robot after completing action.
    '''
    # use global ROBOT to update, or output existing if no orientation change
    global ROBOT
    # if action input is w, move the robot forward
    if action == "w":
        robot_position = move_forward(robot_position, robot_orientation)
    # if action input is s, move the robot backward
    elif action == "s":
        robot_position = move_backward(robot_position, robot_orientation)
    # if action input is a, turn the robot left in place
    elif action == "a":
        robot_orientation, ROBOT = turn_left(robot_orientation)
    # if action input is d, turn the robot right in place
    elif action == "d":
        robot_orientation, ROBOT = turn_right(robot_orientation)
    # return updated robot parameters
    return ROBOT, robot_position, robot_orientation
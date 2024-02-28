"""
This is the main file which contains the entry point of your program.
"""

# import necessary functions and variables
from maze import print_maze
from maze import ROBOT, EMPTY, OBSTACLE, BOOM, GOAL
from maze import robot_position, robot_orientation, goal_position, maze
from robot import update_robot

def main():
    '''
    This program runs the robot maze game. It queries the user for action inputs and updates and displays the maze accordingly.
    '''
    # print the initial maze defined in maze.py
    print("Initial Maze:")
    print_maze()
    
    # open loop to query user for action inputs
    while True:
        # define actions and get input
        action = input("Enter action (w: forward, s: backward, a: left, d: right, q: quit): ")
        # check if action is within valid options
        if action not in ["w","a","s","d","q"]:
            # tell user they have given invalid input, ask to try again
            print("\nInvalid action given, please try again.\n")
            # restart input query loop
            continue
        # check if action is quit, then display a message and break the loop to end program
        elif action == "q":
            print("\nQuitting the maze game. Have a nice day!\n")
            break
        
        # use global variables to update robot position and orientation
        global EMPTY, robot_position, robot_orientation, maze
        # set old robot position to display as an empty spot on maze
        maze[robot_position[0]][robot_position[1]] = EMPTY
        # get new robot position and orientation depending on action
        ROBOT, robot_position, robot_orientation = update_robot(action, robot_position, robot_orientation)
        
        # check if new robot position hits an obstacle
        if maze[robot_position[0]][robot_position[1]] is OBSTACLE:
            # if robot hits obstacle, update maze to show explosion
            maze[robot_position[0]][robot_position[1]] = BOOM
            # tell user they have hit an obstacle and it is game over
            print("\nOh no! You hit an obstacle and the robot exploded! Better luck next time...")
            # create boolean that will be used to end program after printing maze
            end_check = True
        # check if new robot position is the goal
        elif maze[robot_position[0]][robot_position[1]] is GOAL:
            # if robot reaches goal, update maze to show the robot where the flag used to be
            maze[robot_position[0]][robot_position[1]] = ROBOT
            # tell user they have won the game
            print("\nGoal reached! Congratulations! You won!!!")
            # create boolean that will be used to end program after maze is printed
            end_check = True
        # if robot did not hit obstacle or reach goal, update maze to show new robot position and orientation
        else:
            # show robot in its new position and orientation in maze
            maze[robot_position[0]][robot_position[1]] = ROBOT
            # create boolean that will be used to continue program after maze is printed
            end_check = False

        # print the new maze after action is completed
        print_maze()
        # end the program if the robot hit an obstacle or reached the goal
        if end_check is True:
            break
        # continue program if robot has not hit obstacle or reached goal
        else:
            continue


# Run the main function
if __name__ == "__main__":
    main()

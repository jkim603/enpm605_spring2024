"""
This is the main file which contains the entry point of your program.
"""

# import necessary functions and variables
from maze import print_maze
from maze import ROBOT, EMPTY, OBSTACLE, BOOM, GOAL
from maze import robot_position, robot_orientation, goal_position, maze
from robot import update_robot

# def obstacle_goal_check():
#     global robot_position, OBSTACLE, BOOM, GOAL
#     if maze[robot_position[0]][robot_position[1]] == OBSTACLE:
#         maze[robot_position[0]][robot_position[1]] = BOOM
#         print("Oh no! You hit an obstacle and the robot exploded!")
#         return True
#     elif maze[robot_position[0]][robot_position[1]] == GOAL:
#         print("Goal reached! Congratulations! You won!!!")
#         return True
#     else:
#         return False

def main():
    print("Initial Maze:")
    print_maze()
    while True:
        action = input("Enter action (w: forward, s: backward, a: left, d: right, q: quit): ")
        # TODO write the main function
        if action not in ["w","a","s","d","q"]:
            print("\nInvalid action given, please try again.\n")
            continue
        elif action == "q":
            print("\nQuitting the maze game. Have a nice day!\n")
            break
        global ROBOT, EMPTY, robot_position, robot_orientation, maze
        maze[robot_position[0]][robot_position[1]] = EMPTY
        ROBOT, robot_position, robot_orientation = update_robot(action, ROBOT, robot_position, robot_orientation)
        if maze[robot_position[0]][robot_position[1]] is OBSTACLE:
            maze[robot_position[0]][robot_position[1]] = BOOM
            print("\nOh no! You hit an obstacle and the robot exploded!")
            end_check = True
        elif maze[robot_position[0]][robot_position[1]] is GOAL:
            maze[robot_position[0]][robot_position[1]] = ROBOT
            print("\nGoal reached! Congratulations! You won!!!")
            end_check = True
        else:
            maze[robot_position[0]][robot_position[1]] = ROBOT
            end_check = False
        # stop_check = obstacle_goal_check()
        # if stop_check is True:
            # break
        # Ctrl-c to stop the program
        print_maze()
        if end_check is True:
            break


# Run the main function
if __name__ == "__main__":
    main()

"""
This module contains the maze and the robot's initial position, as well as functions to print the maze and move the robot.
"""

# import random number generator to randomize start positions
import random

# Constants
# Here are all the emojis: "💥", "🏁", "⏫", "⏩", "⏪", "⏬", "🚧"
EMPTY = "  "
BOOM = "💥"
OBSTACLE = "🚧"
GOAL = "🏁"
ROBOT = "⏫"
HORIZONTAL_WALL = "──"
VERTICAL_WALL = "│"
CORNER = "┼"

# Define the size of the maze
MAZE_SIZE = 4

# Define the maze as a 2D list
maze = [[EMPTY] * MAZE_SIZE for _ in range(MAZE_SIZE)]
# Rewrite the previous line using for loops

# Define the obstacles' positions
obstacle_positions = [[1, 1], [2, 2], [3, 3]]

# Define the robot's initial position
while True:
    # randomize start position
    x = random.choice(range(MAZE_SIZE))
    y = random.choice(range(MAZE_SIZE))
    # check if start position in obstacle
    if [x,y] in obstacle_positions:
        # rerandomize start if in obstacle
        continue
    # if not in obstacle, accept random start by breaking loop
    else:
        break
# set robot position as the random x,y values
robot_position = [x, y]  # [row, column]
robot_orientation = random.choice(["up","down","left","right"])
# set robot emoji to match randomized orientation
if robot_orientation == "up":
    ROBOT = "⏫"
elif robot_orientation == "right":
    ROBOT = "⏩"
elif robot_orientation == "down":
    ROBOT = "⏬"
elif robot_orientation == "left":
    ROBOT = "⏪"

# Define the goal position
while True:
    # randomize goal position
    xx = random.choice(range(MAZE_SIZE))
    yy = random.choice(range(MAZE_SIZE))
    # check if random goal in obstacle
    if [xx,yy] in obstacle_positions:
        # rerandomize goal if in obstacle
        continue
    # check if goal is robot position
    if [xx,yy] == robot_position:
        # rerandomize goal if is robot start position
        continue
    # if not in obstacle or robot start, accept goal position by breaking loop
    else:
        break
# set goal position as the random xx,yy values
goal_position = [xx,yy]

# Place obstacles, the robot, and the goal in the maze
for obstacle in obstacle_positions:
    maze[obstacle[0]][obstacle[1]] = OBSTACLE

maze[robot_position[0]][robot_position[1]] = ROBOT
maze[goal_position[0]][goal_position[1]] = GOAL


# Function to print the maze
def print_maze():
    # Print top boundary
    print("┌" + "─" * (MAZE_SIZE * 3 - 1) + "┐")

    for i, row in enumerate(maze):
        # Print left boundary
        print(VERTICAL_WALL, end="")

        # Print cell contents
        for j, cell in enumerate(row):
            print(cell, end="")
            # Print vertical wall if not in the last column
            if j < MAZE_SIZE - 1:
                print(VERTICAL_WALL, end="")

        # Print right boundary
        print(VERTICAL_WALL)

        # Print horizontal wall between rows (except for the last row)
        if i < MAZE_SIZE - 1:
            print("├" + "─" * (MAZE_SIZE * 3 - 1) + "┤")

    # Print bottom boundary
    print("└" + "─" * (MAZE_SIZE * 3 - 1) + "┘")

if __name__ == "__main__":
    print_maze()
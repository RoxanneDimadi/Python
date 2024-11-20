# lab 04
from Stack import Stack


def solveMaze(maze, startX, startY):
    s = Stack()
    s.push([startX, startY])
    counter = 0

    while s.isEmpty() == False:
        locationX = s.peek()[0]
        locationY = s.peek()[1]

        if type(maze[locationX][locationY]) != int:
            counter += 1
            maze[locationX][locationY] = counter

        # north
        if maze[locationX - 1][locationY] == 'G':
            return True
        elif maze[locationX - 1][locationY] == ' ':
            s.push([locationX - 1, locationY])
            continue

        # West
        if maze[locationX][locationY - 1] == 'G':
            return True
        elif maze[locationX][locationY - 1] == ' ':
            s.push([locationX, locationY - 1])
            continue
        # South
        if maze[locationX + 1][locationY] == 'G':
            return True
        elif maze[locationX + 1][locationY] == ' ':
            s.push([locationX + 1, locationY])
            continue

            # East
        if maze[locationX][locationY + 1] == 'G':
            return True
        elif maze[locationX][locationY + 1] == ' ':
            s.push([locationX, locationY + 1])
            continue

        s.pop()

    return False


def printMaze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            print("|{:<2}".format(maze[row][col]), sep='', end='')
        print("|")
    return


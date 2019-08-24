import numpy as np

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

UNOCCUPIED = 1
OCCUPIED   = -1
FOOD       = 1
HEAD       = -2
HUNT      = 1


TAIL       = 4
HEALTHLIM = 100
game_state = ""
directions = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
def calculate_move(new_board, game_state):
    find_food(game_state, new_board)
    print(max(directions, key=lambda k: directions[k]))
    print("UP", directions["up"])
    print("DOWN", directions["down"])
    print("LEFT", directions["left"])
    print("RIGHT", directions["right"])
    return max(directions, key=lambda k: directions[k])

def find_food(game_state, board_matrix ):
    minsum = 1000
    y = game_state['you']["body"][0]["y"]
    x = game_state['you']["body"][0]["x"]
    directions["up"] = 0
    directions["down"] = 0
    directions["left"] = 0
    directions["right"] = 0

    for food in game_state["board"]["food"]:
        tot = abs(food['x'] - x)
        tot += abs(food['y'] - y)
        if (tot < minsum):
            goodfood = food
            minsum = tot

    find_path(game_state, board_matrix,x,y, goodfood["x"], goodfood['y'])


def find_path(game_state, board_matrix, x, y, foodx, foody):
    height = game_state["board"]["height"]
    grid = Grid(width=height, height=height, matrix=board_matrix)
    start = grid.node(x, y)
    end = grid.node(foodx, foody)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    if (len(path) > 0):
        pathx = path[1][0]
        pathy = path[1][1]

        y = game_state['you']["body"][0]["y"]
        x = game_state['you']["body"][0]["x"]
        # go up
        if ((y - 1) == pathy) and (x == pathx):
            directions["up"] += 20
            print("Pick: UP")
        # go down
        if ((y + 1) == pathy) and (x == pathx):
            directions["down"] += 20
            print("Pick: down")
        # go left
        if ((x - 1) == pathx) and (y == pathy):
            directions["left"] += 20
            print("Pick: left")
        # go right
        if ((x + 1) == pathx) and (y == pathy):
            directions["right"] += 20
            print("Pick: right")

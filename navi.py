from maze import *
from exception import *
from stack import Stack

class PacMan:
    navigator_maze = []
    def __init__(self, grid):
        self.navigator_maze = grid.grid_representation
    
    def valid_path(self, position):
        x, y = position
        if x < 0 or y < 0 or x >= len(self.navigator_maze) or y >= len(self.navigator_maze[0]):
            return False
        return self.navigator_maze[x][y] == 0
    
    def find_path(self, start, end):
        stack = Stack()
        stack.push((start, [start]))
        
        visited = []
        visited.append(start)

        while not stack.isempty():
            current_position, path = stack.pop()

            if current_position == end:
                return path

            x, y = current_position
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_position = (x + dx, y + dy)

                if new_position not in visited and self.valid_path(new_position):
                    visited.append(new_position)
                    stack.push((new_position, path + [new_position]))

        raise PathNotFoundException

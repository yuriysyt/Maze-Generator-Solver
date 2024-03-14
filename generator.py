import pygame
import random
from config import *
from solver import MazeSolver

class MazeGenerator:

    def __init__(self):
        #Creating immutable variables, which we use in our algorithms
        self.generating = True
        #Creating instructions, which the agent follows
        # Sequence:
        self.DIRECTIONS = [(2, 0), (0, 2), (-2, 0), (0, -2)]

        #Initialize screens and  parametrs for this
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Maze Generator")

        #Create range of maze
        self.maze = []

        # It is calculation for draw all black pixels
        for _ in range(2 *MAZE_HEIGHT + 3):
            # Create all maze using symbols
            row = ['1'] * (2 *MAZE_WIDTH + 3)
            self.maze.append(row)

        # Create a set of visited cells
        self.visited = set()
        
        #Creating starting point
        self.agent_x, self.agent_y = 1, 1
        self.visited.add((self.agent_x, self.agent_y))
        
        
    #Check for valid (within or out of maze)
    #Input position x and y
    #Output: True or False

    def is_valid(self, x, y):
        return 0 <= x < 2 * MAZE_HEIGHT + 3 and 0 <= y < 2 * MAZE_WIDTH + 3
    
    #Check if point unvisit
    def is_unvisited(self, x, y):
        return (x, y) not in self.visited
    
    #Change black pixel to white pixel
    def break_wall(self, x1, y1, x2, y2):
        self.maze[x1 + x2 // 2][y1 + y2 // 2] = ' '


    #Loop for maze generation
    def generate_maze(self):
        running = True
        stack = [(self.agent_x, self.agent_y)]
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            #Clear the screen
            self.screen.fill(COLOR_WHITE)
            self.exit_x, self.exit_y = 2 * MAZE_HEIGHT + 1, 2 * MAZE_WIDTH + 1  # Point of exit x and y
            #Change '1' to 'E'
            self.maze[self.exit_x][self.exit_y] = 'E'
            #Draw maze
            for i, row in enumerate(self.maze):
                for j, cell in enumerate(row):
                    if cell == '1': #Change black pixel to white pixel
                        pygame.draw.rect(self.screen, COLOR_BLACK, (j *CELL_SIZE, i *CELL_SIZE,CELL_SIZE,CELL_SIZE))
                    elif cell == 'E': #Draw exit point
                        pygame.draw.rect(self.screen, COLOR_RED, (j *CELL_SIZE, i *CELL_SIZE,CELL_SIZE,CELL_SIZE))
                        
            
            #Move agent, when we have dirty area. 
            # If we don't have, green rectangle will stop
            if stack:
                #Draw green rectangle (Position of agent)
                pygame.draw.rect(self.screen, COLOR_GREEN, (self.agent_y *CELL_SIZE, self.agent_x *CELL_SIZE,CELL_SIZE,CELL_SIZE))
                pygame.display.flip()
            
            #Store the coordinates
            x, y = self.agent_x, self.agent_y
            #Mark current cell as visited by adding to set
            self.visited.add((x, y))
            #Set the cell in the 'maze' to empty
            self.maze[x][y] = ' '

            unvisited_neighbors = []
            for dx, dy in self.DIRECTIONS:
                # Calculate the new coordinates
                new_x, new_y = x + dx, y + dy
                # Check that the new coordinates are inside the maze and the cell has not been visited yet..
                if self.is_valid(new_x, new_y) and self.is_unvisited(new_x, new_y):
                    unvisited_neighbors.append((new_x, new_y))

            if unvisited_neighbors:
                #Random choose coordinates of your maze
                nx, ny = random.choice(unvisited_neighbors)
                #Replace black pixel to white pixel
                self.break_wall(x, y, nx - x, ny - y)
                #Added
                stack.append((nx, ny))
                self.agent_x, self.agent_y = nx, ny
            elif stack:
                #Delete last element from stack
                self.agent_x, self.agent_y = stack.pop()
                 # Terminate when the stack is empty
                end = (self.exit_x, self.exit_y)  
            else:
                print('end')
                end = (self.exit_x, self.exit_y)   
                running = False    
                MazeSolver().solve(self.maze, end)

if __name__ == "__main__":
    MazeGenerator().generate_maze()
    pygame.quit()
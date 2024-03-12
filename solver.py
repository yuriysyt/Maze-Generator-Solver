import pygame 
import heapq

from config import *

#end = (self.exit_x, self.exit_y)       
# MazeSolver().solve(self.maze, end) 

class MazeSolver():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start = (1, 1)
    end = ()
    distances = {}

    def maze_to_graph(self, maze):
        graph = {}
        rows = len(maze)
        cols = len(maze[0])
        
        for i in range(rows):
            for j in range(cols):
                if maze[i][j] != '1':
                    neighbors = []
                    for dx, dy in self.directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < rows and 0 <= y < cols and maze[x][y] != '1':
                            neighbors.append((x, y))
                    graph[(i, j)] = neighbors
        
        return graph


    def custom_dijkstra(self, custom_graph, custom_start, custom_end):
        self.custom_distances = {custom_node: float('inf') for custom_node in custom_graph}
        self.custom_distances[custom_start] = 0
        custom_queue = [(0, custom_start)]

        while custom_queue:
            custom_distance, custom_node = heapq.heappop(custom_queue)

            if custom_node == custom_end:
                break

            if custom_distance > self.custom_distances[custom_node]:
                continue

            for custom_neighbor in custom_graph[custom_node]:
                custom_distance = custom_distance + 1 
                if custom_distance < self.custom_distances[custom_neighbor]:
                    self.custom_distances[custom_neighbor] = custom_distance
                    heapq.heappush(custom_queue, (custom_distance, custom_neighbor))
    
    def find_shortest_path(self, graph, start, end):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        previous_nodes = {}

        queue = [(0, start)]

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                path = []
                while current_node in previous_nodes:
                    path.insert(0, current_node)
                    current_node = previous_nodes[current_node]
                path.insert(0, start)
                return path

            if current_distance > distances[current_node]:
                continue

            for neighbor in graph[current_node]:
                distance = current_distance + 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))


    def visualize_path(self, maze, path):

        pygame.init()
        window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('fff')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            window.fill(COLOR_WHITE)

            for y in range(len(maze)):
                for x in range(len(maze[y])):
                    if maze[y][x] == '1':
                        pygame.draw.rect(window, COLOR_BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            for node in path:
                x, y = node
                pygame.draw.rect(window, COLOR_GREEN, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            pygame.display.flip()

        pygame.quit()

    def solve (self, maze, end):
        graph = self.maze_to_graph(maze)
        self.end = end
        shortest_path = self.find_shortest_path(graph, self.start, self.end)

        print("Shortest path:", shortest_path)
        self.visualize_path(maze, shortest_path)
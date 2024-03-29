# Maze Generator and Solver

## Introduction

This repository contains Python scripts for maze generation and solving. The `generator.py` script creates a maze using a randomized depth-first search algorithm, and the `solver.py` script utilizes Dijkstra's algorithm to find the shortest path from the starting point to the exit.

## Maze Generator (`generator.py`)

![Generator Picture](https://github.com/yuriysyt/Maze-Generator-Solver/raw/main/readme_images/Generator.png)

Creates mazes using a simple algorithm. It employs a depth-first search technique to generate a maze layout, starting from a designated entrance point and ending at a defined exit. As the script executes, it visualizes the maze generation process using the Pygame library, creating a graphical representation of the maze as it progresses. The generated maze consists of pathways and walls, forming a complex network of corridors. Once the maze generation is complete, the resulting maze can be explored interactively or utilized for various purposes, such as gaming or algorithm testing.

### Usage

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Generator:**
   ```bash
   python generator.py
   ```

3. Follow on-screen instructions to watch the maze being generated.

## Maze Solver (`solver.py`)

![Generator Picture](https://github.com/yuriysyt/Maze-Generator-Solver/raw/main/readme_images/Solver.png)

Once the maze has been generated, the solver.py script takes on the challenge of finding the shortest path from the starting point to the exit. Using Dijkstra's algorithm, it intelligently navigates through the maze's corridors, determining the most efficient route. The solver's final output is the discovered shortest path, providing a clear solution to the maze's intricate layout.

## Configuration (`config.py`)

Adjustable parameters for screen dimensions, cell size, maze dimensions, and colors are defined in `config.py`.

### Configuration Parameters

- `SCREEN_WIDTH`, `SCREEN_HEIGHT`: Screen dimensions.
- `CELL_SIZE`: Size of each maze cell.
- `COLOR_WHITE`, `COLOR_BLACK`, `COLOR_GREEN`, `COLOR_RED`: Color constants.
- `MAZE_WIDTH`, `MAZE_HEIGHT`: Dimensions of the maze.

Feel free to experiment with these parameters to customize the maze generation and solving experience!

---

**Note:** Make sure to run the generator before the solver for a seamless experience. The generated maze will be solved, and the shortest path will be displayed.

Enjoy exploring mazes with this simple Python project!
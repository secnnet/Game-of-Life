# Conway's Game of Life

This script is an implementation of Conway's Game of Life, a cellular automaton devised by John Conway. The Game of Life is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input from human players.
The script creates a grid of cells, where each cell is either alive (1) or dead (0), and updates the grid according to the rules of the game. It displays the grid in the terminal or console, with live cells represented by '#' and dead cells by '.'. The simulation runs for a specified number of generations, and the grid is updated and displayed for each generation.

Here's a brief explanation of the functions in the script:
  1. create_grid(rows, cols): Creates a grid of given dimensions and randomly initializes the cells.
  2. display_grid(grid): Displays the grid in the terminal or console.
  3. get_neighbours(x, y, grid): Retrieves the neighbours of a given cell in the grid.
  4. next_generation(grid): Computes the next generation of the grid based on the rules of Conway's Game of Life.
  5. run_game_of_life(rows, cols, generations, sleep_time=0.1): Runs the Game of Life simulation with specified parameters.

To run the script, follow these steps:
  1. Save the script as a Python file with the .py extension, for example, conways_game_of_life.py.
  2. Open a terminal or command prompt.
  3. Navigate to the directory containing the saved file.
  4. Run the following command: python conways_game_of_life.py.

This command will execute the script and run Conway's Game of Life simulation using the parameters defined in the run_game_of_life() function call at the end of the script.

import os
import time
import random

# Create a grid with given rows and columns and randomly initialize cells as alive (1) or dead (0)
def create_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

# Display the grid in the terminal/console, using '#' for live cells and '.' for dead cells
def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join(['#' if cell else '.' for cell in row]))

# Get the neighbours of a given cell (x, y) in the grid
def get_neighbours(x, y, grid):
    rows, cols = len(grid), len(grid[0])
    neighbours = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:  # Skip the current cell
                continue
            nx, ny = x + dx, y + dy
            # Check if the neighbour's coordinates are within the grid
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbours.append(grid[nx][ny])
    return neighbours

# Compute the next generation of the grid based on the rules of Conway's Game of Life
def next_generation(grid):
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            neighbours = get_neighbours(i, j, grid)
            live_neighbours = sum(neighbours)
            # Apply the rules to determine the state of the cell in the next generation
            if cell and live_neighbours in [2, 3]:
                new_grid[i][j] = 1
            elif not cell and live_neighbours == 3:
                new_grid[i][j] = 1
    return new_grid

# Run the Game of Life simulation with the specified parameters
def run_game_of_life(rows, cols, generations, sleep_time=0.1):
    grid = create_grid(rows, cols)
    for _ in range(generations):
        display_grid(grid)
        grid = next_generation(grid)
        time.sleep(sleep_time)  # Pause between generations

# Entry point for the script
if __name__ == '__main__':
    run_game_of_life(rows=30, cols=60, generations=100)

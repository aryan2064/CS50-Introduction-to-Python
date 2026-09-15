# Maze Solver (DFS/BFS)
#### Video Demo: https://youtu.be/jtJC2tsamjk
#### Description:

This is my final project for CS50's Introduction to Programming with Python. It's a command line maze solver. You can use the default maze or type in your own, then pick DFS or BFS to find a path from start to end. The maze is printed to the terminal, and if a path is found, it's shown marked with `*`.

A maze is just a 2D list where `S` is the start, `E` is the end, `0` is an open path, and `1` is a wall. When making a custom maze, you type each row as a string like `S0100E`.

## Files

- **project.py** — has all the logic:
  - `main()` runs the program.
  - `choose_maze()` and `create_custom_maze()` handle picking or building a maze.
  - `find_start_end()` finds the `S` and `E` positions.
  - `get_neighbors()` returns the open neighboring cells.
  - `dfs()` and `bfs()` search for a path using a stack and a queue.
  - `print_maze()` prints the maze, with the path highlighted if there is one.

- **test_project.py** — tests for `find_start_end`, `get_neighbors`, `bfs`, and `dfs`, covering normal paths, missing start/end, no path existing, and the start/end being the same cell.

## Notes

I kept the maze as a plain 2D list instead of making a class, since it was simple enough not to need one. DFS and BFS are separate functions rather than one function with a flag, since a stack and a queue work differently enough that combining them wasn't worth it. Invalid characters in a custom maze just get treated as `0` instead of rejecting the whole maze, so a typo doesn't crash the program.

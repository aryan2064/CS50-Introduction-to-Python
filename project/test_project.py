from project import (
    default_maze,
    find_start_end,
    get_neighbors,
    dfs,
    bfs,
)



def test_find_start_end():
    grid = [
        ["S", 0, 1],
        [0, 0, 1],
        [1, 0, "E"]
    ]
    start, end = find_start_end(grid)
    assert start == (0, 0)
    assert end == (2, 2)



def test_find_start_end_missing_start():
    grid = [
        [0, 0, 1],
        [0, 0, 1],
        [1, 0, "E"]
    ]
    start, end = find_start_end(grid)
    assert start is None
    assert end == (2, 2)



def test_find_start_end_missing_end():
    grid = [
        ["S", 0, 1],
        [0, 0, 1],
        [1, 0, 0]
    ]
    start, end = find_start_end(grid)
    assert start == (0, 0)
    assert end is None



def test_get_neighbors():
    grid = [
        ["S", 0, 1],
        [0, 0, 1],
        [1, 0, "E"]
    ]
    neighbors = get_neighbors((0, 0), 3, 3, grid)
    assert set(neighbors) == {(0, 1), (1, 0)}



def test_get_neighbors_wall():
    grid = [
        ["S", 1],
        [0, "E"]
    ]
    neighbors = get_neighbors((0, 0), 2, 2, grid)
    assert neighbors == [(1, 0)]



def test_get_neighbors_corner():
    grid = [
        ["S", 0],
        [0, "E"]
    ]
    neighbors = get_neighbors((0, 0), 2, 2, grid)
    assert set(neighbors) == {(0, 1), (1, 0)}



def test_bfs():
    grid = [
        ["S", 0, 0],
        [1, 1, 0],
        [0, 0, "E"]
    ]
    start, end = find_start_end(grid)
    path = bfs(start, end, grid)
    assert path is not None
    assert path[0] == start
    assert path[-1] == end



def test_bfs_no_path():
    grid = [
        ["S", 1, 0],
        [1, 1, 1],
        [0, 1, "E"]
    ]
    start, end = find_start_end(grid)
    path = bfs(start, end, grid)
    assert path is None



def test_bfs_shortest_path():
    grid = [
        ["S", 0, 0],
        [0, 1, 0],
        [0, 0, "E"]
    ]
    start, end = find_start_end(grid)
    path = bfs(start, end, grid)
    assert path is not None
    assert len(path) - 1 == 4



def test_bfs_start_is_end():
    grid = [
        ["S"]
    ]

    path = bfs((0, 0), (0, 0), grid)
    assert path == [(0, 0)]



def test_dfs():
    grid = [
        ["S", 0, 0],
        [1, 1, 0],
        [0, 0, "E"]
    ]
    start, end = find_start_end(grid)
    path = dfs(start, end, grid)
    assert path is not None
    assert path[0] == start
    assert path[-1] == end



def test_dfs_no_path():
    grid = [
        ["S", 1, 0],
        [1, 1, 1],
        [0, 1, "E"]
    ]
    start, end = find_start_end(grid)
    path = dfs(start, end, grid)
    assert path is None



def test_dfs_start_is_end():
    grid = [
        ["S"]
    ]
    path = dfs((0, 0), (0, 0), grid)
    assert path == [(0, 0)]



def test_default_maze_has_start_and_end():
    start, end = find_start_end(default_maze)

    assert start is not None
    assert end is not None


def test_default_maze_bfs():
    start, end = find_start_end(default_maze)

    path = bfs(start, end, default_maze)

    assert path is not None
    assert path[0] == start
    assert path[-1] == end



def test_default_maze_dfs():
    start, end = find_start_end(default_maze)

    path = dfs(start, end, default_maze)

    assert path is not None
    assert path[0] == start
    assert path[-1] == end

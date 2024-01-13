def explore_maze(maze, rat_position, destination, visited):
    x, y = rat_position

    # Base case: rat reaches the destination
    if rat_position == destination:
        return True

    # Mark the current position as visited
    visited[x][y] = True

    # Define possible movements: up, down, left, right
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in movements:
        new_x, new_y = x + dx, y + dy

        # Check if the new position is valid
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 0 and not visited[new_x][new_y]:
            # Move to the new position
            if explore_maze(maze, (new_x, new_y), destination, visited):
                # Path found, return True
                return True

    # No valid movements, backtrack
    visited[x][y] = False
    return False

# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_position = (0, 0)
end_position = (4, 4)
visited_cells = [[False] * len(maze[0]) for _ in range(len(maze))]

result = explore_maze(maze, start_position, end_position, visited_cells)

if result:
    print("Path found!")
else:
    print("No path found.")

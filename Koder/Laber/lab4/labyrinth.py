def rotate(grid, clockwise):
    rows, cols = len(grid), len(grid[0])  
    

    rotated_grid = [[None] * rows for _ in range(cols)]
    
    for r in range(rows):
        for c in range(cols):
            if clockwise:
                rotated_grid[c][rows - 1 - r] = grid[r][c]  
            else:
                rotated_grid[cols - 1 - c][r] = grid[r][c]  
    
    return rotated_grid  

if __name__ == '__main__':
    import labyrinth_test
    labyrinth_test.run_all()
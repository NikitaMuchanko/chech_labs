def fill_spiral(n):
    grid = [[0]*n for _ in range(n)]
    current_num = 1
    start_x, end_x, start_y, end_y = 0, n-1, 0, n-1
    
    while True:
        if start_x > end_x or start_y > end_y:
            break
        
        for x in range(start_x, end_x+1):
            grid[start_y][x] = current_num
            current_num += 1
        for y in range(start_y+1, end_y+1):
            grid[y][end_x] = current_num
            current_num += 1
        for x in range(end_x-1, start_x-1, -1):
            grid[end_y][x] = current_num
            current_num += 1
        for y in range(end_y-1, start_y-1, -1):
            grid[y][start_x] = current_num
            current_num += 1
        
        start_x += 1
        end_x -= 1
        start_y += 1
        end_y -= 1
    
    return grid

def find_most_zeros_and_total(grid):
    max_zero_row = 0
    max_zero_count = 0
    max_sum_col = 0
    max_sum = 0
    
    for row in grid:
        zero_count = row.count(0)
        if zero_count > max_zero_count:
            max_zero_count = zero_count
            max_zero_row = len(row)
    
    for col in zip(*grid):  # Transpose the grid to iterate over columns
        sum_col = sum(col)
        if sum_col > max_sum:
            max_sum = sum_col
            max_sum_col = len(col)
    
    return max_zero_row, max_sum_col

def divide_grid(grid, row, col):
    upper_left = grid[:row, :col]
    lower_right = grid[row:, col:]
    return upper_left, lower_right

def display_tables(upper_left, lower_right):
    print("Upper Left Table:")
    for row in upper_left:
        print(row)
    print("\nLower Right Table:")
    for row in lower_right:
        print(row)

# Example usage
size = 5
grid = fill_spiral(size)
most_zeros_row, total_sum_col = find_most_zeros_and_total(grid)
upper_left, lower_right = divide_grid(grid, most_zeros_row, total_sum_col)
display_tables(upper_left, lower_right)

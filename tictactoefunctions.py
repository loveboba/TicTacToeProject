from grid import the_grid

# Function that checks if the grid is full or not

def is_grid_full():
    for sublist in the_grid:
        for small_element in sublist:
            if small_element == '_':
                return False
    return True


# Function that checks if there is a win for 'X'

def has_x_won():
    # Check if there are even three X's in the grid
    count = 0
    for sublist in the_grid:
        for small_element in sublist:
            if small_element == 'X':
                count += 1
    if count < 3:
        return False
    else:
        # Check if 3 X's are in a row - use first element and second element

        # Check the 3 rows
        for inner_list in the_grid:
            x_count = 0
            for smallest_element in inner_list:
                if smallest_element == 'X':
                    x_count += 1
                    if x_count == 3:
                        return True

        # Check the 3 columns
        if the_grid[0][0] == 'X' and the_grid[1][0] == 'X' and the_grid[2][0] == 'X':
            return True
        if the_grid[0][1] == 'X' and the_grid[1][1] == 'X' and the_grid[2][1] == 'X':
            return True
        if the_grid[0][2] == 'X' and the_grid[1][2] == 'X' and the_grid[2][2] == 'X':
            return True

        # Check the 2 diagonals
        if the_grid[0][0] == 'X' and the_grid[1][1] == 'X' and the_grid[2][2] == 'X':
            return True
        if the_grid[0][2] == 'X' and the_grid[1][1] == 'X' and the_grid[2][0] == 'X':
            return True

    return False


# Function that checks if there is a win for 'O'

def has_o_won():
    # Check if there are even three X's in the grid
    count = 0
    for sublist in the_grid:
        for small_element in sublist:
            if small_element == 'O':
                count += 1
    if count < 3:
        return False
    else:
        # Check if 3 X's are in a row - use first element and second element

        # Check the 3 rows
        for inner_list in the_grid:
            x_count = 0
            for smallest_element in inner_list:
                if smallest_element == 'O':
                    x_count += 1
                    if x_count == 3:
                        return True

        # Check the 3 columns
        if the_grid[0][0] == 'O' and the_grid[1][0] == 'O' and the_grid[2][0] == 'O':
            return True
        if the_grid[0][1] == 'O' and the_grid[1][1] == 'O' and the_grid[2][1] == 'O':
            return True
        if the_grid[0][2] == 'O' and the_grid[1][2] == 'O' and the_grid[2][2] == 'O':
            return True

        # Check the 2 diagonals
        if the_grid[0][0] == 'O' and the_grid[1][1] == 'O' and the_grid[2][2] == 'O':
            return True
        if the_grid[0][2] == 'O' and the_grid[1][1] == 'O' and the_grid[2][0] == 'O':
            return True

    return False

# Reset the grid function - delete (cannot use this function for global variable)

def reset_the_grid():
    # Set the grid back to empty
    # the_grid = [
    #     ['Empty', 'Empty', 'Empty'],
    #     ['Empty', 'Empty', 'Empty'],
    #     ['Empty', 'Empty', 'Empty']
    # ]
    for row in the_grid:
        for the_small in row:
            the_small = '_'


# This is Portfolio Tic-Tac-Toe Project

from grid import the_grid
from grid import print_the_grid
from tictactoefunctions import has_x_won, has_o_won, is_grid_full

# TODO: error handling, scoreboard, do you want to play another game, reset grid

# FIX ISSUE: the first while loop does not break after end

# except ValueError:
    #     the_list = input("You did not enter your input in the correct format. Try again: ")

    # # check that the user input was correct - first part now redundant
    # if type(first_element) != int or type(second_element) != int:
    #     raise ValueError("You did not enter your input in the correct format.")

    # if first_element < 0 or first_element > 3 or second_element < 0 or second_element > 3:
    #     raise ValueError("Your numbers are out of bounds.")

# Print welcome message with scoring system

# NOTE: set up scoring system ; add do you want to play again button at end - when full or if there is a win
# reset the grid function

playeronescore = 0
playertwoscore = 0

# Set Up The Player System

continue_game = True

while continue_game:

    not_done_one = True

    while not_done_one:

        # Ask Player 1 where they want it to be
        the_list = input("Player 1: What square do you choose? (Example: [1,1]) \n")

        # CATCH ERRORS - number out of bound, or not a number at all

        # first element and second element
        first_element = int(the_list[1])
        second_element = int(the_list[3])

        # Check to see if space is already filled up
        if the_grid[first_element][second_element] == 'Empty':

            # Fill Out the appropriate square on the grid
            the_grid[int(first_element)][int(second_element)] = 'X'

            # CHECK FOR WIN - define separate function
            win_no = has_x_won()
            if win_no:
                print("Congratulations Player 1!")
                print_the_grid()
                break

            # CHECK FOR FILLED UP - define separate function
            is_grid_filled = is_grid_full()
            if is_grid_filled:
                print("Game Over.")
                print_the_grid()
                break

            print_the_grid()
            not_done_one = False

        else:
            print("This space is occupied. Pick another space.")
            # continue

    # PLAYER 2 CODE

    not_done_two = True # move to top, and change to false in above code, if game done - same for player 1

    while not_done_two:

        # Ask Player 2 where they want it to be
        the_list = input("Player 2: What square do you choose? (Example: [1,1]) \n")

        # first element and second element

        first_element = int(the_list[1])
        second_element = int(the_list[3])

        # Check to see if space is already filled up
        if the_grid[first_element][second_element] == 'Empty':

            # Fill Out the appropriate square on the grid
            the_grid[int(first_element)][int(second_element)] = 'O'

            # CHECK FOR WIN - define separate function
            win_no = has_o_won()
            if win_no:
                print("Congratulations Player 2!")
                print_the_grid()
                # ASK IF YOU WANT TO PLAY ANOTHER GAME
                break

            # CHECK FOR FILLED UP - define separate function
            is_grid_filled = is_grid_full()
            if is_grid_filled:
                print("Game Over.")
                print_the_grid()
                break

            print_the_grid()
            not_done_two = False

        else:
            print("This space is occupied. Pick another space.")
            # continue






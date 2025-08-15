# This is Portfolio Tic-Tac-Toe Project

from grid import the_grid
from grid import print_the_grid
from tictactoefunctions import has_x_won, has_o_won, is_grid_full

# TODO: do you want to play another game, reset grid

# Print welcome message
print("Welcome to Tic-Tac-Toe!")

playeronescore = 0
playertwoscore = 0

# Set Up The Player System

continue_game = True

while continue_game:

    not_done_one = True

    not_done_two = True

    while not_done_one:

        # Ask Player 1 where they want it to be
        the_list = input("Player 1: What square do you choose? (Example: [1,1]) \n")

        # CATCH ERRORS - number out of bound, or not a number at all

        # first element and second element - this goes in the try for error handling

        the_error = True

        while the_error:
            try:
                first_element = int(the_list[1])
                second_element = int(the_list[3])
                if first_element > 2 or first_element < 0 or second_element > 2 or second_element < 0:
                    raise ValueError
            except ValueError:
                the_error = True
                the_list = input("You did not use the correct format or your numbers are out of bounds. Try again: ")
            except Exception:
                the_error = True
                the_list = input("Unexpected error. Try again: ")
            else:
                the_error = False


        # Check to see if space is already filled up
        if the_grid[first_element][second_element] == '_':

            # Fill Out the appropriate square on the grid
            the_grid[int(first_element)][int(second_element)] = 'X'
            print_the_grid() # ADDED HERE

            # CHECK FOR WIN - define separate function
            win_no = has_x_won()
            if win_no:
                print("Congratulations Player 1!")
                playeronescore += 1
                print_the_grid()
                not_done_two = False
                # break

                # WOULD YOU LIKE TO PLAY AGAIN - same thing but with reset grid and NO break statement
                # add error catch here - maybe no need

                ask_the_user = input("Play again? Type 'Y' or 'N': ")

                if ask_the_user == 'Y':
                    # Reset the grid - no break; if no - break
                    print("Came in here")

                    # for row in the_grid:
                    #     print("Came in here 1")
                    #     for the_small in row:
                    #         the_small = '_'

                    # Reset the grid
                    # the_list = reset_the_grid()
                    for i in range(3):
                        for j in range(3):
                            the_grid[i][j] = '_'

                    not_done_two = True # change to continue the game
                else:
                    print("Came in here 2")
                    break





            # CHECK FOR FILLED UP - define separate function
            is_grid_filled = is_grid_full()
            if is_grid_filled:
                print("Game Over.")
                print_the_grid()
                not_done_two = False

                # WOULD YOU LIKE TO PLAY AGAIN - same thing but with reset grid and NO break statement
                # add error catch here - maybe no need

                ask_the_user = input("Play again? Type 'Y' or 'N': ")

                if ask_the_user == 'Y':
                    # Reset the grid - no break; if no - break
                    print("Came in here")

                    # for row in the_grid:
                    #     print("Came in here 1")
                    #     for the_small in row:
                    #         the_small = '_'

                    # Reset the grid
                    # the_list = reset_the_grid()
                    for i in range(3):
                        for j in range(3):
                            the_grid[i][j] = '_'

                    not_done_two = True  # change to continue the game
                else:
                    print("Came in here 2")
                    break

                # break

            # print_the_grid()
            not_done_one = False

        else:
            print("This space is occupied. Pick another space.")
            # continue

    if not_done_two == False:
        break

    not_done_one = True

    # PLAYER 2 CODE

    while not_done_two:

        # Ask Player 2 where they want it to be
        the_list = input("Player 2: What square do you choose? (Example: [1,1]) \n")

        # first element and second element

        # first element and second element - this goes in the try for error handling

        the_error = True

        while the_error:
            try:
                first_element = int(the_list[1])
                second_element = int(the_list[3])
                if first_element > 2 or first_element < 0 or second_element > 2 or second_element < 0:
                    raise ValueError
            except ValueError:
                the_error = True
                the_list = input(
                    "You did not use the correct format or your numbers are out of bounds. Please try inputting again: ")
            except Exception:
                the_error = True
                the_list = input("Unexpected error. Try again: ")
            else:
                the_error = False

        # Check to see if space is already filled up
        if the_grid[first_element][second_element] == '_':

            # Fill Out the appropriate square on the grid
            the_grid[int(first_element)][int(second_element)] = 'O'
            print_the_grid() # ADDED HERE


            # CHECK FOR WIN - define separate function
            win_no = has_o_won()
            if win_no:
                print("Congratulations Player 2!")
                playertwoscore += 1
                print_the_grid()
                not_done_one = False
                # ASK IF YOU WANT TO PLAY ANOTHER GAME
                break

            # CHECK FOR FILLED UP - define separate function
            is_grid_filled = is_grid_full()
            if is_grid_filled:
                print("Game Over.")
                print_the_grid()
                not_done_one = False
                break

            # print_the_grid()
            not_done_two = False

        else:
            print("This space is occupied. Pick another space.")
            # continue

    if not_done_one == False:
        break

    # not_done_two == True

# AFTER GAME IS DONE - PRINT OUT FINAL SCORE

print("\nPlayer 1 Final Score: " + str(playeronescore))
print("Player 2 Final Score: " + str(playertwoscore))

# reset_the_grid() # doesn't work
print_the_grid()



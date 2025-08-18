# This is Portfolio Tic-Tac-Toe Project

from grid import the_grid
from grid import print_the_grid
from tictactoefunctions import has_x_won, has_o_won, is_grid_full
import google.generativeai as genai
from dotenv import load_dotenv
import os

# TODO: Debug AI part

# Print welcome message
print("Welcome to Tic-Tac-Toe!")

# Ask if you want the other player to be AI or not
ai_or_no = False
ask_ai_or_no = input("Y/n - Do you want to play against an AI player?")

if ask_ai_or_no == 'Y':
    ai_or_no = True

# If other player is AI - initialize the AI and prepare to play
if ai_or_no:

    # Get API key
    load_dotenv()
    my_api_key = os.getenv("GEMINI_API_KEY")

    # Configure API key
    genai.configure(api_key=my_api_key)

    # Initialize model
    the_model = genai.GenerativeModel('gemini-2.5-flash')

    instructions_for_ai = (
        "You are playing Tic Tac Toe against another player. You are Player 2. The grid is 3 by 3. You will return your"
        "answer in this format: [row,col]. When you are asked for your move, do not give any other words or "
        "information. Just return [int,int] (sorry about this!). The rows starts at 0 (top row) and end at 2. The "
        "leftmost"
        "column is 0 and the rightmost is 2. Column 1 is the middle column. Therefore, the numbers "
        "you give in row and col cannot be less than 0 or greater than 2. The board is in a "
        "nested list format. You will be given the board so you can make moves. You cannot occupy a space that has "
        "already been occupied. Respond with a welcome message for the other player.")

    # Start new chat session
    chat = the_model.start_chat(history=[])

    # Send message and get a response
    ai_response = chat.send_message(instructions_for_ai)
    print(ai_response.text)


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
                    # print("Came in here")

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

                    # TELL THE AI WE ARE PLAYING AGAIN
                    if ai_or_no:
                        tell_ai = chat.send_message("Player 1 won! We are playing one more game. The grid has been reset.")
                        print(tell_ai.text)
                        # get response
                else:
                    # print("Came in here 2")
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
                    # print("Came in here")

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

                    # TELL THE AI WE ARE PLAYING AGAIN
                    if ai_or_no:
                        tell_ai = chat.send_message("The game resulted in a tie. We are playing one more game. The grid "
                                                "has been reset.")
                        print(tell_ai.text)
                        # get response
                else:
                    # print("Came in here 2")
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

        # Ask Player 2 where they want it to be - AI or human player
        if ai_or_no:
            get_move = chat.send_message("What square do you choose? (An example of your output format is [1,"
                                         "1]). Choose only one square, then wait for the other player's move. If the "
                                         "grid is the same as when you made the last move, then do not make a move. "
                                         "Here is"
                                         "the current grid: " + str(the_grid))
            print(get_move.text)
            print("CAME HERE! - 1")
            the_list = get_move.text
            print(the_list)
            print("CAME HERE! - 3")

        else:
            the_list = input("Player 2: What square do you choose? (Example: [1,1]) \n")

        # first element and second element

        # first element and second element - this goes in the try for error handling

        print("CAME HERE! - 4")

        the_error = True

        while the_error:
            try:
                first_element = int(the_list[1])
                second_element = int(the_list[3])
                if first_element > 2 or first_element < 0 or second_element > 2 or second_element < 0:
                    raise ValueError
            except ValueError:
                the_error = True
                if ai_or_no:
                    the_list = chat.send_message("You did not use the correct format or your numbers are out of "
                                                 "bounds. Please try inputting again: ")
                    print(the_list.text)
                    # ADD PRINT STATEMENTS - FOR AI STUFF (ALL)
                else:
                    the_list = input(
                        "You did not use the correct format or your numbers are out of bounds. Please try inputting "
                        "again: ")

            except Exception:
                the_error = True
                if ai_or_no:
                    the_list = chat.send_message("Unexpected error. Try again: ")
                    print(the_list.text)
                else:
                    the_list = input("Unexpected error. Try again: ")
            else:
                the_error = False

        # Check to see if space is already filled up
        if the_grid[first_element][second_element] == '_':

            # Fill Out the appropriate square on the grid
            the_grid[int(first_element)][int(second_element)] = 'O'
            print("CAME HERE! -2")
            print_the_grid() # ADDED HERE

            # CHECK FOR WIN - define separate function
            win_no = has_o_won()
            if win_no:
                playertwoscore += 1
                print_the_grid()
                not_done_one = False
                # if AI - tell the AI it won
                if ai_or_no:
                    print("Player 2 has won!")
                    final = chat.send_message("Congratulations Player 2! Print a message of victory!")
                    print(final.text)
                    # break
                else:
                    print("Congratulations Player 2!")

                # ASK IF YOU WANT TO PLAY ANOTHER GAME
                # WOULD YOU LIKE TO PLAY AGAIN - same thing but with reset grid and NO break statement
                # add error catch here - maybe no need

                # if not ai_or_no:
                ask_the_user = input("Play again? Type 'Y' or 'N': ")

                if ask_the_user == 'Y':
                        # Reset the grid - no break; if no - break
                        # print("Came in here")

                        # for row in the_grid:
                        #     print("Came in here 1")
                        #     for the_small in row:
                        #         the_small = '_'

                        # Reset the grid
                        # the_list = reset_the_grid()
                    for i in range(3):
                        for j in range(3):
                            the_grid[i][j] = '_'

                    not_done_one = True  # change to continue the game
                else:
                        # print("Came in here 2")
                    break
                    # break

            # CHECK FOR FILLED UP - define separate function
            is_grid_filled = is_grid_full()
            if is_grid_filled:
                # Tell AI - game over
                # if AI - tell the AI game over
                if ai_or_no:
                    print("Game Over.")
                    final = chat.send_message("The game is over - it is a tie.")
                    print(final.text)
                    break
                else:
                    print("Game Over.")
                print_the_grid()
                not_done_one = False
                # WOULD YOU LIKE TO PLAY AGAIN - same thing but with reset grid and NO break statement
                # add error catch here - maybe no need

                # if not ai_or_no:
                ask_the_user = input("Play again? Type 'Y' or 'N': ")

                if ask_the_user == 'Y':
                        # Reset the grid - no break; if no - break
                        # print("Came in here")

                        #   for row in the_grid:
                        #     print("Came in here 1")
                        #     for the_small in row:
                        #         the_small = '_'

                        # Reset the grid
                        # the_list = reset_the_grid()
                    for i in range(3):
                        for j in range(3):
                            the_grid[i][j] = '_'

                    not_done_one = True  # change to continue the game
                else:
                        # print("Came in here 2")
                     break
                    # break

            # print_the_grid()
            not_done_two = False

        else:
            # TEll AI the space is occupied
            if ai_or_no:
                sent_message = chat.send_message("This space is occupied. Pick another space.")
                print(sent_message.text)
            else:
                print("This space is occupied. Pick another space.")
            # continue

    if not_done_one == False:
        break

    # not_done_two == True

# SET UP PLAYER SYSTEM - ONE PLAYER IS AI

# AFTER GAME IS DONE - PRINT OUT FINAL SCORE

print("\nPlayer 1 Final Score: " + str(playeronescore))
print("Player 2 Final Score: " + str(playertwoscore))

# reset_the_grid() # doesn't work
print_the_grid()



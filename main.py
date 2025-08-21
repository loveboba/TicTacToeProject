# This is Portfolio Tic-Tac-Toe Project
from grid import the_grid
from grid import print_the_grid
from tictactoefunctions import has_x_won, has_o_won, is_grid_full
import google.generativeai as genai
from dotenv import load_dotenv
import os

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

# Initialize variables
first_element = 0
second_element = 0
player_one_score = 0
player_two_score = 0

# Set Up The Player System

continue_game = True

while continue_game:

    not_done_one = True

    not_done_two = True

    # PLAYER 1 CODE

    while not_done_one:

        # Ask Player 1 about their first move
        the_list = input("Player 1: What square do you choose? (Example: [1,1]) \n")

        # Error Handling

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

            # Print the grid
            print("Player 1 move: " + str(the_list))
            print_the_grid()

            # CHECK FOR WIN
            win_no = has_x_won()

            # If Player 1 has won...
            if win_no:
                print("Congratulations Player 1!")
                player_one_score += 1
                print("Final grid: ")
                print_the_grid()
                not_done_two = False

                # Ask the user if they would like to play again
                ask_the_user = input("Play again? Type 'Y' or 'N': ")

                # If the user wants to play again
                if ask_the_user == 'Y':

                    # Reset the Grid
                    for i in range(3):
                        for j in range(3):
                            the_grid[i][j] = '_'

                    # Player 2 makes the first move of the next game
                    not_done_two = True

                    # If Player 2 is AI - tell AI that we are playing another game.
                    if ai_or_no:
                        tell_ai = chat.send_message("Player 1 won! We are playing one more game. The grid has been "
                                                    "reset.")
                        # print(tell_ai.text)

                # If the user does not want to play again
                else:
                    break

            # CHECK IF THE GRID HAS FILLED UP
            is_grid_filled = is_grid_full()

            # If the grid is filled up
            if is_grid_filled:
                print("Game Over.")
                print("Final grid: ")
                print_the_grid()
                not_done_two = False

                # Ask the user if they would like to play again
                ask_the_user = input("Play again? Type 'Y' or 'N': ")

                # User wants to play again:
                if ask_the_user == 'Y':
                    for i in range(3):
                        for j in range(3):
                            the_grid[i][j] = '_'
                    not_done_two = True

                    # If Player 2 is AI - tell them we are playing another game.
                    if ai_or_no:
                        tell_ai = chat.send_message("The game resulted in a tie. We are playing one more game. The "
                                                    "grid has been reset.")
                        print(tell_ai.text)
                else:
                    break

            # No longer Player 1's turn
            not_done_one = False
        else:
            print("This space is occupied. Pick another space.")

    if not not_done_two:
        break

    not_done_one = True

    # PLAYER 2 CODE

    while not_done_two:

        # Ask Player 2 about where they want their move - AI or human player

        # AI Player
        if ai_or_no:
            get_move = chat.send_message("What square do you choose? (An example of your output format is [1,"
                                         "1]). Choose only one square, then wait for the other player's move. If the "
                                         "grid is the same as when you made the last move, then do not make a move. "
                                         "Here is"
                                         "the current grid: " + str(the_grid))
            print(get_move.text)
            the_list = get_move.text
        # Human Player
        else:
            the_list = input("Player 2: What square do you choose? (Example: [1,1]) \n")

        # Error Handling
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
            print("Player 2 move: " + str(the_list))
            print_the_grid()

            # CHECK FOR WIN
            win_no = has_o_won()

            if win_no:
                player_two_score += 1
                print("Final grid: ")
                print_the_grid()
                not_done_one = False

                # If the Player is AI - tell the AI it won
                if ai_or_no:
                    print("Player 2 has won!")
                    final = chat.send_message("Congratulations Player 2! Print a message of victory!")
                    print(final.text)
                # If the Player is human
                else:
                    print("Congratulations Player 2!")

                # Ask the user if they would like to play again
                ask_the_user = input("Play again? Type 'Y' or 'N': ")

                if ask_the_user == 'Y':
                    for i in range(3):
                        for j in range(3):
                            the_grid[i][j] = '_'
                    not_done_one = True
                else:
                    break

            # Check if the grid is filled up
            is_grid_filled = is_grid_full()

            if is_grid_filled:
                # Tell AI
                if ai_or_no:
                    print("Game Over.")
                    final = chat.send_message("The game is over - it is a tie.")
                    print(final.text)
                # Tell the user
                else:
                    print("Game Over.")

                print("Final grid: ")
                print_the_grid()
                not_done_one = False

                # Ask the user if they would like to play again
                ask_the_user = input("Play again? Type 'Y' or 'N': ")

                if ask_the_user == 'Y':
                    for i in range(3):
                        for j in range(3):
                            the_grid[i][j] = '_'
                    not_done_one = True
                else:
                     break

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

# AFTER GAME IS DONE - PRINT OUT FINAL SCORE

print("\nPlayer 1 Final Score: " + str(player_one_score))
print("Player 2 Final Score: " + str(player_two_score))





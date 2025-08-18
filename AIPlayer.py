# from google import genai
import google.generativeai as genai

from dotenv import load_dotenv
import os


# Get API key
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")

# Configure API key
genai.configure(api_key=my_api_key)

# Initialize model
the_model = genai.GenerativeModel('gemini-2.5-flash')

instructions_for_ai = ("You are playing Tic Tac Toe against another player. The grid is 3 by 3. You will return your "
                       "answer in this format: [row,col]. The rows starts at 0 (top row) and end at 2. The leftmost "
                       "column is 0 and the rightmost is 2. Column 1 is the middle column. Therefore, the numbers "
                       "you give in row and col cannot be less than 0 or greater than 2. The board is in a "
                       "nested list format. You cannot occupy a space that has already been occupied. It is your "
                       "move. You will be given occupied spaces in list format.")
# Start new chat session
chat = the_model.start_chat(history=[])

# Send message and get a response
ai_response = chat.send_message(instructions_for_ai)
print(ai_response.text)






# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=instructions_for_ai
# )
#
#
#
# print(response.text)


# FUNCTION TO ESTABLISH AI PLAYER

# FUNCTION TO GET RESPONSE FROM PLAYER





# TWO FUNCTIONS

# TELL THE AI GAME HOW TO PLAY





#
# instructions_for_ai.append( {
#     "content": "My last move is [1,1]. The board is empty other than that."
# })
#
# the_chat = client.chat.completions.create(model="gemini-2.5-flash", messages=instructions_for_ai)
#
# print(the_chat.choices[0].message.content)





# TELL AI GAME WHAT BOARD LOOKS LIKE


# GET AI RESPONSE AND INPUT IT







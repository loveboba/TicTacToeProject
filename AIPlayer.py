# from google import genai
import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)

instructions_for_ai = ("You are playing Tic Tac Toe against another player. The grid is 3 by 3. You will return your "
                       "answer in this format: [row,col]. The rows starts at 0 (top row) and end at 2. The leftmost "
                       "column is 0 and the rightmost is 2. Column 1 is the middle column. Therefore, the numbers "
                       "cannot you give in row and col cannot be less than 0 or greater than 2. The board is in a "
                       "nested list format. You cannot occupy a space that has already been occupied. It is your "
                       "move. You will be given occupied spaces in list format. If list is empty, then no spaces are "
                       "occupied. The currently occupied spaces are: [1,1].")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=instructions_for_ai
)

print(response.text)





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







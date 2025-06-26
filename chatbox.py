import tkinter as tk
from datetime import datetime
import random

# Jokes list
jokes = [
    "Why are mountains so funny? They’re hill areas.",
    "What did 20 do when it was hungry? Twenty-eight.",
    "Why was Cinderella so bad at soccer? She kept running away from the ball.",
    "What did the fish say when he swam into the wall? DAM!!"
]

# Answering the user
def lets_chat():
    user_input = entry.get().lower()

    if "hi" in user_input or "hello" in user_input:
        answer = "Hey there! I'm your friendly chatbot 😄"
    elif "joke" in user_input:
        answer= random.choice(jokes)
    elif "date" in user_input:
        answer = "Today's date is: " + datetime.now().strftime("%b %d, %Y")
    elif "time" in user_input:
        answer = "Current time is: " + datetime.now().strftime("%I:%M %p")
    else:
        answer = "I can greet you, tell jokes, and give the date or time. Try typing 'joke'!"

    chat.insert(tk.END, f"You: {entry.get()}\nBot: {answer}\n\n")
    entry.delete(0, tk.END)

# GUI setup
window = tk.Tk()
window.title("A Chatbot - to greet and for jokes")

chat = tk.Text(window, width=60, height=20, bg="lavender")
chat.pack(pady=10)

entry = tk.Entry(window, width=50)
entry.pack(padx=10)

send_button = tk.Button(window, text="Send", command=lets_chat, bg="lightblue")
send_button.pack(pady=5)

window.mainloop()
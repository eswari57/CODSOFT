import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
import random

# Sample book data
books = [
    {"title": "The Silent Patient", "genre": "Thriller"},
    {"title": "The Friend Zone", "genre": "Romance"},
    {"title": "Love and Other Words", "genre": "Romance"},
    {"title": "If He Had Been with Me", "genre": "Romance"},
    {"title": "Archer's Voice", "genre": "Romance"},
    {"title": "Verity", "genre": "Thriller"},
    {"title": "The Alchemist", "genre": "Philosophical Fiction"},
    {"title": "A Thousand Splendid Suns", "genre": "Drama"},
    {"title": "The Fault in Our Stars", "genre": "Romance"},
    {"title": "The Notebook", "genre": "Romance"},
    {"title": "The Housemaid", "genre": "Thriller"},
    {"title": "A Court of Thorns and Roses", "genre": "Fantasy"},
    {"title": "Six of Crows", "genre": "Fantasy"},
    {"title": "Throne of Glass", "genre": "Fantasy"},
]

# Book recommendation functions
def recommend_books(genre):
    recommended = [book["title"] for book in books if book["genre"] == genre]
    result_var.set("\n".join(recommended) if recommended else "No books found for this genre.")

def surprise_me():
    surprise = random.choice(books)
    result_var.set(f"🎉 Surprise Read: {surprise['title']} ({surprise['genre']})")

# GUI Setup
root = tk.Tk()
root.title("Book Recommender")
root.geometry("600x500")
root.configure(bg="#fceef5")  # Cherry blossom pink

title_label = tk.Label(root, text="📚 Book Recommender", font=("Georgia", 22, "bold"), bg="#fceef5", fg="#8b5d76")
title_label.pack(pady=30) 
title_label.place(relx=0.5, y=130, anchor='n') # Push title down a bit

genre_label = tk.Label(root, text="Choose your favorite genre:", font=("Georgia", 14), bg="#fceef5", fg="#8b5d76")
genre_label.pack(pady=(10, 0))
genre_label.place(relx=0.5, y=180, anchor='n')

genre_choice = ttk.Combobox(root, values=["Romance", "Fantasy", "Thriller"])
genre_choice.pack(pady=(10, 20))  # Adds extra space after combo box
genre_choice.place(relx=0.5, y=215, anchor='n')

recommend_btn = tk.Button(root, text="Recommend", font=("Georgia", 12), bg="#f8c8dc", fg="#8b5d76", command=lambda: recommend_books(genre_choice.get()))
recommend_btn.pack(pady=5)
recommend_btn.place(relx=0.5, y=260, anchor='n')

surprise_btn = tk.Button(root, text="Surprise Me!", font=("Georgia", 12), bg="#f8c8dc", fg="#8b5d76", command=surprise_me)
surprise_btn.pack(pady=5)
surprise_btn.place(relx=0.5, y=305, anchor='n')
# Output
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Georgia", 12), bg="#fceef5", fg="#8b5d76", justify="center", wraplength=450)
result_label.pack(pady=20)
result_label.place(relx=0.5, y=370, anchor='n')


# --- Cherry Blossoms Animation ---
cherry_img = Image.open("cherry flowers.gif")
cherry_frames = [ImageTk.PhotoImage(frame.copy().resize((220, 120))) for frame in ImageSequence.Iterator(cherry_img)]
cherry_label = tk.Label(root, bg="#fff0f5")
cherry_label.place(relx=1.0, y=10, anchor='ne')

def animate_cherry(index):
    cherry_label.configure(image=cherry_frames[index])
    root.after(120, animate_cherry, (index + 1) % len(cherry_frames))

animate_cherry(0)


root.mainloop()





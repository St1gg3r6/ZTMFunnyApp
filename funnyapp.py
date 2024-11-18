import pyjokes
import tkinter as tk


def get_joke():
    new_joke = pyjokes.get_joke()
    return new_joke


def get_next_joke():
    new_joke = pyjokes.get_joke()
    label.config(text=new_joke)


root = tk.Tk()
root.geometry("800x400")
root.title("It's a Joke!")
label = tk.Label(root, text=pyjokes.get_joke())
label.config(height="6", wraplength="600")
label.pack()
next_joke = tk.Button(
    text="Another!",
    command=get_next_joke,
    height=3,
    width=18, 
    relief="raised",
    activebackground="lightblue")
next_joke.place(x=325, y=180)
root.mainloop()

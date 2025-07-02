import tkinter as tk

screen = tk.Tk()
text = tk.Label(text="Test", background="red")
text.pack()

button = tk.Button(text="Drück mich nicht!")
button.pack()

screen.mainloop()
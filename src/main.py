import tkinter as tk


def main() -> None:
    """Main Funktion"""
    screen = tk.Tk(className = "pightroom")
    text = tk.Label(screen, text = "Potexxi's Pightroom", background = "lightyellow", font=("Arial", 20, "bold"))
    text.place(x=100, y=10)

    button = tk.Button(text="Drück mich nicht!")
    button.pack()

    screen.mainloop()


if __name__ == "__main__":
    main()
import tkinter as tk
import submodule.pictures as pictures


def main() -> None:
    """Main Funktion"""
    screen = tk.Tk(className = "pightroom")
    screen.geometry("1000x600")

    header = tk.Label(screen, text = "Potexxi's Pightroom", background = "lightyellow", font=("Arial", 25, "bold"))
    status_label_pictures = tk.Label(screen, text="", font=("Arial", 10))
    status_label_path = tk.Label(screen, text="", font=("Arial", 10))
    button_picture_select = tk.Button(screen, text="Select Pictures", command=lambda: pictures.select(status_label_pictures),
                       font=("Arial", 15), background="lightblue")
    button_export_path = tk.Button(screen, text="Select export path", command=lambda: pictures.export_path(status_label_path),
                       font=("Arial", 15), background="lightblue")

    header.pack(pady=5)
    button_picture_select.place(x=100, y=100)
    status_label_pictures.place(x=100, y=140)
    button_export_path.place(x=100, y=200)
    status_label_path.place(x=10, y=240)

    screen.mainloop()


if __name__ == "__main__":
    main()
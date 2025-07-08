import tkinter
from tkinter import filedialog
from PIL import Image
import src.submodule.globals as g


def export_path(status_label_path: tkinter.Label) -> None:
    g.EXPORT_PATH = filedialog.askdirectory()
    status_label_path.config(text=f"current Path: {g.EXPORT_PATH}")


def select(status_label_pictures: tkinter.Label) -> None:
    """
    Select the pictures, which the user wants to edit
    :param status_label_pictures: the statuslabel, the text, how many pictures the user selected
    """
    g.PICTURES.clear()
    datapath = filedialog.askopenfilenames(title="Select Pictures", filetypes=[("Bilddateien", "*.jpg *.jpeg *.png")])
    for path in datapath:
        try:
            picture = Image.open(path)
            g.PICTURES.append(picture)
        except Exception:
            print(f"Fehler beim laden: {Exception}")
    if len(g.PICTURES) == 1:
        status_label_pictures.config(text=f"{len(g.PICTURES)} picture loaded.")
    else:
        status_label_pictures.config(text=f"{len(g.PICTURES)} pictures loaded.")
import os
import tkinter as tk
from tkinter import filedialog

if __name__ == "__main__":
  s = "programa"
  script_path = os.path.abspath(__file__)
  
  name = script_path
  if True:
    root = tk.Tk()
    root.withdraw()
    script_path = filedialog.askdirectory()
    root.destroy()
  
  name = script_path + "/example.txt"
  with open(name, "w") as f:
    f.write((s + " ") * 1)


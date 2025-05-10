import tkinter as tk
from workout_gui import WorkoutGUI

def main():
    root = tk.Tk()
    app = WorkoutGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

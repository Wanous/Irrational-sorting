import tkinter as tk
from sources.Sorting_Visualizer import SortingVisualizer
'''
main.py initiate the app.
Every search of a file start with this folder because main.py start it.
three ligns yes but a useful file for the structure of the code.
'''
root = tk.Tk()
visualizer = SortingVisualizer(root)
root.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import random
import json

from sources.Irrational_sorting import irrational_sorting

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")
        self.root.iconbitmap("sources/ressources/images/TPI_LOGO.ico")
        self.window_size=(800,450)
        self.root.geometry(f"{self.window_size[0]}x{self.window_size[1]}")
        self.root.minsize(500,450) 
        self.font = Font(family="Arial", size=16, weight="bold")
        self.font_2 = Font(family="Arial", size=15, weight="bold")

        #---Images 
        self.images = {'Button_startOn':  tk.PhotoImage(file="sources/ressources/images/Boutton_start_ON.png"),
                       'Restart_Button':  tk.PhotoImage(file="sources/ressources/images/Button_restart.png"),
                      }
       
        # loads the image/decimals of irrationals
        with open('Irrationals_numbers.json', 'r') as f:
            data = json.load(f)

        # add them to self.images
        for I in data["Irrational"]:
            self.images[I['name']] = {'image' : tk.PhotoImage(file=I['image_path']),'file' : I['decimals_path'] }

        #---List of random numbers---
        self.data = [0]
        
        self.Speed = {'min':1,'max':100}
        self.list_size = {'min':2,'max':20}

        self.irrational = data["Irrational"][0]['name']
        self.Sorting = irrational_sorting(self,self.data,self.images[self.irrational]['file'])

        #---Canvas---
        self.canvas = tk.Canvas(root, width=600, height=500, bg="white")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.decimals_counter = tk.Label(root,font=self.font_2,text="Decimals used : ") 

        #---Frame with the controls of the application--- 
        self.controls_frame = tk.Frame(root)
        self.controls_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.space = tk.Label(self.controls_frame, text="") # Space to set the other controls in the center
        self.space.pack(pady=self.root.winfo_width())
        
        self.speed_label = tk.Label(self.controls_frame, text="2.0") # Speed control
        self.speed_label.pack()
        self.speed_scale = ttk.Scale(self.controls_frame, from_=self.Speed['min'], to=self.Speed['max'], orient=tk.HORIZONTAL)
        self.speed_scale.set(self.Speed['max']/2)
        self.speed_scale.pack(pady=20)
        
        self.list_label = tk.Label(self.controls_frame, text="100") # Lenght of the list control
        self.list_label.pack()
        self.size_scale = ttk.Scale(self.controls_frame, from_=self.list_size['min'], to=self.list_size['max'], orient=tk.HORIZONTAL)
        self.size_scale.set(self.list_size['max']/2)
        self.size_scale.pack(pady=20)

        self.start_button = tk.Button(self.controls_frame, text=" Start ", command=self.start_sort,image=self.images['Button_startOn'],border=0) # To start the sorting
        self.start_button.pack()

        self.reset_button = tk.Button(self.controls_frame, text="Restart", command=self.reset,image=self.images['Restart_Button'],border=0) # To restart a new sorting
        self.reset_button.pack()

        self.combobox = ttk.Combobox(self.controls_frame,
                                     state="readonly",
                                     values=[name['name'] for name in data["Irrational"]],
                                     width=30)
        
        self.combobox.current(0)
        self.combobox.pack(pady=10)
        #Canvas for the image
        self.Irrational_image = tk.Canvas(self.controls_frame, width = 60, height = 60)
        self.Irrational_image.pack(pady=20)
        self.Irrational_image.create_image(25,25, image=self.images[data["Irrational"][0]['name']]['image'],anchor=tk.CENTER)

        #---Frame for the irrationnal number--- 
        self.digits_frame = tk.Frame(root)
        self.digits_frame.place(x=self.root.winfo_width()*0.7,y=self.root.winfo_height()*0.3,width=self.root.winfo_width()*0.7,height=self.root.winfo_height()*0.3)

        self.digits_label = tk.Label(self.digits_frame,font=self.font,text="Decimals here") 
        self.digits_label.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        #---Events---
        self.combobox.bind("<<ComboboxSelected>>", self.change_irrational)
        self.root.bind("<B1-Motion>", self.Update_Value)
        self.diff=0
        self.root.bind("<Configure>", self.gestion_affichage)
        
        self.is_sorting = False
        self.gestion_affichage()
        self.Update_Value()
        self.reset()
    
    def Update_Value(self,event=None):
         self.speed_label['text'] = round(self.speed_scale.get()/self.Speed['max'],2)
         if int(self.list_label['text']) != int(self.size_scale.get()) :
             if self.is_sorting == False :
                 self.reset()
             self.list_label['text'] = int(self.size_scale.get())
             
    def gestion_affichage(self,event=None):    
        """
        Méthode qui gére le placement et l'affichage de tout les widgets de la fenêtre principales ,
        efficace pour produire des modifications de manière simple .
        """

        #---Canvas on the right of the Frame(70% of the screen width and 90% of the screen height)
        self.canvas.width = self.root.winfo_width()*0.7
        self.canvas.height = self.root.winfo_height()*0.9
        
        #---Placement
        self.controls_frame.place(x=0, y=0,width=self.root.winfo_width()*0.3,height=self.root.winfo_height())     
        self.digits_frame.place(x=self.root.winfo_width()*0.3,y=self.root.winfo_height()*0.9,width=self.root.winfo_width()*0.7,height=self.root.winfo_height()*0.1)                                                                             
        self.canvas.place(x=self.root.winfo_width()*0.3,y=0,height=self.root.winfo_height(),width=self.root.winfo_width()*0.7)
        self.decimals_counter.place(x=self.root.winfo_width()*0.3,y=self.root.winfo_height()*0.9-30)
      
        #---Draw the line that represent the numbers        
        self.diff = abs(self.root.winfo_height()*0.9 - self.window_size[1]*0.9)
        self.draw_data(self.data, ["#b472e0" for _ in range(len(self.data))])
        self.space.pack(pady=self.root.winfo_height()*0.05)

        self.font.configure(size = int(self.root.winfo_height()*0.03))

    def draw_data(self, data, color_array):
        self.canvas.delete("all")
        canvas_height = self.canvas.height
        canvas_width = self.canvas.width
        bar_width = canvas_width / len(data)
        for i, height in enumerate(data):
            x0 = i  * bar_width
            y0 = canvas_height - height - self.diff 
            x1 = (i + 1) * bar_width
            y1 = canvas_height 
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        self.root.update_idletasks()

    def reset(self):
        if self.is_sorting == True :
            self.is_sorting = False

        # put the buttons back on
        self.start_button.config(state=tk.NORMAL)
        self.combobox.configure(state="readonly")

        # generation of a new list
        self.data = [random.randint(int(self.window_size[1]*0.12),int(self.window_size[1]*0.88)) for _ in range(int(self.size_scale.get()))]
        self.draw_data(self.data, ["#b472e0" for _ in range(len(self.data))])
    
    def start_sort(self):
        # disabled buttons
        self.start_button.config(state=tk.DISABLED)
        self.combobox.configure(state="disabled")
        self.is_sorting = True

        # Charge the sort 
        self.Sorting = irrational_sorting(self,self.data,self.images[self.irrational]['file'])
        self.selection_sort()
        
    def selection_sort(self):

            def sort_step():
                if self.is_sorting == True:
                    if self.Sorting.verification_tri() != True :
                        self.Sorting.sorting()                        
                        self.root.after(int(self.Speed['max'] / self.speed_scale.get()), lambda: sort_step())
                    else:
                        self.is_sorting = False

            sort_step()

    def change_irrational(self,event = None):
        selection = self.combobox.get()
        self.Irrational_image.delete('all')
        self.Irrational_image.create_image(30,30, image=self.images[selection]['image'],anchor=tk.CENTER)
        self.Sorting.I_number = self.Sorting.irrationnel(self.images[selection]['file'])
        self.irrational = selection
        print(self.images[selection]['file'])


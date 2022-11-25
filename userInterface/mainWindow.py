import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class MainWindow(tk.Tk):
    
    def __init__(self, controller):

        super().__init__()
        self._controller = controller
        self.title('Word Cloud For Readers')
        self._display_frame = None
        self._txt1 = None
        self._btn1 = None
        self._btn2 = None
        self._text = tk.StringVar()
        self._labelwc = None
        self._second_frame = None
        self._create_main_frame()
        self._create_txt_input()
        self._scrollBar_txt()
        self._create_btn()        
        self.mainloop()
        

    
    def _create_main_frame(self):
        self.geometry("800x500")
        self.resizable(1,1)
        self._display_frame = tk.Frame(master=self)
        self._display_frame.pack(fill=BOTH,expand=1)       

        sec = Frame(self._display_frame)

        sec.pack(fill=X,side=BOTTOM)

        my_canvas = Canvas(self._display_frame, bg='red')

        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

        y_scrollbar = ttk.Scrollbar(self._display_frame,orient=VERTICAL,command=my_canvas.yview)

        y_scrollbar.pack(side=RIGHT,fill=Y)        

        my_canvas.configure(yscrollcommand=y_scrollbar.set)

        my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 

        self._second_frame = Frame(my_canvas, bg='red')
        

        my_canvas.create_window((0,0),window= self._second_frame, anchor="nw")

        


    def _create_txt_input(self):           

        self._txt1 = tk.Text(
            master=self._second_frame,
            
            )
        
        self._txt1.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        
        
    
    def _create_label_imagewc(self):        
        self._labelwc = tk.Label(
            master=self._second_frame,              
            borderwidth=2, 
            relief="groove",                        
            width=80, 
            height=25,            
            )
        
        self._labelwc.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,            
        )        

    
    def _scrollBar_txt(self):
                
        scroll_vert = tk.Scrollbar(
            master=self._second_frame,
            command=self._txt1.yview
            )

        scroll_vert.grid(
            row=0,
            column=1,
            sticky='nsew'
            )
        
        self._txt1.config(yscrollcommand=scroll_vert.set)
        
    
    
    def _create_btn(self):

        self._btn1 = tk.Button(
            master=self._second_frame,
            text='Analizar Texto',
            command= self._click_btn_analisis_word_cloud
            )
        
        self._btn1.grid(row=1,column=0)   
        
    
    
    def _click_btn_analisis_word_cloud(self):
        txt = self._txt1.get(1.0, tk.END+"-1c")
        self._controller.txt = txt        
        self._controller.word_cloud()
        self._create_label_imagewc()
        self._load_image()
        self._topics()
        self._words()
        self._btn_diagram_pie()    
        self._btn_graph()

    
    def _load_image(self):        
        imagewc = tk.PhotoImage(file='./wc.png')        
        self._labelwc['image'] = imagewc
        self._labelwc.image = imagewc         
        self._labelwc.config(width=800,height=250)

    
    def _btn_diagram_pie(self):
        self._btn2 = tk.Button(
            master=self._second_frame,
            text='Digrama de Torta',
            command= self._click_btn_diagram_pie
            )
        self._btn2.grid(row=5,column=0)   
    
    def _click_btn_diagram_pie(self):
        self._controller.diagram_pie()
    
    
    def _btn_graph(self):
        self._btn3 = tk.Button(
            master=self._second_frame,
            text='Relación Tema - palabras',
            command= self._click_btn_graph
            )
        self._btn3.grid(row=6,column=0)
           
    
    def _click_btn_graph(self):
        self._controller.graph()
    

    def _topics(self):
        thereis_topic = True
        self._gridFrame = tk.Frame(master=self._second_frame)
        for x in range(100):
            for y in range(5):
                topic = self._controller.topic()
                if topic!=0:
                    label = tk.Label(
                        master=self._gridFrame,              
                        borderwidth=2, 
                        relief="groove",                        
                        text=topic[0],           
                        )
                        
                    label.grid(   
                        padx=1,
                        pady=1,            
                        row=x,
                        column=y
                        )
                    if topic[1] == 1:
                        label.config(bg='light salmon')                        
                        
                else:
                    thereis_topic = False 
                    break
            if not thereis_topic:
                break
        self._gridFrame.grid(row=3 ,column=0)
    
    def _words(self):
        self._gridFramebtn = tk.Frame(master=self._second_frame)
        for row in range(100):            
            for col in range(8):                
                word = self._controller.words()
                if word != 0:
                    self._button = tk.Button(
                        master=self._gridFramebtn,
                        text=word,                    
                        fg="black",
                        width=10,
                        height=2,
                        highlightbackground="lightblue",
                        bg="purple2",                    
                    )                
                    self._button.bind("<ButtonPress-1>", self._cellClicked)
                    self._button.grid(
                        row=row,
                        column=col,
                        padx=5,
                        pady=5,
                        sticky="nsew"
                    )                
                
        self._gridFramebtn.grid(row=4 ,column=0)
                
    
    def _cellClicked(self,event):
        clickedBtn = event.widget 
        self._definition_word(clickedBtn['text'],self._controller.definition_word(clickedBtn['text']))
    
    def _definition_word(self, word, definition):
        defi = ""
        for x in definition:
            defi = defi + ("- "+x+"\n\n")
        messagebox.showinfo(message=defi, title="Definicion de "+word)
        

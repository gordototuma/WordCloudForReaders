import tkinter as tk
from tkinter import *


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
        self._create_main_frame()
        self._create_txt_input()
        self._create_label_imagewc()
        self._scrollBar_txt()
        self._create_btn()
        self._btn_diagram_pie()    
        self._btn_graph()        
        self.mainloop()
        

    
    def _create_main_frame(self):

        self._display_frame = tk.Frame(master=self)
        self._display_frame.pack(fill=tk.X)

        


    def _create_txt_input(self):           

        self._txt1 = tk.Text(
            master=self._display_frame,
            height=5
            )
        
        self._txt1.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )
    
    def _create_label_imagewc(self):        
        self._labelwc = tk.Label(
            master=self._display_frame,              
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
            master=self._display_frame,
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
            master=self._display_frame,
            text='Analizar Texto',
            command= self._click_btn_analisis_word_cloud
            )
        self._btn1.grid(row=1,column=0)   
        
    
    
    def _click_btn_analisis_word_cloud(self):
        txt = self._txt1.get(1.0, tk.END+"-1c")
        self._controller.txt = txt        
        self._controller.word_cloud()
        self._load_image()
        self._topics()

    
    def _load_image(self):        
        imagewc = tk.PhotoImage(file='./wc.png')        
        self._labelwc['image'] = imagewc
        self._labelwc.image = imagewc         
        self._labelwc.config(width=800,height=250)

    
    def _btn_diagram_pie(self):
        self._btn2 = tk.Button(
            master=self._display_frame,
            text='Digrama de Torta',
            command= self._click_btn_diagram_pie
            )
        self._btn2.grid(row=4,column=0)   
    
    def _click_btn_diagram_pie(self):
        self._controller.diagram_pie()
    
    
    def _btn_graph(self):
        self._btn3 = tk.Button(
            master=self._display_frame,
            text='Relación Tema - palabras',
            command= self._click_btn_graph
            )
        self._btn3.grid(row=5,column=0)
           
    
    def _click_btn_graph(self):
        self._controller.graph()
    

    def _topics(self):
        thereis_topic = True
        self._gridFrame = tk.Frame(master=self._display_frame)
        for x in range(100):
            for y in range(8):
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
                        
                    self._gridFrame.grid(row=3 ,column=0)
                else:
                    thereis_topic = False 
                    break
            if not thereis_topic:
                break
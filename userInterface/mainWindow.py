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
        self._text = tk.StringVar()
        self._labelwc = None
        self._create_main_frame()
        self._create_txt_input()
        self._create_label_imagewc()
        self._scrollBar_txt()
        self._create_btn()
        self.mainloop()
        

    
    def _create_main_frame(self):

        self._display_frame = tk.Frame(master=self)
        self._display_frame.pack(fill=tk.X)


    def _create_txt_input(self):           

        self._txt1 = tk.Text(
            master=self._display_frame,
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
            row=0,
            column=2,
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

    
    def _load_image(self):        
        imagewc = tk.PhotoImage(file='./wc.png')        
        self._labelwc['image'] = imagewc
        self._labelwc.image = imagewc


    
    def _analisis(self):
        pass
        
import tkinter as tk

class MainWindow(tk.Tk):
    
    def __init__(self, controller):

        super().__init__()
        self._controller = controller
        self.title('Word Cloud For Readers')
        self._display_frame = None
        self._txt1 = None
        self._btn1 = None
        self._create_main_frame()
        self._create_txt_input()
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
            master=self,
            text='Analizar Texto'
            )
        
        self._btn1.pack()
    
    def _analisis(self):
        pass
        
import base64
from tkinter import messagebox

import tkinter.ttk as Ttk
import tkinter as Tk


from urllib.request import urlopen







#import scraper

import scraper_intelaf_newpc as newpc


class UI:
    def __init__(self):
        messagebox.showwarning('Tiempo promedio de ejecucion',
        'Debido a que el programa realiza scraping, en algunos sitios se tuvo que implementar timers por lo que el tiempo de ejecucion aproximado es:\n \t5 MINUTOS')

        self.scraper = newpc.PC()

        self.window = Tk.Tk()
        self.window.geometry('1280x720')
        self.window.title('SCRAPPER by MR8UG')
        self.window.resizable(0,0)

        #STYLE
        color_primary = '#6002EE'
        color_complementary = '#90ee02'
        color_analog = '##d602ee'
        color_tradic = '#fff2df'
        color_white = '#FDFEFE'

        style = Ttk.Style()
 
        style.theme_create('pastel', settings={
            ".": {
                "configure": {
                    "background": '#defabb', # All except tabs
                    "font": 'red' 
                }
            },
            "TNotebook": {
                "configure": {
                    "background":'#ff0266', # Your margin color
                    "tabmargins": [2, 5, 0, 0], # margins: left, top, right, separator
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "background": '#d9ffcc', # tab color when not selected
                    "padding": [10, 2], # [space between text and horizontal tab-button border, space between text and vertical tab_button border]
                    "font":"white"
                },
                "map": {
                    "background": [("selected", '#ccffff')], # Tab color when selected
                    "expand": [("selected", [1, 1, 1, 0])] # text margins
                }
            }
        })
 
        #style.theme_use('pastel')

        self.windowBackgroundColor = '#CFD8DC'

        ###NOTEBOOK
        self.notebook = Ttk.Notebook(self.window, padding=5, width=int(1246/2), height=int(400))
        self.window.update()
        windowW = int(self.notebook.winfo_reqwidth())
        windowH = self.notebook.winfo_reqheight() 
        #print("Tamaño de ventana", windowW, windowH)

        #frames
        self.frame_procmobo = Tk.Frame(self.notebook, width=int(windowW), height=int(windowH), background=color_white)
        self.frame_video = Tk.Frame(self.notebook, width=windowW, height=windowH, background=color_white)
        self.frame_almacenamiento = Tk.Frame(self.notebook, width=windowW, height=windowH, background=color_white)

        
        #notebook para seleccionar por componente
        

        self.notebook.add(self.frame_procmobo, text='Procesador y Motherboard')
        self.notebook.add(self.frame_video, text='Tarjeta de Video')
        self.notebook.add(self.frame_almacenamiento, text='Almacenamiento')
        
        self.notebook.place(x=10, y=10)

        
        try:
            url = 'https://img.icons8.com/wired/344/computer.png'
            image_byte = urlopen(url).read()
            image_b64 = base64.encodebytes(image_byte)
            self.window.iconphoto(True, Tk.PhotoImage(data=image_b64))
        except:
            print("Error mostrando icono.")


        #Formulario

        #### PROCESADOR Y MOTHERBOARD
        self.l_tipoProcesador = Ttk.Label(self.frame_procmobo, text='Tipo de Procesador',background=color_tradic)
        self.l_tipoProcesador.place(x=50, y=50)

        self.selected_tipoProc = Tk.StringVar()
        self.combo_tipoProc = Ttk.Combobox(self.frame_procmobo)
        self.combo_tipoProc.place(x=50, y=75)
        listaTipoProc = list()
        listaTipoProc.append('Intel')
        listaTipoProc.append('AMD')
        self.combo_tipoProc['values']=listaTipoProc
        self.combo_tipoProc['state'] = 'readonly'
        self.combo_tipoProc.bind('<<ComboboxSelected>>', self.setProcesador)

        self.btn_apliProc = Tk.Button(self.frame_procmobo, text='Aplicar', command=lambda:self.setProcesador(self.combo_tipoProc.get()))
        self.btn_apliProc.place(x=200, y=75)

        

        self.l_procesador = Ttk.Label(self.frame_procmobo, text='Procesador',background=color_tradic)
        self.l_procesador.place(x=50, y=100) 
        self.combo_procesador = Ttk.Combobox(self.frame_procmobo, width=75)
        self.combo_procesador.place(x=50, y=125)
        self.combo_procesador['state'] = 'readonly'
        
        

        self.l_mobo = Ttk.Label(self.frame_procmobo, text='Tarjeta Madre',background=color_tradic)
        self.l_mobo.place(x=50, y=150)
        self.combo_mother = Ttk.Combobox(self.frame_procmobo, width=75 )
        self.combo_mother.place(x=50, y=175)
        self.combo_mother['state'] = 'readonly'

        #### TARJETA DE VIDEO
        self.l_tipoVideo = Ttk.Label(self.frame_video, text='Tipo Tarjeta de Video', background=color_tradic)
        self.l_tipoVideo.place(x=50, y=50)
        
        self.combo_tipoVid = Ttk.Combobox(self.frame_video)
        listaTipoVid = list()
        listaTipoVid.append('NVIDIA')
        listaTipoVid.append('RADEON')

        self.combo_tipoVid['values'] = listaTipoVid
        self.combo_tipoVid['state'] = 'readonly'
        self.combo_tipoVid.place(x=50,y=75)
        self.combo_tipoVid.bind('<<ComboboxSelected>>', self.setVideo)
        
        self.btn_apliVid = Tk.Button(self.frame_video, text='Aplicar', command=lambda:self.setVideo(self.combo_tipoVid.get()))
        self.btn_apliVid.place(x=200, y=100)

        self.l_tarjetaVideo = Ttk.Label(self.frame_video, text='Tarjeta de Video', background=color_tradic)
        self.l_tarjetaVideo.place(x=50, y=100)


        self.combo_video = Ttk.Combobox(self.frame_video, width=75)
        self.combo_video.place(x=50, y=125)
        self.combo_video['state'] = 'readonly'

        
        
        

        #### ALMACENAMIENTO (SSD Y HDD)
        self.l_ssd = Ttk.Label(self.frame_almacenamiento, text='SSD', background=color_tradic)
        self.l_ssd.place(x=50, y=50)
        self.combo_ssd = Ttk.Combobox(self.frame_almacenamiento, width=75)
        self.combo_ssd.place(x =50, y=75)
        self.combo_ssd['values'] = self.setSSD()
        self.combo_ssd['state'] = 'readonly'

 
        self.l_ssd_cantidad = Ttk.Label(self.frame_almacenamiento, text='Cantidad')
        self.l_ssd_cantidad.place(x=255, y= 50)
        self.combo_ssd_cantidad = Ttk.Combobox(self.frame_almacenamiento, width=10)
        self.combo_ssd_cantidad.place(x=325, y=50)
        self.combo_ssd_cantidad['values'] = ['0','1','2','3','4','5','6']
        self.combo_ssd_cantidad['state'] = 'readonly'
       
        self.l_hdd = Ttk.Label(self.frame_almacenamiento, text='HDD', background=color_tradic)
        self.l_hdd.place(x=50, y=100)
        self.combo_hdd = Ttk.Combobox(self.frame_almacenamiento, width=75)
        self.combo_hdd.place(x =50, y=125)
        self.combo_hdd['values'] = self.setHDD()
        self.combo_hdd['state'] = 'readonly'

 
        self.l_hdd_cantidad = Ttk.Label(self.frame_almacenamiento, text='Cantidad')
        self.l_hdd_cantidad.place(x=255, y= 100)
        self.combo_hdd_cantidad = Ttk.Combobox(self.frame_almacenamiento, width=10)
        self.combo_hdd_cantidad.place(x=325,y=100)
        self.combo_hdd_cantidad['values'] = ['0','1','2','3','4','5','6']
        self.combo_hdd_cantidad['state'] = 'readonly'






    def run(self):
        self.window.config(background='#5D6D7E')
        self.window.mainloop()

    def setProcesador(self, event):
        tipo = self.combo_tipoProc.get()
        print("TIPO Seleccionado: ",str(tipo))
        combo_procesador_values = list()
        combo_mother_values = list()
        if(tipo =='Intel'):
            for c in self.scraper.getProcIntel():
                combo_procesador_values.append(str(c['nombre']).replace('PROCESADOR ','') + ' ---| \t Q' + str(c['precio_normal']))
            self.combo_procesador['values'] = combo_procesador_values

            

            for c in self.scraper.getMoboIntel():
                combo_mother_values.append(str(c['nombre']).replace('MBOARD ','')+ ' ---| \t Q' + str(c['precio_normal']))
            self.combo_mother['values'] = combo_mother_values

        if(tipo =='AMD'):
            for c in self.scraper.getProcAMD():
                combo_procesador_values.append(str(c['nombre']).replace('PROCESADOR ','')+ ' ---| \t Q' + str(c['precio_normal']))
            self.combo_procesador['values'] = combo_procesador_values

            for c in self.scraper.getMoboAMD():
                combo_mother_values.append(str(c['nombre']).replace('MBOARD ','')+ ' ---| \t Q' + str(c['precio_normal']))
            self.combo_mother['values'] = combo_mother_values
    
    def setVideo(self, event):
        tipo = self.combo_tipoVid.get()
        combo_video = list()

        if(tipo == 'NVIDIA'):
            for c in self.scraper.getNVidiaCards():
                combo_video.append(str(c['nombre']).replace('TARJ VIDEO','')+ ' ---| \t Q' + str(c['precio_normal']))

            self.combo_video['values'] = combo_video

        if(tipo == 'RADEON'):
            for c in self.scraper.getRadeonCards():
                combo_video.append(str(c['nombre']).replace('TARJ VIDEO','')+ ' ---| \t Q' + str(c['precio_normal']))

            self.combo_video['values'] = combo_video

    def setSSD(self):
        combo_ssd = list()
        for c in self.scraper.getSSDs():
            combo_ssd.append(str(c['nombre']) + ' ---| \t Q' + str(c['precio_normal']))
        
        return combo_ssd

    def setHDD(self):
        combo_hdd = list()
        for c in self.scraper.getHDDs():
            combo_hdd.append(str(c['nombre']) + ' ---| \t Q' + str(c['precio_normal']))

        return combo_hdd

    
ui = UI()
ui.run()
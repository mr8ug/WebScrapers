import base64

import os
import re
import subprocess

import tkinter.ttk as Ttk
import tkinter as Tk
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename
from tkinter import Button, Canvas, Frame, Scrollbar, Widget, messagebox, scrolledtext
from urllib.request import urlopen






#import scraper

import scraper_intelaf_newpc as newpc


class UI:
    def __init__(self):
        self.scraper = newpc.PC()

        self.window = Tk.Tk()
        self.window.geometry('1280x720')
        self.window.title('SCRAPPER by MR8UG')
        self.window.resizable(0,0)

        try:
            url = 'https://img.icons8.com/wired/344/computer.png'
            image_byte = urlopen(url).read()
            image_b64 = base64.encodebytes(image_byte)
            self.window.iconphoto(True, Tk.PhotoImage(data=image_b64))
        except:
            print("Error mostrando icono.")


        #Formulario
        self.l_tipoProcesador = Ttk.Label(self.window, text='Tipo de Procesador',background='#A1CDCC')
        self.l_tipoProcesador.place(x=50, y=50)

        self.selected_tipoProc = Tk.StringVar()
        self.combo_tipoProc = Ttk.Combobox(self.window)
        self.combo_tipoProc.place(x=50, y=75)
        listaTipo = list()
        listaTipo.append('Intel')
        listaTipo.append('AMD')
        self.combo_tipoProc['values']=listaTipo
        self.combo_tipoProc['state'] = 'readonly'

        self.btn_apliProc = Tk.Button(self.window, text='Aplicar', command=lambda:self.setProcesador(self.combo_tipoProc.get()))
        self.btn_apliProc.place(x=200, y=75)

        

        self.l_procesador = Ttk.Label(self.window, text='Procesador',background='#A1CDCC')
        self.l_procesador.place(x=50, y=125) 
        self.combo_procesador = Ttk.Combobox(self.window, postcommand=self.setProcesador(self.combo_tipoProc.get()), width=75)
        self.combo_procesador.place(x=50, y=150)
        self.combo_procesador['state'] = 'readonly'
        

        self.l_mobo = Ttk.Label(self.window, text='Tarjeta Madre',background='#A1CDCC')
        self.l_mobo.place(x=50, y=175)
        self.combo_mother = Ttk.Combobox(self.window, postcommand=self.setProcesador(self.combo_tipoProc.get()), width=75 )
        self.combo_mother.place(x=50, y=200)
        self.combo_mother['state'] = 'readonly'


    def run(self):
        self.window.config(background='#A1CDCC')
        self.window.mainloop()

    def setProcesador(self, tipo):
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
    
    
ui = UI()
ui.run()
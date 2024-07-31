from tkinter import *
from tkinter import ttk
from time import strftime
from googletrans import Translator
translate=Translator()
def actualizar_reloj():
    dia=translate.translate(strftime("%A"),dest='es').text
    etiqueta_hm.config(text=strftime("%H:%M"))
    etiqueta_s.config(text=strftime("%S"))
    etiqueta_fecha.config(text=strftime(f"{dia}, %d/%m/%y"))
    etiqueta_s.after(1000,actualizar_reloj)
ventana=Tk()
ventana.title("Reloj")
ventana.config(bg='black')
frame_hora=Frame(bg='black')
frame_hora.pack()
etiqueta_hm=Label(frame_hora, font=('LED Real',100),text="h:m",fg='blue', bg='black')
etiqueta_hm.grid(row=0,column=1,sticky="n")

etiqueta_s=Label(frame_hora, font=("LED Real", 50),text="s",fg='blue', bg='black')
etiqueta_s.grid(row=0,column=2,sticky="n")

etiqueta_fecha=Label(font=("LED Real", 50),text=("dia""d/m/aaaa"),fg='blue', bg='black')
etiqueta_fecha.pack(anchor="center")

actualizar_reloj()
ventana.mainloop()
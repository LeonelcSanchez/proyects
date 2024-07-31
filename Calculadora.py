from tkinter import *
ventana=Tk()
ventana.title("Calculadora")
ventana.config(bg='black')
i=0
e_texto= Entry(ventana,bg='black',fg='white')
e_texto.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

def click_botones(valor):
    global i
    e_texto.insert(i,valor)
    i+=1
def borrar():
    e_texto.delete(0,END)
    i=0
def operaciones():
    ecuacion=e_texto.get()
    resultado=eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    i=0
boton1=Button(ventana,text="1",width=5,height=2,command=lambda:click_botones(1),bg='#3B526B',fg='white')
boton2=Button(ventana,text="2",width=5,height=2,command=lambda:click_botones(2),bg='#3B526B',fg='white')
boton3=Button(ventana,text="3",width=5,height=2,command=lambda:click_botones(3),bg='#3B526B',fg='white')
boton4=Button(ventana,text="4",width=5,height=2,command=lambda:click_botones(4),bg='#3B526B',fg='white')
boton5=Button(ventana,text="5",width=5,height=2,command=lambda:click_botones(5),bg='#3B526B',fg='white')
boton6=Button(ventana,text="6",width=5,height=2,command=lambda:click_botones(6),bg='#3B526B',fg='white')
boton7=Button(ventana,text="7",width=5,height=2,command=lambda:click_botones(7),bg='#3B526B',fg='white')
boton8=Button(ventana,text="8",width=5,height=2,command=lambda:click_botones(8),bg='#3B526B',fg='white')
boton9=Button(ventana,text="9",width=5,height=2,command=lambda:click_botones(9),bg='#3B526B',fg='white')
boton0=Button(ventana,text="0",width=13,height=2,command=lambda:click_botones(0),bg='#3B526B',fg='white')

boton_borrar=Button(ventana,text="AC",width=5,height=2,command=lambda:borrar(),bg='#032B44',fg='red')
boton_parentesis1=Button(ventana,text="(",width=5,height=2,command=lambda:click_botones("("),bg='#032B44',fg='green')
boton_parentesis2=Button(ventana,text=")",width=5,height=2,command=lambda:click_botones(")"),bg='#032B44',fg='green')
boton_punto=Button(ventana,text=".",width=5,height=2,command=lambda:click_botones("."),bg='#032B44',fg='green')

boton_div=Button(ventana,text="/",width=5,height=2,command=lambda:click_botones("/"),bg='#032B44',fg='green')
boton_mult=Button(ventana,text="x",width=5,height=2,command=lambda:click_botones("*"),bg='#032B44',fg='green')
boton_sum=Button(ventana,text="+",width=5,height=2,command=lambda:click_botones("+"),bg='#032B44',fg='green')
boton_rest=Button(ventana,text="-",width=5,height=2,command=lambda:click_botones("-"),bg='#032B44',fg='green')
boton_igual=Button(ventana,text="=",width=5,height=2,command=lambda:operaciones(),bg='green',fg='white')

boton_borrar.grid(row=1,column=0,padx=5,pady=5)
boton_parentesis1.grid(row=1,column=1,padx=5,pady=5)
boton_parentesis2.grid(row=1,column=2,padx=5,pady=5)
boton_div.grid(row=1,column=3,padx=5,pady=5)

boton7.grid(row=2,column=0,padx=5,pady=5)
boton8.grid(row=2,column=1,padx=5,pady=5)
boton9.grid(row=2,column=2,padx=5,pady=5)
boton_mult.grid(row=2,column=3,padx=5,pady=5)

boton4.grid(row=3,column=0,padx=5,pady=5)
boton5.grid(row=3,column=1,padx=5,pady=5)
boton6.grid(row=3,column=2,padx=5,pady=5)
boton_sum.grid(row=3,column=3,padx=5,pady=5)

boton1.grid(row=4,column=0,padx=5,pady=5)
boton2.grid(row=4,column=1,padx=5,pady=5)
boton3.grid(row=4,column=2,padx=5,pady=5)
boton_rest.grid(row=4,column=3,padx=5,pady=5)

boton0.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
boton_punto.grid(row=5,column=2,padx=5,pady=5)
boton_igual.grid(row=5,column=3,padx=5,pady=5)


ventana.mainloop()
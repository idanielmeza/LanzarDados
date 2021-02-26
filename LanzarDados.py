from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Lanzador de dados')
root.resizable(0,0)
root.iconbitmap('dado.ico')

global dadoUno
global dadoDos

caraUno = PhotoImage(file='d1.png').subsample(2,2)
caraDos = PhotoImage(file='d2.png').subsample(2,2)
caraTres = PhotoImage(file='d3.png').subsample(2,2)
caraCuatro = PhotoImage(file='d4.png').subsample(2,2)
caraCinco = PhotoImage(file='d5.png').subsample(2,2)
caraSeis = PhotoImage(file='d6.png').subsample(2,2)

def lanzarUno():
	dadoUno = random.randint(1,6)
	botonLanzar['text'] = 'Volver a lanzar dados'	

	if dadoUno == 1:
		dadoUnoLabel['image'] = caraUno

	elif dadoUno == 2:
		dadoUnoLabel['image'] = caraDos

	elif dadoUno == 3:
		dadoUnoLabel['image'] = caraTres

	elif dadoUno == 4:
		dadoUnoLabel['image'] = caraCuatro

	elif dadoUno == 5:
		dadoUnoLabel['image'] = caraCinco

	elif dadoUno == 6:
		dadoUnoLabel['image'] = caraSeis

	return dadoUno

def lanzarDos():
	dadoDos = random.randint(1,6)

	if dadoDos == 1:
		dadoDosLabel['image'] = caraUno

	elif dadoDos == 2:
		dadoDosLabel['image'] = caraDos

	elif dadoDos == 3:
		dadoDosLabel['image'] = caraTres

	elif dadoDos == 4:
		dadoDosLabel['image'] = caraCuatro

	elif dadoDos == 5:
		dadoDosLabel['image'] = caraCinco

	elif dadoDos == 6:
		dadoDosLabel['image'] = caraSeis

	return dadoDos

def monitorFun():
	primero = lanzarUno()
	segundo = lanzarDos()
	monitor['fg'] = 'blue' 
	monitor['text'] = '{} 	     {}'.format(primero,segundo)
	monitor['font'] = ('Aharoni',25)
	

monitor = Label(root, text= 'Lanza los dados', fg = 'black', font =('Aharoni',20))
monitor.grid(row=0, column=0, columnspan=2)

dadoUnoLabel = Label(root, image= caraUno)
dadoUnoLabel.grid(row=1, column=0)
dadoDosLabel = Label(root, image= caraDos)
dadoDosLabel.grid(row=1, column=1)

botonLanzar = ttk.Button(root, text = 'Lanzar Dados',command = lambda:[lanzarUno(), lanzarDos(), monitorFun()], width= 25)
botonLanzar.grid(row=2, column=0, columnspan=2)





root.mainloop()
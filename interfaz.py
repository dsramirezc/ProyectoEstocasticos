try:
    from tkinter import *  # Python 3.x
except :
    from Tkinter import *  # Python 2.x

# Clase para hacer la interfaZ grafica
class Ventana: #Se crea clase ventana la cual va realizar la interfas gráfica.  
    def __init__(self, master):
        self.master = master #Creando objeto (gráfica) 
        master.title("GUI") #Nombre de ventana 
        master.geometry("600x500") #  Tamaño de ventana
        master['bg'] = '#4A5160'.upper() #Color de background
        color= '#4A5160'.upper() #Color azúl de botón
        color1="#5870B3".upper() #Color azúl de bóton 
        self.va = Label(master, text="Bienvenido a la interfaz del proyecto ",height=2,bg=color) #Label donde aparece mensaje.
        self.va.pack() # Se añade mensaje a la ventanda. 
        x1=30 #Margen de x del cuadro n.
        y1=40# Margen de y del cuadro n.
        x2=145
        deltaX=50
        deltaY=30
        auxx=105
        self.lab1 =Label(master, text="Numero de nodos:",width=20,bg=color).place(x=x1+40,y=50)
        #self.l3 = Label(master, text="nodos ",width=7,bg=color).place(x=x1-10+auxx*2,y=deltaY*2+y1) #Margen superior de n, otro label. 
        x1=0
        self.nodos = Entry(width=6)
        self.nodos.insert(END,11)#pasar de grados a radianes
        self.nodos.place(x=x1-10+deltaX+auxx*2,y=deltaY*2+y1) #Objeto Entry de la interfaz.
        self.lab2 =Label(master, text="Alpha:",width=40,bg=color).place(x=x1,y=150) 
        #self.a2 =Label(master, text="a",width=7,bg=color).place(x=x1-10+auxx*2,y=deltaY*2+y1+100) #Margen superior de n, otro label. 
        self.alpha = Entry(width=6)
        self.alpha.insert(END,0.8)#valor predeterminado
        self.alpha.place(x=x1-10+deltaX+auxx*2,y=deltaY*2+y1+100) #Objeto Entry de la interfaz.
        self.lab3 =Label(master, text="Numero de servidores:",width=28,bg=color).place(x=50,y=250)
        self.nraices= Entry(width=6)
        self.nraices.insert(END,0)#pasar de grados a radianes
        self.nraices.place(x=x1-10+deltaX+auxx*2,y=deltaY*2+y1+200) #Objeto Entry de la interfaz.
        self.lab4 =Label(master, text="Numero de redes a generar:",width=30,bg=color).place(x=50,y=350) 
        self.nredes = Entry(width=6)
        self.nredes.insert(END,0)#pasar de grados a radianes
        self.nredes.place(x=x1-10+deltaX+auxx*2,y=deltaY*2+y1+300) #Objeto Entry de la interfaz.
        self.generar = Button(master, text="Generar",width=6,command=self.generar,highlightbackground=color1).place(x=280-100,y=440)     # Se crea animar con el botón animar, el color que de fondo y de nuevo, se llama la función de más abajo animar
        self.guardarDatos = Button(master, text="Guardar redes",width=20,highlightbackground=color1,command=self.guardarDatos).place(x=280+50,y=440)     # Se crea animar con el botón animar, el color que de fondo y de nuevo, se llama la función de más abajo animar

    #funcion para realizar las diferentes graficas 
    def generar(self):
        parameters = [int(self.nodos.get()),int(self.alpha.get()),int(self.nraices.get()),int(self.nredes.get())]
        return True
    def guardarDatos(self):

        #guarda los datos de las redes
        return True
root = Tk()
Ventana(root)
root.mainloop()

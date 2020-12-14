import csv

try:
    from tkinter import *  # Python 3.x
except :
    from Tkinter import *  # Python 2.x

from proyectoLenguajes import RandomGraph

# Clase para hacer la interfaZ grafica
class Ventana: #Se crea clase ventana la cual va realizar la interfas gráfica.  
    graphs = []
    def __init__(self, master):
        self.master = master #Creando objeto (gráfica) 
        master.title("GUI") #Nombre de ventana 
        master.geometry("600x500") #  Tamaño de ventana
        master['bg'] = '#4A5160'.upper() #Color de background
        color= '#4A5160'.upper() #Color azúl de botón
        color1="#9F9FA0".upper() #Color azúl de bóton 
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
        self.generar = Button(master, text="Generar",width=6,command=self.generar,highlightbackground=color1).place(x=250-100,y=440)     # Se crea animar con el botón animar, el color que de fondo y de nuevo, se llama la función de más abajo animar
        self.reiniciar = Button(master, text="Reiniciar",width=20,highlightbackground=color1,command=self.reboot).place(x=280+50,y=380)     # Se crea animar con el botón animar, el color que de fondo y de nuevo, se llama la función de más abajo animarreu
        self.guardarDatos = Button(master, text="Guardar redes",width=20,highlightbackground=color1,command=self.guardarDatos).place(x=280+50,y=440)     # Se crea animar con el botón animar, el color que de fondo y de nuevo, se llama la función de más abajo animar
    #funcion para realizar las diferentes graficas 
    def generar(self):
        redes = int(self.nredes.get())
        parameters = [int(self.nodos.get()),float(self.alpha.get()),int(self.nraices.get())]
        for i in range(redes):
            rg = RandomGraph(parameters[0],parameters[1],parameters[2])
            self.graphs.append(rg)
        for i in self.graphs:
            # i.colorgraph()
            print(i.articulationPoints)
        return True
    def guardarDatos(self):
        import csv
        with open('graphs.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Num", "N. roots", "N. nodes", "Alpha", "N. edges", "N. Bridge", "N. Articulation points", "Disperse", "Dense","Max Deep", "N. disconected nodes"])
            i =0
            for g in self.graphs:
                writer.writerow([i,len(g.roots),g.nodes,g.alpha,g.edges,len(g.bridges),len(g.articulationPoints),g.isDisperse(),g.isDense(),g.maxDepth,len(g.disconectednodes)])
                i+=1
        #guarda los datos de las redes
        return True
    def reboot(self):
        print("reboot")
        self.graphs = []
        return True
root = Tk()
Ventana(root)
root.mainloop()

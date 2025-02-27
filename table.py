import tkinter as tk
import time
import json
class Table(tk.LabelFrame):
    graphs=[]
    def __init__(self,*args, **kwargs):
        self.graphs=args[1]
        tk.LabelFrame.__init__(self, args[0], **kwargs)
        data = [
            ]
        index=1
        for i in self.graphs:
            data.append([index,i.nodes,i.nroots,i.alpha,i.edges,len(i.bridges),
                        len(i.articulationPoints),i.isDisperse(),i.isDense(),i.maxDepth,len(set(i.disconectednodes))])
            index+=1
        self.grid_columnconfigure(1, weight=1)
        tk.Label(self, text="id", anchor="w").grid(row=0, column=0, sticky="ew")
        tk.Label(self, text="nodos", anchor="w").grid(row=0, column=1, sticky="ew")
        tk.Label(self, text="raices", anchor="w").grid(row=0, column=2, sticky="ew")
        tk.Label(self, text="alpha", anchor="w").grid(row=0, column=3, sticky="ew")
        tk.Label(self, text="conexiones", anchor="w").grid(row=0, column=4, sticky="ew")
        tk.Label(self, text="puentes", anchor="w").grid(row=0, column=5, sticky="ew")
        tk.Label(self, text="articulaciones", anchor="w").grid(row=0, column=6, sticky="ew")
        tk.Label(self, text="Disperso", anchor="w").grid(row=0, column=7, sticky="ew")
        tk.Label(self, text="Denso", anchor="w").grid(row=0, column=8, sticky="ew")
        tk.Label(self, text="Deep", anchor="w").grid(row=0, column=9, sticky="ew")
        tk.Label(self, text="Disconected nodes", anchor="w").grid(row=0, column=10, sticky="ew")
        tk.Label(self, text="ver datos", anchor="w").grid(row=0, column=11, sticky="ew")
        tk.Label(self, text="exportar", anchor="w").grid(row=0, column=12, sticky="ew")

        row = 1
        for (nr,nodes,raices,alpha,aristas,puentes,articulaciones,disperso,denso,maxProfundidad,innodes) in data:
            nr_label = tk.Label(self, text=nr, anchor="w")
            nodes_label = tk.Label(self, text=nodes, anchor="w")
            raices_label = tk.Label(self, text=raices, anchor="w")
            alpha_label = tk.Label(self, text=alpha, anchor="w")
            aristas_label = tk.Label(self, text=aristas, anchor="w")
            puentes_label = tk.Label(self, text=puentes, anchor="w")
            articulaciones_label = tk.Label(self, text=articulaciones, anchor="w")
            disperso_label = tk.Label(self, text=disperso, anchor="w")
            denso_label = tk.Label(self, text=denso, anchor="w")
            maxProfundidad_label = tk.Label(self, text=maxProfundidad, anchor="w")
            innodes_label = tk.Label(self, text=innodes, anchor="w")
            action_button = tk.Button(self, text="graficar", command=lambda nr=nr: self.graficar(nr-1))
            export_button = tk.Button(self, text="exportar", command=lambda nr=nr: self.exportar(nr-1))

            nr_label.grid(row=row, column=0, sticky="ew")
            nodes_label.grid(row=row, column=1, sticky="ew")
            raices_label.grid(row=row, column=2, sticky="ew")
            alpha_label.grid(row=row, column=3, sticky="ew")
            aristas_label.grid(row=row, column=4, sticky="ew")
            puentes_label.grid(row=row, column=5, sticky="ew")
            articulaciones_label.grid(row=row, column=6, sticky="ew")
            disperso_label.grid(row=row, column=7, sticky="ew")
            denso_label.grid(row=row, column=8, sticky="ew")
            maxProfundidad_label.grid(row=row, column=9, sticky="ew")
            innodes_label.grid(row=row, column=10, sticky="ew")
            action_button.grid(row=row, column=11, sticky="ew")
            export_button.grid(row=row, column=12, sticky="ew")
            row += 1
    def graficar(self, x):
        print(x)
        self.graphs[x].colorgraph()
    def exportar(self,x):
        title = "Graph-" +str(x) +".json"
        data = self.graphs[x].exportar()
        with open(title, 'w') as o:
            json.dump(data, o)

import p2_metodo_nuevo as p1
import parte2_p2 as p2
import matplotlib.pyplot as plt
import tkinter as tk

#Grafica
#Entradas:
            #listaValoresX: valores que se graficaran en el eje 'x'
            #listaValoresY: valores que se graficaran en el eje 'y'
#Salidas:
            #Grafico con los valores ingresados
def grafica(listaValoresX, listaValoresY):
    plt.plot(listaValoresX, listaValoresY, 'bx')
    plt.title("Metodo de Newton-Raphson")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()

root = tk.Tk()
root.title("Calculadora de Ecuaciones No Lineales")
e = tk.Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
button_1 = Button(root, text = "Metodo Nuevo", padx = 40, pady = 20, command = p1.metodo_nuevo(f, x0, 15, 0.0001))
button_2 = Button(root, text = "Metodo Nuevo", padx = 40, pady = 20, command = p1.metodo_nuevo(f, x0, 15, 0.0001))
button_3 = Button(root, text = "Metodo Nuevo", padx = 40, pady = 20, command = p1.metodo_nuevo(f, x0, 15, 0.0001))
button_4 = Button(root, text = "Metodo Nuevo", padx = 40, pady = 20, command = p1.metodo_nuevo(f, x0, 15, 0.0001))

if __name__ == '__main__':
    root.mainloop()
    print("################################################")

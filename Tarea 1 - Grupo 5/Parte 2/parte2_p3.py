import parte2_p2 as p2
import tkinter as tk

# Intervalos
x0 = 0
a = 1/2
b = (p2.math.pi)/4
# Tolerancia
tol = 1e-10
# Maximo iteraciones
iterMax = 100
# Funcion
f = lambda x: p2.math.cos(x) - x

#Se crea la ventana de Tkinter
root = tk.Tk()
root.title("Calculadora de Ecuaciones No Lineales")

#Se crean los labels de la interfaz
e_func = tk.Entry(root, width = 35, borderwidth = 5)
e_func.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
e_valor_inicial = tk.Entry(root, width = 35, borderwidth = 5)
e_valor_inicial.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)
e_primer_intervalo = tk.Entry(root, width = 35, borderwidth = 5)
e_primer_intervalo.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 10)
e_segundo_intervalo = tk.Entry(root, width = 35, borderwidth = 5)
e_segundo_intervalo.grid(row = 3, column = 0, columnspan = 3, padx = 10, pady = 10)
e_tolerancia = tk.Entry(root, width = 35, borderwidth = 5)
e_tolerancia.grid(row = 4, column = 0, columnspan = 3, padx = 10, pady = 10)
e_iter_max = tk.Entry(root, width = 35, borderwidth = 5)
e_iter_max.grid(row = 5, column = 0, columnspan = 3, padx = 10, pady = 10)

#Función del botón del nuevo método
def button_ren():
    global option
    try:
        option = "Ren"
    except ValueError:
        print("Oops, do it again!")

#Función del botón del nuevo método
def button_biseccion():
    global option
    try:
        option = "Biseccion"
    except ValueError:
        print("Oops, do it again!")

#Función del botón del método de Newton-Raphson 
def button_newton():
    global option
    try:
        option = "Newton-Raphson"
    except ValueError:
        print("Oops, do it again!")

#Función del botón del método de la secante 
def button_secante():
    global option
    try:
        option = "Secante"
    except ValueError:
        print("Oops, do it again!")

#Función del botón del método de la falsa posición 
def button_posicion():
    global option
    try:
        option = "Falsa Posicion"
    except ValueError:
        print("Oops, do it again!")

#Función del botón para calcular funciones
def button_calcular():
    try:
        if option == "Ren":
            p2.metodo_nuevo(f, x0, iterMax, tol)
        elif option == "Biseccion":
            p2.biseccion(f, a, b, iterMax, tol)
        elif option == "Newton-Raphson":
            p2.newton_raphson(f, x0, iterMax, tol)
        elif option == "Secante":
            p2.secante(f, a, b, iterMax, tol)
        elif option == "Falsa Posicion":
            p2.falsa_posicion(f, a, b, iterMax, tol)
    except ValueError:
        print("Oops, do it again!")

#Función del botón para limpiar los labels 
def button_clear():
    try:
        e_func.delete(0, tk.END)
        e_valor_inicial.delete(0, tk.END)
        e_primer_intervalo.delete(0, tk.END)
        e_segundo_intervalo.delete(0, tk.END)
        e_tolerancia.delete(0, tk.END)
        e_iter_max.delete(0, tk.END)
    except ValueError:
        print("Oops, do it again!")

#Se definen todos los botones
button_1 = tk.Button(root, text = "Metodo Nuevo", padx = 40, pady = 20, command = lambda: button_ren())
button_2 = tk.Button(root, text = "Biseccion", padx = 40, pady = 20, command = lambda : button_biseccion())
button_3 = tk.Button(root, text = "Newton-Raphson", padx = 40, pady = 20, command = lambda : button_newton())
button_4 = tk.Button(root, text = "Secante", padx = 40, pady = 20, command = lambda : button_secante())
button_5 = tk.Button(root, text = "Falsa Posicion", padx = 40, pady = 20, command = lambda : button_posicion())
button_6 = tk.Button(root, text = "Calcular", padx = 40, pady = 20, command = lambda : button_calcular())
button_7 = tk.Button(root, text = "Clear", padx = 40, pady = 20, command = lambda : button_clear())

#Se agregan todos los botones a la interfaz
button_1.grid(row = 1, column = 3)
button_2.grid(row = 3, column = 3)
button_3.grid(row = 5, column = 3)
button_4.grid(row = 1, column = 5)
button_5.grid(row = 3, column = 5)
button_6.grid(row = 5, column = 5)
button_7.grid(row = 7, column = 5)

if __name__ == '__main__':
    root.mainloop()



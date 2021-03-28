import p2_metodo_nuevo as p1
import parte2_p2 as p2
import tkinter as tk

# Intervalos
x0 = 0
a = 1/2
b = (p2.math.pi)/4
# Tolerancia
tol = 0.00001
# Maximo iteraciones
iterMax = 100
# Funcion
f = lambda x: p2.math.cos(x) - x
iteraciones = []
errores = []

#Se crea la ventana de Tkinter
root = tk.Tk()
root.title("Calculadora de Ecuaciones No Lineales")

#Se crean los labels de la interfaz
e = tk.Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

#Función del botón del nuevo método
def button_ren():
    try:
        p1.metodo_nuevo(f, x0, 15, 0.0001)
    except ValueError:
        print("Oops, do it again!")

#Función del botón del método de Newton-Raphson 
def button_newton():
    try:
        p2.newton_raphson(f, x0, 15, 0.0001)
    except ValueError:
        print("Oops, do it again!")

#Función del botón del método de la secante 
def button_secante():
    try:
        p2.secante(f, a, b, 15, 0.0001)
    except ValueError:
        print("Oops, do it again!")

#Función del botón del método de la falsa posición 
def button_posicion():
    try:
        p2.falsa_posicion(f, a, b, 15, 0.0001)
    except ValueError:
        print("Oops, do it again!")

#Función del botón para calcular funciones
def button_calcular():
    try:
        print("Hello World!")
    except ValueError:
        print("Oops, do it again!")

#Función del botón para limpiar los labels 
def button_clear():
    try:
        e.delete(0, tk.END)
    except ValueError:
        print("Oops, do it again!")

#Se definen todos los botones
button_1 = tk.Button(root, text = "Metodo Nuevo", padx = 40, pady = 20, command = lambda: button_ren())
button_2 = tk.Button(root, text = "Newton-Raphson", padx = 40, pady = 20, command = lambda : button_newton())
button_3 = tk.Button(root, text = "Secante", padx = 40, pady = 20, command = lambda : button_secante())
button_4 = tk.Button(root, text = "Falsa Posicion", padx = 40, pady = 20, command = lambda : button_posicion())
button_5 = tk.Button(root, text = "Calcular", padx = 40, pady = 20, command = lambda : button_calcular)
button_5 = tk.Button(root, text = "Clear", padx = 40, pady = 20, command = button_clear)

#Se agregan todos los botones a la interfaz
button_1.grid(row = 3, column = 3)
button_2.grid(row = 4, column = 3)
button_3.grid(row = 5, column = 3)
button_4.grid(row = 6, column = 5)
button_5.grid(row = 8, column = 5)

if __name__ == '__main__':
    root.mainloop()



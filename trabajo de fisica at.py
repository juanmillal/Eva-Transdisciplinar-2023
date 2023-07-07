import tkinter as tk
import math
from tkinter import messagebox

#----------------------
# Ventana
#-----------------------
# su creacion, dimensiones y color respectivamente.
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.configure(background= "medium sea green")
#-------------------------
# Comienzo del trabajo
#-------------------------
#titulo del trabajo  
titulo = tk.Label (ventana,text = "trabajo de fisica", bg = "pink")
titulo.pack(fill= tk.X)
#columna azul
columna = tk.Canvas(ventana, width=200, height=600)
columna.place(x=0, y=0)
columna.create_rectangle(0, 0, 200, 800, fill='blue')

def cal_acereracion(d_angulo,d_masa,d_roce=0):

    peso= d_masa *9.8 
    p_y = d_masa* math.sin(d_angulo)
    radianes = (d_angulo * math.pi) / 180 
    p_x = peso*math.cos(radianes)

    if d_roce < 0 or d_roce > 1:
        raise ValueError("El coeficiente de roce debe estar entre 0 y 1")
    if d_angulo < 1 or d_angulo > 90:
        raise ValueError("El angulo debe estar entre 1 y 89 grados")
    
    N = p_y
    roce = round(N * d_roce, 2)
    # Calcular la fuerza neta (componente x del peso menos la fuerza de roce)
    fuerza_neta = round(p_x - roce, 2)
    fuerza_neta = max(fuerza_neta, 0)
    # Calcular la aceleración con roce
    aceleracion = round(fuerza_neta / d_masa, 2)

    return aceleracion, round(d_masa, 2), d_angulo, roce, fuerza_neta, round(p_x, 2), round(p_y, 2)


def dibujar_triangulo(angulo):
    canvas.delete("triangulo")  # Borra cualquier triángulo dibujado previamente

    #Convertir el ángulo a radianes
    radianes = math.radians(angulo)

    #Coordenadas del vértice del ángulo agudo
    x1 = 40
    y1 = 450

    #Longitud del cateto adyacente y cateto opuesto
    cateto_adyacente = 420
    cateto_opuesto = cateto_adyacente * math.tan(radianes)

    #Coordenadas del segundo vértice (en el cateto adyacente)
    x2 = x1 + cateto_adyacente
    y2 = y1

    #Coordenadas del tercer vértice (en el triangulo)
    x3 = x1
    y3 = y1 - cateto_opuesto

    #Dibujar el triángulo en el recuadro
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="black", fill="lightblue", tags="triangulo")

def dibujar_cuadrado():
    canvas.create_rectangle(150, 120, 250, 180, outline="black",fill="black") 


def cal_button():
    try:
        d_masa = float(V_masa.get())
        d_angulo = float(V_Ángulo.get())
        d_roce = float(V_Roce.get())

        aceleracion, masa_objeto, angulo_objeto, roce, fuerza_neta, pesox, pesoy = cal_acereracion(d_angulo, d_masa, d_roce)

        resultado_text.set(f"Aceleración: {aceleracion}\n"
                           f"Masa: {masa_objeto}\n"
                           f"Ángulo: {angulo_objeto}\n"
                           f"Fuerza de Roce = (N x μ) = {roce}\n"
                           f"Fuerza Neta: P + N + Fr = {fuerza_neta}\n"
                           f"Peso en X = P x sen(α) = {pesox}\n"
                           f"Peso en Y = P x cos(α) = {pesoy}")
        
        dibujar_triangulo(d_angulo)
        dibujar_cuadrado()
    except ValueError as e:
        messagebox.showerror("Error", str(e))


T_datos= tk.Label (ventana, text="ingrese los siguiente datos ")
T_datos.place(x=25, y=55)
#ventana del masa
vmasa= tk.Label (ventana, text="ingrese la masa")
vmasa.place(x=50, y=100)
# Crear caja de texto.
V_masa = tk.Entry()
# Posicionarla en la ventana.
V_masa.place(x=50, y=125)

#ventana del ángulo
vángulo= tk.Label (ventana, text="ingrese el ángulo")
vángulo.place(x=50, y=150)
# Crear caja de texto.
V_Ángulo = tk.Entry()
# Posicionarla en la ventana.
V_Ángulo.place(x=50, y=175)

#ventana de roce 
vroce= tk.Label (ventana, text="ingrese la el roce")
vroce.place(x=50, y=200)
# Crear caja de texto.
V_Roce = tk.Entry()
# Posicionarla en la ventana.
V_Roce.place(x=50, y=225)

#texto del resultado
resultado_text = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=resultado_text )
label_resultado.place(x=20, y=305)
#Variable de texto para mostrar el resultado

#boton de calcular
button = tk.Button(ventana,text="Mostrar resultado", command=cal_button)
button.place(x=70, y=250)

canvas = tk.Canvas(ventana, width=380, height=500)
canvas.pack()


ventana.resizable(False,False)
#inicia un bucle en la interfaz gráfica
ventana.mainloop()
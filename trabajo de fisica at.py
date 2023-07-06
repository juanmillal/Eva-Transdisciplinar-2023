import tkinter as tk
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

#variable iniciales 
masa = 0 
ace = 0 
pes_X = 0 
pes_Y = 0
T_datos= tk.Label (ventana, text="ingrese los siguiente datos ")
T_datos.place(x=25, y=55)
#ventana del peso
peso= tk.Label (ventana, text="ingrese la peso")
peso.place(x=50, y=100)
# Crear caja de texto.
V_peso = tk.Entry()
# Posicionarla en la ventana.
V_peso.place(x=50, y=125)

#ventana del ángulo
ángulo= tk.Label (ventana, text="ingrese el ángulo")
ángulo.place(x=50, y=150)
# Crear caja de texto.
V_Ángulo = tk.Entry()
# Posicionarla en la ventana.
V_Ángulo.place(x=50, y=175)

#ventana de roce 
roce= tk.Label (ventana, text="ingrese la el roce")
roce.place(x=50, y=200)
# Crear caja de texto.
V_Roce = tk.Entry()
# Posicionarla en la ventana.
V_Roce.place(x=50, y=225)

#boton de calcular
button = tk.Button(text="calcular")
button.place(x=70, y=250)

ventana.resizable(False,False)
#inicia un bucle en la interfaz gráfica
ventana.mainloop()
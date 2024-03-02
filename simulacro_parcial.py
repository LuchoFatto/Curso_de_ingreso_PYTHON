import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luciano
apellido: Fattoni 

Enunciado:
Se desea desarrollar un programa que permita al usuario ingresar el nombre, año emitido (inferior al 2000, Superior a 2000 e inferior a 2015
y superior al 2015), si es online u offline y costo (500 a 10000) de 10 videojuegos.
Realizar las siguientes operaciones:

A - Encontrar el videojuego más caro y el más barato ingresado.
B - Calcular el promedio de los costos de los videojuegos, pero solo para aquellos que son online.
C - Encontrar los videojuegos con el costo máximo y mínimo de aquellos emitidos antes de 2015.
D - Calcular el porcentaje de videojuegos offline en relación al total de videojuegos ingresados.
E - Informar a que rango de año emitido pertenecen la mayor parte de los videojuegos vendidos.

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        costo_maximo = 499
        nombre_costo_min = ""
        costo_minimo = 10001
        nombre_costo_max = ""

        contador_online = 0
        costo_de_online = 0

        costo_maximo_2015 = 499
        costo_minimo_2015 = 10001

        contador_offline = 0

        contador_antes = 0
        contador_durante = 0
        contador_despues = 0

        for i in range(3):
            nombre = prompt(f"Juego {i + 1}", "Ingrese el nombre del juego:")

            while nombre == None or nombre == "":
                nombre = prompt("Error", "Ingrese un nombre valido:")

            año_emitido = prompt(f"Juego {i + 1}", "Ingrese el año en el que se emitio el juego:")

            while año_emitido:
                if not año_emitido.isdigit():
                    año_emitido = prompt("Error", "Ingrese el año en números:")
                else:
                    año_emitido = int(año_emitido)
                    break
            
            modo_de_juego = prompt(f"Juego {i + 1}", "Ingrese si el juego es online u offline:")

            while modo_de_juego:
                if modo_de_juego != "offline" and modo_de_juego != "online":
                    modo_de_juego = prompt("Error", "Ingrese si es online u offline:")
                else:
                    break
            
            costo = prompt(f"Juego {i + 1}", "Ingrese el costo del juego:")

            while costo:
                if not costo.isdigit() or (int(costo) < 500 or int(costo) > 10000):
                    costo = prompt("Error", "Ingrese un costo válido:")
                else:
                    costo = int(costo)
                    break

            print(f"\n Juego {i + 1}",
                f"\n Nombre = {nombre}",
                f"\n Año Emitido = {año_emitido}",
                f"\n Modo de Juego= {modo_de_juego}",
                f"\n Costo = {costo}")
            
            #A - Encontrar el videojuego más caro y el más barato ingresado.
            if int(costo) < int(costo_minimo):
                costo_minimo = costo
                nombre_costo_min = nombre
                
            if int(costo) > int(costo_maximo):
                costo_maximo = costo
                nombre_costo_max = nombre

            #B - Calcular el promedio de los costos de los videojuegos, pero solo para aquellos que son online.
                
            if modo_de_juego == "online":
                contador_online += 1
                costo_de_online += int(costo)
            
            promedio_online = costo_de_online / contador_online

            #C - Encontrar los videojuegos con el costo máximo y mínimo de aquellos emitidos antes de 2015.

            if año_emitido < 2015:
                if int(costo) < int(costo_minimo_2015):
                    costo_minimo_2015 = costo
                if int(costo) > int(costo_maximo_2015):
                    costo_maximo_2015 = costo
            
            #D - Calcular el porcentaje de videojuegos offline en relación al total de videojuegos ingresados.
            
            if modo_de_juego == "offline":
                contador_offline += 1
            
            porcentaje_offline = (contador_offline / 10) * 100

            #E - Informar a que rango de año emitido pertenecen la mayor parte de los videojuegos vendidos.

            if año_emitido < 2000:
                contador_antes += 1
            elif año_emitido >= 2000 and año_emitido < 2015:
                contador_durante += 1
            else:
                contador_despues += 1

            if contador_durante < contador_antes > contador_despues:
                año_con_mayor_juegos = "Antes del 2000"
            elif contador_durante > contador_antes:
                año_con_mayor_juegos = "Desde el 2000 hasta 2015"
            else:
                año_con_mayor_juegos = "Despues del 2015"


        alert("A", f"\n El juego con mayor costo es {nombre_costo_max} \n El juego con menor costo es {nombre_costo_min} ")
        alert("B", f"Promedio de los costos de los videojuegos online {promedio_online} pesos")
        alert("C", f"\n El juego con mayor costo es {costo_maximo_2015} \n El juego con menor costo es {costo_minimo_2015} antes del 2015")
        alert("D", f"Porcentaje de juegos offline {porcentaje_offline}%")
        alert("E", f"Rango de años de los juegos que se vendio más {año_con_mayor_juegos}")





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
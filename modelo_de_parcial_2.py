import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luciano
apellido: Fattoni 
---
Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

Nombre
Edad (debe ser mayor a 12)
Altura (debe ser mayor a cero)
Días que asiste a la semana (1, 3, 5)
Kilos que levanta en peso muerto (debe ser mayor a cero) 

No se sabe cuántos clientes serán consultados.

Se debe informar al usuario:

El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
El porcentaje de clientes que asiste solo 1 día a la semana.
Nombre y edad del cliente con más altura.
Determinar si los clientes eligen más ir 1, 3 o 5 días.
Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        contador_personas = 0

        contador_3_dias = 0
        kilos = 0

        contador_1_dias = 0

        altura_max = 1
        nombre_max = ""
        edad_max = 0

        contador_5_dias = 0

        edad_min = 130
        nombre_min = ""
        cant_de_kilos_min = 0

        while True:
            nombre = prompt(f"Persona {contador_personas + 1}", "Ingrese su nombre:")

            while nombre == "":
                nombre = prompt("Error", "Ingrese un nombre válido:")

            if nombre == None:
                break

            edad = prompt(f"Persona {contador_personas + 1}", "Ingrese su edad:")

            while edad:
                if int(edad) <= 12:
                    edad = prompt("Error", "Ingrese una edad mayor a 12:")
                else:
                    edad = int(edad)
                    break

            altura = prompt(f"Persona {contador_personas + 1}", "Ingrese su altura:")

            while altura:
                if float(altura) <= 0:
                    altura = prompt("Error", "Ingrese una altura válida:")
                else:
                    altura = float(altura)
                    break
            
            dias_que_asiste = prompt(f"Persona {contador_personas + 1}", "Ingrese los dias que asiste a la semana:")

            while dias_que_asiste:
                if int(dias_que_asiste) != 1 and int(dias_que_asiste) != 3 and int(dias_que_asiste) != 5:
                    dias_que_asiste = prompt("Error", "Ingrese los dias que asiste a la semana (1, 3 o 5):")
                else:
                    dias_que_asiste = int(dias_que_asiste)
                    break
            
            kilos_en_peso_muerto = prompt(f"Persona {contador_personas + 1}", "Ingrese los kilos que levanta en peso muerto:")

            while kilos_en_peso_muerto:
                if int(kilos_en_peso_muerto) <= 0:
                    kilos_en_peso_muerto = prompt("Error", "Ingrese un peso válido:")
                else:
                    kilos_en_peso_muerto = int(kilos_en_peso_muerto)
                    break

            print(f"\n Persona {contador_personas + 1}",
                f"\n Nombre: {nombre}",
                f"\n Edad: {edad}",
                f"\n Altura: {altura}",
                f"\n Días a la Semana: {dias_que_asiste}",
                f"\n Kg en Peso Muerto: {kilos_en_peso_muerto}")
            
            #El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
            if dias_que_asiste == 3:
                contador_3_dias += 1
                kilos += kilos_en_peso_muerto

            #El porcentaje de clientes que asiste solo 1 día a la semana.
            contador_personas += 1

            if dias_que_asiste == 1:
                contador_1_dias += 1

            #Nombre y edad del cliente con más altura.
            if altura > altura_max:
                altura_max = altura
                nombre_max = nombre
                edad_max = edad

            #Determinar si los clientes eligen más ir 1, 3 o 5 días.
            if dias_que_asiste == 5:
                contador_5_dias += 1
            
            if contador_3_dias < contador_1_dias > contador_5_dias:
                dias_mas_elegidos = "Los clientes eligen ir mas 1 día a la semana"
            elif contador_3_dias > contador_1_dias:
                dias_mas_elegidos = "Los clientes eligen ir mas 3 días a la semana"
            elif contador_3_dias < contador_5_dias > contador_1_dias:
                dias_mas_elegidos = "Los clientes eligen ir mas 5 días a la semana"
            else:
                dias_mas_elegidos = "No hay"

            #Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
            if edad < edad_min and dias_que_asiste == 5:
                nombre_min = nombre
                cant_de_kilos_min = kilos_en_peso_muerto

        #El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
        promedio_kilos = kilos / contador_3_dias

        #El porcentaje de clientes que asiste solo 1 día a la semana.
        porcentaje_1_dia = (contador_1_dias / contador_personas) * 100

        alert("Punto 1", f"El promedio de kilos que levantan las personas que asisten solo 3 días a la semana es de {promedio_kilos}kg")
        alert("Punto 2", f"El porcentaje de clientes que asiste solo 1 día a la semana es del {porcentaje_1_dia}%")
        alert("Punto 3", f"El cliente con más altura es {nombre_max} y su edad es de {edad_max} años")
        alert("Punto 4", f"{dias_mas_elegidos}")
        alert("Punto 5", f"La persona más joven que asiste 5 días a la semana es {nombre_min} y levanta {cant_de_kilos_min}kg")





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
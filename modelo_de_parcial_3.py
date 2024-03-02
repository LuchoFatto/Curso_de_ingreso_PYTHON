import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luciano
apellido: Fattoni 
---
Enunciado:
De 5 mascotas que ingresan a una veterinaria  se deben tomar y validar los siguientes datos.

Nombre
Tipo (gato ,perro o exotico)
Peso (entre 10 y 80)
Sexo(F o M)
Edad(mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        contador_f = 0
        contador_m = 0

        contador_gatos = 0
        contador_perros = 0
        contador_exoticos = 0

        peso_min = 81
        nombre_min = ""
        tipo_min = ""

        edad_min = 105
        nombre_min_perro = ""

        suma_de_pesos = 0

        for i in range(5):
            nombre = prompt(f"mascota {i +1}", "Ingrese el nombre de su mascota:")

            while True:
                if nombre.isdigit() or nombre == "" or nombre == None:
                    nombre = prompt("Error", "Ingrese un nombre válido:")
                else:
                    break

            tipo = prompt(f"Mascota {i +1}", "Ingrese que tipo de mascota tiene:")

            while True:
                if tipo == "" or tipo != "gato" and tipo != "perro" and tipo != "exotico":
                    tipo = prompt("Error", "Ingrese un tipo de mascota válido (gato, perro o exotico):")
                else:
                    break

            peso = prompt(f"Mascota {i +1}", "Ingrese cuanto pesa su mascota:")

            while True:
                if peso == "" or int(peso) < 10 or int(peso) > 80:
                    peso = prompt("Error", "Ingrese un peso válido (entre 10 a 80):")
                else:
                    peso = int(peso)
                    break

            sexo = prompt(f"Mascota {i +1}", "Ingrese el sexo de su mascota:")

            while True:
                if sexo == "" or sexo != "f" and sexo != "m":
                    sexo = prompt("Error", "Ingrese un sexo válido (m o f):")
                else:
                    break
            
            edad = prompt(f"Mascota {i +1}", "Ingrese la edad de su mascota:")

            while True:
                if edad == "" or int(edad) <= 0:
                    edad = prompt("Error", "Ingrese una edad válida:")
                else:
                    edad = int(edad)
                    break

            print(f"\n Mascota {i + 1}"
                f"\n Nombre: {nombre}"
                f"\n Tipo: {tipo}"
                f"\n Peso: {peso}"
                f"\n Sexo: {sexo}"
                f"\n Edad: {edad}")

            #Informe A- Cuál fue el sexo menos ingresado (F o M)
            if sexo == "f":
                contador_f += 1
            else:
                contador_m += 1

            #Informe B- El porcentaje de mascotas que hay por tipo (gato ,perro o exotico)
            if tipo == "gato":
                contador_gatos += 1
            elif tipo == "perro":
                contador_perros += 1
            else:
                contador_exoticos += 1

            #Informe C- El nombre y tipo de la mascota menos pesada
            if int(peso) < peso_min:
                peso_min = peso
                nombre_min = nombre
                tipo_min = tipo

            #Informe D- El nombre del perro más joven
            if tipo == "perro" and int(edad) < edad_min:
                edad_min = edad
                nombre_min_perro = nombre
            
            #Informe E- El promedio de peso de todas las mascotas
            suma_de_pesos += peso
            promedio_de_pesos = suma_de_pesos / 5

        #A
        if contador_f > contador_m:
            sexo_menos_ingresado = "Masculino"
        elif contador_f < contador_m:
            sexo_menos_ingresado = "Femenino"
        else:
            sexo_menos_ingresado = "No hay"

        #B
        porcentaje_gatos = (contador_gatos / 5) * 100
        porcentaje_perros = (contador_perros / 5) * 100
        porcentaje_exoticos = (contador_exoticos / 5) * 100

        print(f"\n Sexo menos ingresado: {sexo_menos_ingresado}",
            f"\n Porcentaje de gatos: {porcentaje_gatos}",
            f"\n Porcentaje de perros: {porcentaje_perros}",
            f"\n Porcentaje de exoticos: {porcentaje_exoticos}",
            f"\n La mascota menos pesada es {nombre_min} y es un {tipo_min}",
            f"\n El perro más jóven: {nombre_min_perro}"
            f"\n Promedio de pesos de todas las mascotas: {promedio_de_pesos}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
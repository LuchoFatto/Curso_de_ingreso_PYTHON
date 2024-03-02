import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luciano
apellido: Fattoni
dni: 45.421.405 
---
De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos:

Marca (no validar)
Categoría (peligroso, comestible, indumentaria)
Peso (entre 100 y 800)
Tipo de material (aluminio, hierro , madera)
Costo en $ (mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:

Informe A- Cuál fue tipo de material menos usado ( aluminio, hierro , madera)
Informe B- El porcentaje de contenedores por Categoría (peligroso, comestible, indumentaria)
Informe C- La marca y tipo del contenedor más costoso
Informe D- La marca del contenedor de aluminio con mayor costo
Informe E- El promedio de costo de todos los contenedores
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        contador_aluminio = 0
        contador_hierro = 0
        contador_madera = 0
        
        contador_peligroso = 0
        contador_comestible = 0
        contador_indumentaria = 0

        costo_max = 0
        tipo_costoso = ""
        marca_costosa = ""

        costo_max_alum = 0
        marca_cara_alum = ""

        suma_de_costos = 0

        for i in range(20):
            marca = prompt(f"Contenedor {i + 1}", "Ingrese la marca del contenedor:")

            categoria = prompt(f"Contenedor {i + 1}", "Ingrese la categoría del contenedor:")

            while True:
                if categoria == "" or categoria != "peligroso" and categoria != "comestible" and categoria != "indumentaria":
                    categoria = prompt("Error", "Ingrese una categoría válida (peligroso, comestible o indumentaria):")
                else:
                    break

            peso = prompt(f"Contenedor {i + 1}", "Ingrese el peso del contenedor:")

            while True:
                if peso == "" or int(peso) < 100 or int(peso) > 800:
                    peso = prompt("Error", "Ingrese un peso válido (100 a 800):")
                else:
                    peso = int(peso)
                    break

            tipo_de_material = prompt(f"Contenedor {i + 1}", "Ingrese el tipo de material del contenedor:")

            while True:
                if tipo_de_material == "" or tipo_de_material != "aluminio" and tipo_de_material != "hierro" and tipo_de_material != "madera":
                    tipo_de_material = prompt("Error", "Ingrese un material válido (aluminio, hierro o madera):")
                else:
                    break
            
            costo = prompt(f"Contenedor {i + 1}", "Ingrese el costo en pesos:")

            while True:
                if costo == "" or int(costo) <= 0:
                    costo = prompt(f"Contenedor {i + 1}", "Ingrese un costo válido (mayor a 0):")
                else:
                    costo = int(costo)
                    break

            print(f"\n Contenedor {i + 1}",
                f"\n Marca: {marca}",
                f"\n Categoría: {categoria}",
                f"\n Peso: {peso}",
                f"\n Tipo de Material: {tipo_de_material}",
                f"\n Costo: {costo}")
            
            #Informe A- Cuál fue tipo de material menos usado (aluminio, hierro , madera)
            if tipo_de_material == "aluminio":
                contador_aluminio += 1
            elif tipo_de_material == "hierro":
                contador_hierro += 1
            else:
                contador_madera += 1

            #Informe B- El porcentaje de contenedores por Categoría (peligroso, comestible, indumentaria)
            if categoria == "peligroso":
                contador_peligroso += 1
            elif categoria == "comestible":
                contador_comestible += 1
            else:
                contador_indumentaria += 1

            #Informe C- La marca y tipo del contenedor más costoso
            if int(costo) > costo_max:
                costo_max = costo
                tipo_costoso = tipo_de_material
                marca_costosa = marca

            #Informe D- La marca del contenedor de aluminio con mayor costo
            if tipo_de_material == "aluminio" and int(costo) > costo_max_alum:
                costo_max_alum = costo
                marca_cara_alum = marca

            #Informe E- El promedio de costo de todos los contenedores
            suma_de_costos += costo
            promedio_de_costos = suma_de_costos / 20

        #B
        porcentaje_peligroso = (contador_peligroso / 20) * 100
        porcentaje_comestible = (contador_comestible / 20) * 100
        porcentaje_indumentaria = (contador_indumentaria / 20) * 100

        #A
        if contador_hierro > contador_aluminio < contador_madera:
            material_menos_usado = "Aluminio"
        elif contador_aluminio > contador_hierro < contador_madera:
            material_menos_usado = "Hierro"
        elif contador_aluminio > contador_madera < contador_hierro:
            material_menos_usado = "Madera"
        else:
            material_menos_usado = "No hay"

        print(f"\n El material menos usado es {material_menos_usado}",
            f"\n El porcentaje de peligroso es: {porcentaje_peligroso}, el de comestibles es: {porcentaje_comestible} y el de indumentaria es: {porcentaje_indumentaria}",
            f"\n El contenedor mas costoso es de la marca {marca_costosa} y el tipo de material es {tipo_costoso}",
            f"\n La marca del contenedor más caro de aluminio es {marca_cara_alum}",
            f"\n El promedio de costo de todos los contenedores {promedio_de_costos}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

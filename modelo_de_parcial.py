import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luciano
apellido: Fattoni 
---
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
edad(mayor a 0)
pedir datos por prompt y mostrar por print

Punto A - informar cual fue el sexo mas ingresado
Punto B - el porcentaje de personas con fiebre y el porcentaje sin fiebre

Punto C - por el número de DNI del alumno

DNI terminados en  4 o 5

1)informar la cantidad de personas de sexo  nb
2) la edad promedio de  personas de sexo  femenino
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)

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
        contador_nb = 0

        contador_fiebre = 0
        contador_sin_fiebre = 0

        edad_fem = 0

        temperatura_min = 43
        nombre_m_min = ""

        for i in range(5):
            nombre = prompt(f"Persona {i + 1}", "Ingrese su nombre:")

            temperatura = prompt(f"persona {i + 1}", "Ingrese su temperatura:")

            while temperatura:
                if not temperatura.isdigit() or (int(temperatura) <= 35 or int(temperatura) >= 42):
                    temperatura = prompt("Error", "Ingrese una temperatura válida:")
                else:
                    temperatura = int(temperatura)
                    break

            sexo = prompt(f"persona {i + 1}", "Ingrese su sexo:")

            while sexo:
                if sexo != "m" and sexo != "f" and sexo != "nb":
                    sexo = prompt("Error", "Ingrese un sexo válido (m, f, nb):")
                else:
                    break

            edad = prompt(f"persona {i + 1}", "Ingrese su edad:")

            while edad:
                if int(edad) <= 0:
                    edad = prompt("Error", "Ingrese una edad válida (mayor a cero):")
                else:
                    edad = int(edad)
                    break
            
            print(f"\n Persona {i + 1}",
                f"\n Nombre = {nombre}",
                f"\n Temperatura = {temperatura} °C",
                f"\n Género = {sexo}",
                f"\n Edad = {edad}")

            #Punto A - informar cual fue el sexo mas ingresado

            if sexo == "m":
                contador_m += 1
            elif sexo == "f":
                contador_f += 1
            else:
                contador_nb += 1

            #Punto B - el porcentaje de personas con fiebre y el porcentaje sin fiebre
                    
            if temperatura >= 37:
                contador_fiebre += 1
            else:
                contador_sin_fiebre += 1

            #Punto C, 2) la edad promedio de personas de sexo femenino
            
            if sexo == "f":
                edad_fem += int(edad)
            
            #Punto C, 3) el nombre de la persona de sexo masculino con la temperatura mas baja(si la hay)
                
            if sexo == "m" and int(temperatura) < int(temperatura_min):
                temperatura_min = temperatura
                nombre_m_min = nombre
                

        #Punto A
        if contador_f < contador_m > contador_nb:
            sexo_mas_ingresado = "Masculino"
        elif contador_f > contador_m:
            sexo_mas_ingresado = "Femenino"
        elif contador_f < contador_nb > contador_m:
            sexo_mas_ingresado = "No Binario"
        else:
            sexo_mas_ingresado = "No hay"
    
        #Punto B
        porcentaje_fiebre = (contador_fiebre / 5) * 100
        porcentaje_sin_fiebre = (contador_sin_fiebre / 5) * 100

        #Punto C, 2)
        edad_promedio_fem = edad_fem / contador_f 

        alert("Punto A", f"El sexo más ingresado es: {sexo_mas_ingresado}")
        alert("Punto B", f"\n Porcentaje de personas con fiebre {porcentaje_fiebre} %, \n Porcentaje de personas sin fiebre {porcentaje_sin_fiebre} %")
        alert("Punto C, 1", f"Cantidad de personas de sexo No BInario: {contador_nb}")
        alert("Punto C, 2", f"Edad promedio del sexo femenino: {edad_promedio_fem}")
        alert("Punto C, 3", f"Persona masculina con menor temperatura: {nombre_m_min}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
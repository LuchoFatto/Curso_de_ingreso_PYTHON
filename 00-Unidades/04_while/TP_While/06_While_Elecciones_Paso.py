import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luciano
apellido: Fattoni
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        edad = None
        cant_votos = None
        cant_votos_max = None
        cant_votos_min = None
        contador = 0
        suma = 0
        suma_votos = 0

        while True:
            nombre = prompt("Ingreso", "Ingrese su nombre de candidato")
            edad = prompt("Ingreso", "Ingrese su edad")
            cant_votos = prompt("Ingreso", "Ingrese cantidad de votos")
            
            if nombre is None:
                break

            edad = int(edad)
            cant_votos = int(cant_votos)

            while edad < 25:
                edad = int(prompt("No válido", "Ingrese una edad valida"))
            
            #a
            if cant_votos_max == None or cant_votos_max < cant_votos:
                cant_votos_max = cant_votos
                nombre_max = nombre

            cant_y_votos_max =  f"\n candidato con más votos: {nombre_max} {cant_votos_max}"

            #b
            if cant_votos_min == None or cant_votos_min > cant_votos:
                cant_votos_min = cant_votos
                nombre_min = nombre
            
            cant_y_votos_min =  f"\n candidato con menos votos: {nombre_min} {cant_votos_min}"

            #c
            contador += 1
            suma += edad
            promedio_edad = suma / contador

            mensaje = f"\n promedio edades {promedio_edad}"

            #d
            suma_votos += cant_votos

            mensaje_2 = f"\n suma total de votos {suma_votos}"
            
        print(cant_y_votos_max, cant_y_votos_min, mensaje, mensaje_2)
        #f"\n {mensaje}"

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

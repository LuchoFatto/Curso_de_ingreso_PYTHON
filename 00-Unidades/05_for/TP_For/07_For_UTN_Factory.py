import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luciano
apellido: Fattoni
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador_punto_a = 0

        edad_minima = 100
        minimo = ""

        contador_edad_nb = 0
        contador_edad_m = 0
        contador_edad_f = 0
        contador_nb = 0
        contador_f = 0
        contador_m = 0

        contador_js = 0
        contador_phyton = 0
        contador_asp_net = 0
        tecno_con_mas_paticipantes = ""
        
        for i in range(10):
            nombre = prompt(f"Ingreso {i + 1}", "Ingrese su nombre:")
            edad = prompt(f"Ingreso {i + 1}", "Ingrese su edad:")

            while edad:
                if not edad.isdigit() or int(edad) <= 17:
                    edad = prompt("Error", "Ingrese una edad valida (18 o mas)")
                else:
                    edad = int(edad)
                    break
            
            genero = prompt(f"Ingreso {i + 1}", "Ingrese su género")

            while genero:
                if genero != "f" and genero != "m" and genero != "nb":
                    genero = prompt("Error", "Ingrese un genero válido (f, m , nb)")
                else:
                    break
                    
            tecnologia = prompt(f"Ingreso {i + 1}", "Ingrese su tecnología")

            while tecnologia:
                if tecnologia != "phyton" and tecnologia != "js" and tecnologia != "asp.net":
                    tecnologia = prompt("Error", "Ingrese una tecnología válido (PYTHON, JS , ASP.NET)")
                else:
                    break
            
            puesto = prompt(f"Ingreso {i + 1}", "Ingrese su puesto")

            while puesto:
                if puesto != "jr" and puesto != "ssr" and puesto != "sr":
                    puesto = prompt("Error", "Ingrese un puesto valido (jr, ssr , sr)")
                else:
                    break

            print(f"\n Ingreso {i + 1}",
                  f"\n Nombre = {nombre}",
                  f"\n Edad = {edad}",
                  f"\n Género = {genero}",
                  f"\n Tecnología = {tecnologia}",
                  f"\n Puesto = {puesto}")
            
            #a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
            #cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
            if genero == "nb" and (tecnologia == "asp.net" or tecnologia == "js") and (int(edad) >= 25 and int(edad) <= 40) and puesto == "Ssr":
                contador_punto_a += 1
            
            #b. Nombre del postulante Jr con menor edad.
            if puesto == "jr" and int(edad) < int(edad_minima):
                edad_minima = edad
                minimo = nombre
            
            #c. Promedio de edades por género.
            if genero == "nb":
                contador_edad_nb += int(edad)
                contador_nb += 1
            else:
                if genero == "f":
                    contador_edad_f += int(edad) 
                    contador_f += 1
                else:
                    contador_edad_m += int(edad)
                    contador_m += 1
        
            #d. Tecnologia con mas postulantes (solo hay una).
            if tecnologia == "js":
                contador_js += 1
            if tecnologia == "asp.net":
                contador_asp_net += 1
            if tecnologia == "phyton":
                contador_phyton += 1
            
            #e. Porcentaje de postulantes de cada genero.
                porcentaje_fem = (contador_f / 10) * 100
                porcentaje_mas = (contador_m / 10) * 100
                porcentaje_nb = (contador_nb / 10) * 100
            

        if contador_m == 0:
            promedio_m = 0
        else:
            promedio_m = contador_edad_m / contador_m
        if contador_f == 0:
            promedio_f = 0
        else:
            promedio_f = contador_edad_f / contador_f
        if contador_nb == 0:
            promedio_nb = 0
        else:
            promedio_nb = contador_edad_nb / contador_nb

        if contador_asp_net > contador_js and contador_asp_net > contador_phyton:
            tecno_con_mas_paticipantes = "ASP.NET"
        if contador_js > contador_asp_net and contador_js > contador_phyton:
            tecno_con_mas_paticipantes = "JS"
        if contador_phyton > contador_asp_net and contador_phyton > contador_js:
            tecno_con_mas_paticipantes = "PHYTON"

        alert("Cantidad", f"Cantdiad de postulantes {contador_punto_a}")
        alert("Edad mínima", f"Postulante con edad mínima {minimo}")
        alert("Promedios", f"Promedios de edad de género nb: {promedio_nb}, f: {promedio_f}, m: {promedio_m}")
        alert("Tecnología", f"Tecnologia con mas postulantes {tecno_con_mas_paticipantes}")
        alert("Porcentajes", f"Porcentaje masculinos: {porcentaje_mas}%, Porcentaje femeninos {porcentaje_fem}%, Porcentaje no binarios {porcentaje_nb}%")




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

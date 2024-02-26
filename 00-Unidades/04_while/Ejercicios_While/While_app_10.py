import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luciano
apellido: Fattoni
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numero = 0
        suma_n = 0
        suma_p = 0
        contador_negativos = 0
        contador_positivos = 0
        cantidad_0 = 0

        while True:
            numero = prompt("Ingresar", "Ingrese un número")
            

            if(numero is None):
                break

            numero = int(numero)
            
            if(numero < 0):
                suma_n += numero
                contador_negativos += 1
            else:
                if(numero > 0):
                    suma_p += numero
                    contador_positivos += 1
                else:
                    cantidad_0 += 1
            
            diferencia = contador_positivos - contador_negativos
            
            mensaje = ("La suma de los numeros negativos es {0}, la de los positivos es {1}, la cantidad de numeros positivos es de {2},"
                        "la cantidad de negativos es de {3} y su diferencia es de {4},"
                        "cantidad de ceros {5}".format(suma_n, suma_p, contador_positivos, contador_negativos, diferencia, cantidad_0))

        alert("Datos", mensaje)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

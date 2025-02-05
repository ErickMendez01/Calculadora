import tkinter as tk
from tkinter import END, messagebox

class Calculadora:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora")
        self.root.geometry("400x500")

        self.txtDisplay = tk.Entry(self.root, font=("Arial", 18), width=18, bd=5, justify="right")
        self.txtDisplay.grid(row=0, column=0, columnspan=4, pady=10)
        self.txtDisplay.bind("<KeyRelease>", self.actualizar_binario)
        
        self.lblBinario = tk.Label(self.root, text="Bin 0", font=("Arial", 12), anchor="e")
        self.lblBinario.grid(row=1, column=0, columnspan=4, pady=5, sticky="w")

        self.aux = 0
        self.signo = ""

        botones = [
            ('A',0,2),('log', 1, 2), ('x^x', 2, 2), ('CE', 3, 2), ('<-', 4, 2),
            ('B',0,3),('^', 1, 3),   ('!n', 2, 3),  ('%', 3, 3),  ('/', 4, 3),
            ('C',0,4),('7', 1, 4),   ('8', 2, 4),   ('9', 3, 4),  ('*', 4, 4),
            ('D',0,5),('4', 1, 5),   ('5', 2, 5),   ('6', 3, 5),  ('-', 4, 5),
            ('E',0,6),('1', 1, 6),   ('2', 2, 6),   ('3', 3, 6),  ('+', 4, 6),
            ('F',0,7),('AB', 1, 7),  ('0', 2, 7),   ('.', 3, 7),  ('=', 4, 7)
        ]

        for (text, col, row) in botones:
            tk.Button(self.root, text=text, font=("Arial", 10), width=5, height=2, 
                      command=lambda t=text: self.boton_click(t)).grid(row=row, column=col, padx=5, pady=5)

        self.root.mainloop()

    def boton_click(self, valor):
        if valor in "0123456789.":
            self.txtDisplay.insert(END, valor)
            self.actualizar_binario()
        elif valor in "+-*/":
            self.operador(valor)
        elif valor == "=":
            self.operacion()
        elif valor == "!n":
            self.mostrar_factorial()

    def decimal_a_binario(self, decimal):
        if decimal <= 0:
            return "0"
        binario = ""
        while decimal > 0:
            residuo = int(decimal % 2)
            decimal = int(decimal / 2)
            binario = str(residuo) + binario
        return binario

    def actualizar_binario(self, event=None):
        try:
            valor = int(float(self.txtDisplay.get()))
            self.lblBinario.config(text=f"Bin {self.decimal_a_binario(valor)}")
        except ValueError:
            self.lblBinario.config(text="Bin 0")

    def operador(self, op):
        self.signo = op
        try:
            self.aux = float(self.txtDisplay.get())
            self.txtDisplay.delete(0, END)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")

    def suma(self, actual):
        return self.aux + actual
    
    def resta(self, actual):
        return self.aux - actual
    
    def multiplicacion(self, actual):
        return self.aux * actual 
       
    def division(self, actual): 
        return self.aux / actual
    
    def factorial(self, valor):
        if valor == 0 or valor == 1:
            return 1
        resultado = 1
        for i in range(2, valor + 1):
            resultado *= i
        return resultado
        
    def mostrar_factorial(self):
        actual = int(float(self.txtDisplay.get()))  
        resultado = self.factorial(actual)
        self.txtDisplay.delete(0, END)
        self.txtDisplay.insert(0, str(resultado))
        self.actualizar_binario()
    
    def operacion(self):
        try:
            actual = float(self.txtDisplay.get())
        
            if self.signo == "+":
                resultado = self.suma(actual)
            elif self.signo == "-":
                 resultado = self.resta(actual)
            elif self.signo == "*":
                 resultado = self.multiplicacion(actual)
            elif self.signo == "/":
                try:
                     resultado = self.division(actual)
                except ZeroDivisionError:
                    messagebox.showerror("Error de sistema","División entre cero")
                    return
            self.txtDisplay.delete(0, END)
            self.txtDisplay.insert(0, str(resultado))
            self.actualizar_binario()
        except ValueError:
            messagebox.showerror("Error de sistema", "Operación no válida")

if __name__=="__main__":
    Calculadora()

import tkinter as tk
from tkinter import END, messagebox

class Calculadora:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora")
        self.root.geometry("400x500")
        self.txtDisplay = tk.Entry(self.root, font=("Arial", 18), width=18, bd=5, justify="right")
        self.txtDisplay.grid(row=0, column=0, columnspan=4, pady=10)
        self.aux = 0
        self.signo = ""

        botones = [
            ('A',0,1),('log', 1, 1), ('x^x', 2, 1), ('CE', 3, 1), ('<-', 4, 1),
            ('B',0,2),('^', 1, 2),   ('!n', 2, 2),  ('%', 3, 2),  ('/', 4, 2),
            ('C',0,3),('7', 1, 3),   ('8', 2, 3),   ('9', 3, 3),  ('*', 4, 3),
            ('D',0,4),('4', 1, 4),   ('5', 2, 4),   ('6', 3, 4),  ('-', 4, 4),
            ('E',0,5),('1', 1, 5),   ('2', 2, 5),   ('3', 3, 5),  ('+', 4, 5),
            ('F',0,6),('AB', 1, 6),  ('0', 2, 6),   ('.', 3, 6),  ('=', 4, 6)
        ]

        for (text, col, row) in botones:
            tk.Button(self.root, text=text, font=("Arial", 10), width=5, height=2, 
                      command=lambda t=text: self.boton_click(t)).grid(row=row, column=col, padx=5, pady=5)

        self.root.mainloop()

    def boton_click(self, valor):
        if valor in "0123456789.":
            self.txtDisplay.insert(END, valor)
        elif valor in "+-*/":
            self.operador(valor)
        elif valor == "=":
            self.operacion()
        elif valor == "!n":
            self.mostrar_factorial()

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
        except ValueError:
            messagebox.showerror("Error de sistema", "Operación no válida")

if __name__=="__main__":
    Calculadora()
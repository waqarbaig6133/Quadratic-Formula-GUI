#Quadratic formula solver
from tkinter import *
import math


class Solving:
    """Solving"""

    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0

    def quadratic1(self):
        D = (self.B) ** 2 - (4 * self.A * self.C)
        if D < 0:
            return "no real solutions"
        else:
            sqrt_D = math.sqrt(D)
            return ((-self.B + sqrt_D) / (2 * self.A))

    def quadratic2(self):
        D = (self.B) ** 2 - (4 * self.A * self.C)
        if D < 0:
            return "no real solutions"
        else:
            sqrt_D = math.sqrt(D)
            return ((-self.B - sqrt_D) / (2 * self.A))

        
        
    

def calculate():
    myQuad = Solving()
    myQuad.A = float(ent_A.get())
    myQuad.B = float(ent_B.get())
    myQuad.C = float(ent_C.get())
    txtCal.configure(text="Calculatation: \t"+str(myQuad.quadratic1()))
    txtCal2.configure(text="Calculatation: \t"+str(myQuad.quadratic2()))        
fen = Tk()
fen.title("Quadratic formula calculator")

#Value A
txtA = Label(fen, text = "A: ")
txtA.grid(row = 0, column = 0, sticky = E)
ent_A = Entry(fen)
ent_A.grid(row = 0, column = 1)

#Value B
txtB = Label(fen, text = "B: ")
txtB.grid(row = 1, column = 0, sticky = E)
ent_B = Entry(fen)
ent_B.grid(row = 1, column = 1)

#Value C
txtC = Label(fen, text = "C: ")
txtC.grid(row = 2, column = 0, sticky = E)
ent_C = Entry(fen)
ent_C.grid(row = 2, column = 1)

button = Button(fen, text = "Calculate", command = calculate)
button.grid(row = 3, column = 0, columnspan = 2)

txtCal = Label(fen, text = "Zero 1: ")
txtCal.grid(row = 4, column = 0, columnspan = 2, sticky = W)
txtCal2 = Label(fen, text = "Zero 2: ")
txtCal2.grid(row = 5, column = 0, columnspan = 2, sticky = W)

fen.mainloop()

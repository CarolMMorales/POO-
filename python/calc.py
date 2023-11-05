from tkinter import *
ventana = Tk()
myFrame = Frame(ventana, height= 500, width=800)
myFrame.pack()

num1Label=Label(myFrame, text="num1").place(x=200, y=100)
num1Input=Entry(myFrame)
num1Input.place(x=270, y=100)

num2Label=Label(myFrame, text="num2").place(x=200, y=150)
num2Input=Entry(myFrame)
num2Input.place(x=270, y=150)

resultLabel=Label(myFrame, text="resultado").place(x=200,y=200)


opcion=IntVar()

operRadio1=Radiobutton(myFrame, text="suma", variable=opcion, value=1).place(x=150,y=250)
operRadio2=Radiobutton(myFrame, text="resta", variable=opcion, value=2).place(x=220,y=250)
operRadio3=Radiobutton(myFrame, text="multiplicacion", variable=opcion, value=3).place(x=290,y=250)
operRadio4=Radiobutton(myFrame, text="division", variable=opcion, value=4).place(x=400,y=250)



class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.sum = 0
        self.rest = 0
        self.mult = 0
        self.div = 0
        
    def Setsuma(self):
        self.sum = self.num1+self.num2
        #print("Suma: " , (self.num1+self.num2))
    def Getsuma(self):
        return self.sum
        
    def Setresta(self):
        self.rest = self.num1-self.num2
        
    def Getresta(self):
        return self.rest
        
    def Setdividir(self):
        self.div = self.num1/self.num2
        
    def Getdividir(self):
        return self.div

    def Setmultiplicar(self):
        self.mult= self.num1*self.num2
        
    def Getmultiplicar(self):
            return self.mult  
 
      
def calcular():
    resultLabel = ""
    num1 = float(num1Input.get())
    num2 = float(num2Input.get())
    if opcion.get() == 1:
        resultLabel = num1 + num2
    elif opcion.get() == 2:
        resultLabel = num1 - num2    
    elif opcion.get() == 3:
        resultLabel = num1 * num2 
    elif opcion.get() == 3:
        resultLabel = num1 / num2
        
    resultLabel=Label(myFrame, text=resultLabel).place(x=270,y=200) 
        
botonCalcular=Button(myFrame, text="calcular", command= calcular)
botonCalcular.place(x=280,y=300)        

num1 = float(input("ingrese numero 1"))
num2 = float(input("ingrese numero 2"))
Calc = Calc(num1, num2)


Calc.Setsuma()
print("la suma es: ", Calc.Getsuma())

Calc.Setresta()
print("la resta es: ", Calc.Getresta())

Calc.Setmultiplicar()
print("la multiplicación es: ", Calc.Getmultiplicar())

Calc.Setdividir()
print("la división es: ", Calc.Getdividir())


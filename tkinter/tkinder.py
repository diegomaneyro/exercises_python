import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

def saludar(nombre):
    print('hola '+ nombre)

boton1 = tkinter.Button(ventana, text = "boton1", width = 10, height = 5,  command = lambda: print('hola'))

boton1.grid(row=0, column=0)

if __name__ == '__main__':
    ventana.mainloop()


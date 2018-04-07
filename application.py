from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 5
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 5
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 5
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 5
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 5
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 5
        self.sextoContainer.pack()

        self.setimoContainer = Frame(master)
        self.setimoContainer["padx"] = 5
        self.setimoContainer.pack()

        self.display = Entry(self.segundoContainer, text="", font=self.fontePadrao, bg="gray85")
        self.display["width"] = 14
        self.display["font"] = ("Calibri", "40")
        self.display.pack()

        self.c = Button(self.terceiroContainer, bg="black", fg="white" )
        self.c["text"] = "C"
        self.c["font"] = ("Calibri", "25")
        self.c["width"] = 4
        self.c["height"] = 2
        self.c.pack(side=LEFT)

        self.porcentagem = Button(self.terceiroContainer, bg="black", fg="white")
        self.porcentagem["text"] = "%"
        self.porcentagem["font"] = ("Calibri", "25")
        self.porcentagem["width"] = 4
        self.porcentagem["height"] = 2
        self.porcentagem.pack(side=LEFT)

        self.raizquadrada = Button(self.terceiroContainer, bg="black", fg="white")
        self.raizquadrada["text"] = "√"
        self.raizquadrada["font"] = ("Calibri", "25")
        self.raizquadrada["width"] = 4
        self.raizquadrada["height"] = 2
        self.raizquadrada.pack(side=LEFT)

        self.delete = Button(self.terceiroContainer, bg="black", fg="white")
        self.delete["text"] = "DEL"
        self.delete["font"] = ("Calibri", "25")
        self.delete["width"] = 4
        self.delete["height"] = 2
        self.delete.pack(side=LEFT)

        self.sete = Button(self.quartoContainer, bg="black", fg="white")
        self.sete["text"] = "7"
        self.sete["font"] = ("Calibri", "25")
        self.sete["width"] = 4
        self.sete["height"] = 2
        self.sete.pack(side=LEFT)

        self.oito = Button(self.quartoContainer, bg="black", fg="white")
        self.oito["text"] = "8"
        self.oito["font"] = ("Calibri", "25")
        self.oito["width"] = 4
        self.oito["height"] = 2
        self.oito.pack(side=LEFT)

        self.nove = Button(self.quartoContainer, bg="black", fg="white")
        self.nove["text"] = "9"
        self.nove["font"] = ("Calibri", "25")
        self.nove["width"] = 4
        self.nove["height"] = 2
        self.nove.pack(side=LEFT, )

        self.divisao = Button(self.quartoContainer, bg="gray25", fg="orange")
        self.divisao["text"] = "÷"
        self.divisao["font"] = ("Calibri", "25")
        self.divisao["width"] = 4
        self.divisao["height"] = 2
        self.divisao.pack(side=LEFT)

        self.quatro = Button(self.quintoContainer, bg="black", fg="white")
        self.quatro["text"] = "4"
        self.quatro["font"] = ("Calibri", "25")
        self.quatro["width"] = 4
        self.quatro["height"] = 2
        self.quatro.pack(side=LEFT)

        self.cinco= Button(self.quintoContainer, bg="black", fg="white")
        self.cinco["text"] = "5"
        self.cinco["font"] = ("Calibri", "25")
        self.cinco["width"] = 4
        self.cinco["height"] = 2
        self.cinco.pack(side=LEFT)

        self.seis = Button(self.quintoContainer, bg="black", fg="white")
        self.seis["text"] = "6"
        self.seis["font"] = ("Calibri", "25")
        self.seis["width"] = 4
        self.seis["height"] = 2
        self.seis.pack(side=LEFT)

        self.multiplicacao = Button(self.quintoContainer, bg="gray25", fg="orange")
        self.multiplicacao["text"] = "X"
        self.multiplicacao["font"] = ("Calibri", "25")
        self.multiplicacao["width"] = 4
        self.multiplicacao["height"] = 2
        self.multiplicacao.pack(side=LEFT)

        self.um = Button(self.sextoContainer, bg="black", fg="white")
        self.um["text"] = "1"
        self.um["font"] = ("Calibri", "25")
        self.um["width"] = 4
        self.um["height"] = 2
        self.um.pack(side=LEFT)

        self.dois = Button(self.sextoContainer, bg="black", fg="white")
        self.dois["text"] = "2"
        self.dois["font"] = ("Calibri", "25")
        self.dois["width"] = 4
        self.dois["height"] = 2
        self.dois.pack(side=LEFT)

        self.tres = Button(self.sextoContainer, bg="black", fg="white")
        self.tres["text"] = "3"
        self.tres["font"] = ("Calibri", "25")
        self.tres["width"] = 4
        self.tres["height"] = 2
        self.tres.pack(side=LEFT)

        self.subtracao = Button(self.sextoContainer, bg="gray25", fg="orange")
        self.subtracao["text"] = "-"
        self.subtracao["font"] = ("Calibri", "25")
        self.subtracao["width"] = 4
        self.subtracao["height"] = 2
        self.subtracao.pack(side=LEFT)

        self.zero = Button(self.setimoContainer, bg="black", fg="white")
        self.zero["text"] = "0"
        self.zero["font"] = ("Calibri", "25")
        self.zero["width"] = 4
        self.zero["height"] = 2
        self.zero.pack(side=LEFT)

        self.ponto = Button(self.setimoContainer, bg="black", fg="white")
        self.ponto["text"] = "."
        self.ponto["font"] = ("Calibri", "25")
        self.ponto["width"] = 4
        self.ponto["height"] = 2
        self.ponto.pack(side=LEFT)

        self.igual = Button(self.setimoContainer, bg="orange", fg="white")
        self.igual["text"] = "="
        self.igual["font"] = ("Calibri", "25")
        self.igual["width"] = 4
        self.igual["height"] = 2
        self.igual.pack(side=LEFT)

        self.adicao = Button(self.setimoContainer, bg="gray25", fg="orange")
        self.adicao["text"] = "+"
        self.adicao["font"] = ("Calibri", "25")
        self.adicao["width"] = 4
        self.adicao["height"] = 2
        self.adicao.pack(side=LEFT)

root = Tk()
root.title('Calculadora')
root.configure(bg='black')
Application(root)
root.mainloop()
#Importando a biblioteca Tkinter
from tkinter import *
from tkinter import ttk

#Cores
cor1 = "#121f1e" #preto
cor2 = "#2e2e2e" #cinza escuro
cor3 = "#feffff" #branco
cor4 = "#2a2b39" #azul
cor5 = "#ffab40" #laranja

#Criação da janela
janela = Tk()
janela.title("Calculadora") #Define o titulo da minha janela
janela.geometry("235x310") #Define o tamanho, sendo o primeiro valor a largura, e o segundo a altura
janela.config(bg=cor1)

#Frame para criação do display
frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)

#Frame para criação do teclado da calculadora
frame_botoes = Frame(janela, width=235, height=268)
frame_botoes.grid(row=1, column=0)

#Lógica

total_valores = '' #variável para armazenar o que se digita
valor_texto = StringVar() #Variável para imprimir na tela a string 

def entrada_valor(event):

    global total_valores #definir como global para que possa ser alterada em todas as funções
    
    total_valores = total_valores + str(event)

    #Passando o valor digitado para a tela
    valor_texto.set(total_valores)

#Função para calcular
def calcular():

    global total_valores
    resultado = eval(total_valores) #comando eval para realizar interpretar o calculo da string inserida

    #Passando o resultado do calculo para a tela
    valor_texto.set(str(resultado))

#Função limpar a tela
def limpar_tela():

    global total_valores
    total_valores = "" #limpa o valor já digitado
    valor_texto.set("") #limpa o valor exibido na tela

#Labels
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor2, fg=cor3)
app_label.place(x=0, y=0)

#Botões

#Primeira fila
b_1 = Button(frame_botoes, command=limpar_tela, text="C", width=11, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_botoes, command=lambda: entrada_valor('%'), text="%", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_botoes, command=lambda: entrada_valor('/'), text="/", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

#Segunda fila
b_4 = Button(frame_botoes, command=lambda: entrada_valor('7'), text="7", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_botoes, command=lambda: entrada_valor('8'), text="8", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_botoes, command=lambda: entrada_valor('9'), text="9", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_botoes, command=lambda: entrada_valor('*'), text="*", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

#Terceira fila
b_8 = Button(frame_botoes, command=lambda: entrada_valor('4'), text="4", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_botoes, command=lambda: entrada_valor('5'), text="5", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10 = Button(frame_botoes, command=lambda: entrada_valor('6'), text="6", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11 = Button(frame_botoes, command=lambda: entrada_valor('-'), text="-", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

#Quarta fila
b_12 = Button(frame_botoes, command=lambda: entrada_valor('1'), text="1", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_botoes, command=lambda: entrada_valor('2'), text="2", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_botoes, command=lambda: entrada_valor('3'), text="3", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_botoes, command=lambda: entrada_valor('+'), text="+", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

#Quinta fila
b_16 = Button(frame_botoes, command=lambda: entrada_valor('0'), text="0", width=11, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frame_botoes, command=lambda: entrada_valor('.'), text=".", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18 = Button(frame_botoes, command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)

janela.mainloop()
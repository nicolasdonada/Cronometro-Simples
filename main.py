from tkinter import *
import tkinter


# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul


root = Tk()
root.title("Cronômetro")
root.geometry("500x300")
root.config(bg=cor1)
root.resizable(width=False, height=False)

#Definindo váriaveis globais
global rodar
global tempo
global contador

tempo = "00:00:00"
rodar = False
contador = -5
limitador = 60

#Função para contagem de iniciar o cronômetro
def iniciar():
    global contador
    global tempo
    global rodar
    global limitador

    if rodar:
        #Iniciando o cronômetro
        if contador <= -1:
            inicio = "Começando em " + str(abs(contador))
            label_tempo["text"] = inicio
            label_tempo["font"] = "Arial 40"

        #Trocando para o cronômetro
        else:
            label_tempo["text"] = tempo
            label_tempo["font"] = "Times 90 bold"

            temporaria = str(tempo)
            h,m,s = map(int, temporaria.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)

            if s >= limitador:
                contador = 0
                m += 1
            
            if m > limitador - 1:
                contador = 0 
                h += 1
                m = 0

            if s == limitador:
                contador = 0
                s = 00

            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            #Atualizando os valores do cronômetro
            temporaria = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            label_tempo["text"] = temporaria
            tempo = temporaria

        label_tempo.after(1000, iniciar)
        contador += 1 

#Função para startar a contagem para o cronômetro
def start():
    global rodar
    if rodar == True:
        return False
    rodar = True
    iniciar()

#Função para pausar o cronômetro
def pausar():
    global rodar
    rodar = False

#Função para reiniciar o cronômetro
def reiniciar():
    global rodar
    global tempo
    global contador

    #Reiniciando o tempo e o contador
    contador = 0
    rodar = False
    tempo = "00:00:00"
    label_tempo["text"] = tempo

#Labels ---------------------------------

label_app = Label(root, width=15, height=2, text="CRONÔMETRO", bg=cor1, fg="white", font=("Arial 10"))
label_app.place(x=15, y=8)

label_tempo = Label(root, width=0, height=0, text=tempo, fg=cor4, bg=cor1, font=("times 90 bold"))
label_tempo.place(x=30, y=50)

#Botões ---------------------------------

botao_iniciar = Button(root, width=15, height=2, text="Iniciar", bg=cor1, fg=cor2, font=("Arial 12"), relief="raised", overrelief="ridge", command=start)
botao_iniciar.place(x=35, y=230)

botao_pausar = Button(root, width=15, height=2, text="Pausar", bg=cor1, fg=cor2, font=("Arial 12"), relief="raised", overrelief="ridge", command=pausar)
botao_pausar.place(x=180, y=230)

botao_reiniciar = Button(root, width=15, height=2, text="Reiniciar", bg=cor1, fg=cor2, font=("Arial 12"), relief="raised", overrelief="ridge", command=reiniciar)
botao_reiniciar.place(x=325, y=230)

iniciar()

root.mainloop()
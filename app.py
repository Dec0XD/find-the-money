from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
from tkinter import Toplevel, Label, Canvas
import random
import time

app = CTk()
app.geometry("900x600")
app.resizable(0, 0)

set_appearance_mode("dark")

def MostrarInformaçao():
    CTkMessagebox(title="Informações sobre a aplicação", 
                  message="""
Bem vindo! Vamos dar início ao jogo.\n
Para jogar é bem simples:\n
1. Escolha uma caixinha branca, ou da esquerda ou da direita, e tente encontrar a nota de 100 reais.
2. No início de cada rodada posicione o mouse no círculo vermelho.
3. Cuidado! Se demorar muito para escolher, voltará para o início do jogo.""")
def InfosJogo():
    CTkMessagebox(title="Informações sobre o jogo", 
                message="Se você fizer um tempo menor do que o tempo médio em cada rodada, a nota que você achar terá valor dobrado!")

sidebar_frame = CTkFrame(master=app, fg_color="#070F1F", width=200, height=800, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("assets/GPDOC.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(100, 110))

CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")
CTkLabel(master=sidebar_frame, text="Para mais informações").pack(pady=(38, 0), anchor="center")
CTkLabel(master=sidebar_frame, text="clique aqui").pack(pady=(2, 0), anchor="center")

informationApp = CTkButton(master=sidebar_frame, text="Instruções 1", command=MostrarInformaçao).pack(pady=(10,0), anchor="center")
informationJogo = CTkButton(master=sidebar_frame, text="Instruções 2", command=InfosJogo).pack(pady=(10,0), anchor="center")

def IniciarJogo():
    # Cria uma nova janela
    new_window = Toplevel(app)
    new_window.geometry("900x300")
    
    # Carrega as imagens das notas
    nota_50_img = Image.open("assets/50.jpg")
    nota_2_img = Image.open("assets/2.jpg")
    
    # Redimensiona as imagens para caber no canvas
    nota_50_img = nota_50_img.resize((410, 110))
    nota_2_img = nota_2_img.resize((410, 110))
    
    nota_50_photo = ImageTk.PhotoImage(nota_50_img)
    nota_2_photo = ImageTk.PhotoImage(nota_2_img)
    
    # Cria um canvas para exibir a imagem
    canvas = Canvas(new_window, width=410, height=110)
    canvas.pack()
    
    # Cria botões na nova janela
    BTNEsquerda = CTkButton(master=new_window, text="Botão da esquerda")
    BTNEsquerda.pack(side="left", padx=100, pady=10)
    BTNDireita = CTkButton(master=new_window, text="Botão da direita")
    BTNDireita.pack(side="right", padx=100, pady=10)
    canvas_circulo = Canvas(new_window, width=50, height=50)
    canvas_circulo.pack()
    canvas_circulo.create_oval(5, 5, 45, 45, fill="red")


    
    # Define qual botão terá a nota de 50 reais
    if QuantidadeNotaEsquerda.get() == "":
        percentual_esquerda = 50/100
    else:
        percentual_esquerda = int(QuantidadeNotaEsquerda.get()) / 100

    if NumeroRodadas.get() == "" or NumeroRodadas.get() == "0":
        total_rodadas = 10
    else:
        total_rodadas = int(NumeroRodadas.get())

    rodadas_esquerda = round(total_rodadas * percentual_esquerda)
    rodadas = ["esquerda"] * rodadas_esquerda + ["direita"] * (total_rodadas - rodadas_esquerda)
    random.shuffle(rodadas)
    
    if rodadas == total_rodadas:
        new_window.destroy()

    def acertou():
        tempo_inicio = time.time()
        if not rodadas:  # Se todas as rodadas foram concluídas
            stop_timer()
            timer_label.config(text="Fim do jogo!")
            inciarJogoDois.configure(state=NORMAL)
            return
        canvas.create_image(205, 55, image=nota_50_photo)
        stop_timer()
        new_window.after(2000, lambda: canvas.delete("all"))
        new_window.after(10, lambda: BTNDireita.configure(state=DISABLED))
        new_window.after(2000, lambda: BTNDireita.configure(state=NORMAL))
        new_window.after(10, lambda: BTNEsquerda.configure(state=DISABLED))
        new_window.after(2000, lambda: BTNEsquerda.configure(state=NORMAL))
        new_window.after(2000, start_timer)
        rodada = rodadas.pop(0)
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_2 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_2 = BTNEsquerda
        nota_50.configure(command=acertou)
        nota_2.configure(command=errou)
        tempo_fim = time.time()
        tempo_decorrido = (tempo_fim - tempo_inicio)
        print(f"Tempo decorrido: {tempo_decorrido} milissegundos")

    def errou():
        tempo_inicio = time.time()
        if not rodadas:  # Se todas as rodadas foram concluídas
            stop_timer()
            timer_label.config(text="Fim do jogo!")
            inciarJogoDois.configure(state=NORMAL)
            return
        canvas.create_image(205, 55, image=nota_2_photo)
        stop_timer()
        new_window.after(2000, lambda: canvas.delete("all"))
        new_window.after(10, lambda: BTNDireita.configure(state=DISABLED))
        new_window.after(2000, lambda: BTNDireita.configure(state=NORMAL))
        new_window.after(10, lambda: BTNEsquerda.configure(state=DISABLED))
        new_window.after(2000, lambda: BTNEsquerda.configure(state=NORMAL))
        new_window.after(2000, start_timer)
        rodada = rodadas.pop(0)
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_2 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_2 = BTNEsquerda
        nota_50.configure(command=acertou)
        nota_2.configure(command=errou)
        tempo_fim = time.time()
        tempo_decorrido = (tempo_fim - tempo_inicio)
        print(f"Tempo decorrido: {tempo_decorrido} milissegundos")
        
    for rodada in rodadas:
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_2 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_2 = BTNEsquerda
        nota_50.configure(command=acertou)
        nota_2.configure(command=errou)
    
    # Cria um temporizador
    tempo_restante = 5
    timer_label = Label(new_window, text=f"Tempo restante: {tempo_restante} segundos")
    timer_label.pack()
    
    # Variável de controle para pausar o temporizador
    pausar_temporizador = False
    
    def countdown():
        nonlocal tempo_restante
        if tempo_restante > 0 and not pausar_temporizador:
            tempo_restante -= 1
            timer_label.config(text=f"Tempo restante: {tempo_restante} segundos")
            new_window.after(1000, countdown)
        elif tempo_restante <= 0:
            timer_label.config(text="O tempo acabou!")
            new_window.destroy()
    
    def start_timer():
        if not rodadas:  # Se todas as rodadas foram concluídas
            return
        nonlocal tempo_restante, pausar_temporizador
        tempo_restante = 6
        timer_label.config(text=f"Tempo restante: {tempo_restante} segundos")
        pausar_temporizador = False
        countdown()

    
    def stop_timer():
        nonlocal pausar_temporizador
        pausar_temporizador = True
    
    # Inicia o temporizador
    start_timer()

def iniciarSegundoJogo():
    # Cria uma nova janela
    new_window = Toplevel(app)
    new_window.geometry("900x300")
    
    # Carrega as imagens das notas
    nota_100_img = Image.open("assets/100.jpg")
    nota_50_img = Image.open("assets/50.jpg")
    nota_2_img = Image.open("assets/2.jpg")
    
    # Redimensiona as imagens para caber no canvas
    nota_100_img = nota_100_img.resize((410, 110))
    nota_50_img = nota_50_img.resize((410, 110))
    nota_2_img = nota_2_img.resize((410, 110))
    
    nota_100_photo = ImageTk.PhotoImage(nota_100_img)
    nota_50_photo = ImageTk.PhotoImage(nota_50_img)
    nota_2_photo = ImageTk.PhotoImage(nota_2_img)
    
    # Cria um canvas para exibir a imagem
    canvas = Canvas(new_window, width=410, height=110)
    canvas.pack()
    
    # Cria botões na nova janela
    BTNEsquerda = CTkButton(master=new_window, text="Botão da esquerda")
    BTNEsquerda.pack(side="left", padx=100, pady=10)
    BTNDireita = CTkButton(master=new_window, text="Botão da direita")
    BTNDireita.pack(side="right", padx=100, pady=10)
    canvas_circulo = Canvas(new_window, width=50, height=50)
    canvas_circulo.pack()
    canvas_circulo.create_oval(5, 5, 45, 45, fill="red")
    
    # Define qual botão terá a nota de 50 reais
    if QuantidadeNotaEsquerdaJogoDois.get() == "":
        percentual_esquerdaJogoDois = 50/100
    else:
        percentual_esquerdaJogoDois = int(QuantidadeNotaEsquerdaJogoDois.get()) / 100

    if NumeroRodadasJogoDois.get() == "" or NumeroRodadasJogoDois.get() == "0":
        total_rodadas = 40
    else:
        total_rodadas = int(NumeroRodadasJogoDois.get())

    rodadas_esquerdaJogoDois = round(total_rodadas * percentual_esquerdaJogoDois)
    rodadas = ["esquerda"] * rodadas_esquerdaJogoDois + ["direita"] * (total_rodadas - rodadas_esquerdaJogoDois)
    random.shuffle(rodadas)
    
    if rodadas == total_rodadas:
        new_window.destroy()
    
    tempos_resposta = []
    def acertou():
        tempo_inicio = time.time()
        if not rodadas:  # Se todas as rodadas foram concluídas
            stop_timer()
            timer_label.config(text="Fim do jogo!")
            new_window.after(10, lambda: BTNDireita.configure(state=DISABLED))
            new_window.after(2000, lambda: BTNDireita.configure(state=NORMAL))
            new_window.after(10, lambda: BTNEsquerda.configure(state=DISABLED))
            new_window.after(2000, lambda: BTNEsquerda.configure(state=NORMAL))
            inciarJogoDois.configure(state=NORMAL)
            return
        tempo_fim = time.time()
        tempo_decorrido = (tempo_fim - tempo_inicio)
        tempos_resposta.append(tempo_decorrido)
        media_tempos = sum(tempos_resposta) / len(tempos_resposta)
        if tempo_decorrido < media_tempos:
            imagem_nota = nota_100_photo
        else:
            imagem_nota = nota_50_photo
        canvas.create_image(205, 55, image=imagem_nota)
        stop_timer()
        new_window.after(2000, lambda: canvas.delete("all"))
        new_window.after(2000, start_timer)
        rodada = rodadas.pop(0)
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_2 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_2 = BTNEsquerda
        nota_50.configure(command=acertou)
        nota_2.configure(command=errou)
        print(f"Tempo decorrido: {tempo_decorrido} milissegundos")

    def errou():
        tempo_inicio = time.time()
        if not rodadas:  # Se todas as rodadas foram concluídas
            stop_timer()
            timer_label.config(text="Fim do jogo!")
            new_window.after(10, lambda: BTNDireita.configure(state=DISABLED))
            new_window.after(2000, lambda: BTNDireita.configure(state=NORMAL))
            new_window.after(10, lambda: BTNEsquerda.configure(state=DISABLED))
            new_window.after(2000, lambda: BTNEsquerda.configure(state=NORMAL))
            inciarJogoDois.configure(state=NORMAL)
            return
        canvas.create_image(205, 55, image=nota_2_photo)
        stop_timer()
        new_window.after(2000, lambda: canvas.delete("all"))
        new_window.after(2000, start_timer)
        rodada = rodadas.pop(0)
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_2 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_2 = BTNEsquerda
        nota_50.configure(command=acertou)
        nota_2.configure(command=errou)
        tempo_fim = time.time()
        tempo_decorrido = (tempo_fim - tempo_inicio)
        print(f"Tempo decorrido: {tempo_decorrido} milissegundos")

    for rodada in rodadas:
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_2 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_2 = BTNEsquerda
        nota_50.configure(command=acertou)
        nota_2.configure(command=errou)
    
    # Cria um temporizador
    tempo_restante = 5
    timer_label = Label(new_window, text=f"Tempo restante: {tempo_restante} segundos")
    timer_label.pack()
    
    # Variável de controle para pausar o temporizador
    pausar_temporizador = False
    
    def countdown():
        nonlocal tempo_restante
        if tempo_restante > 0 and not pausar_temporizador:
            tempo_restante -= 1
            timer_label.config(text=f"Tempo restante: {tempo_restante} segundos")
            new_window.after(1000, countdown)
        elif tempo_restante <= 0:
            timer_label.config(text="O tempo acabou!")
            new_window.destroy()
    
    def start_timer():
        nonlocal tempo_restante, pausar_temporizador
        tempo_restante = 6
        timer_label.config(text=f"Tempo restante: {tempo_restante} segundos")
        pausar_temporizador = False
        countdown()
    
    def stop_timer():
        nonlocal pausar_temporizador
        pausar_temporizador = True
    
    # Inicia o temporizador
    start_timer()

CTkLabel(master=app, text="Primeira fase!", text_color="#fff",
        justify="center", font=("Arial Bold", 24)).pack(anchor="center", pady=(10, 5),padx=(25, 0))

CTkLabel(master=app, text="Insira o percentual de vezes que a nota de R$ 50 deverá aparecer do lado esquerdo.", text_color="#fff",
        justify="center", font=("Arial Bold", 16)).pack(anchor="center", pady=(10, 5),padx=(25, 0))
QuantidadeNotaEsquerda = CTkEntry(app, placeholder_text="Apenas Números!")
QuantidadeNotaEsquerda.pack(anchor="center", pady=(5, 5),padx=(25, 0))

CTkLabel(master=app, text="Insira o número de rodadas.", text_color="#fff",
        justify="center", font=("Arial Bold", 16)).pack(anchor="center", pady=(5, 5),padx=(25, 0))

NumeroRodadas = CTkEntry(app, placeholder_text="Apenas Números!")
NumeroRodadas.pack(anchor="center", pady=(0, 5),padx=(25, 0))

CTkLabel(master=app, text="Aperte o botão para iniciar o jogo!", text_color="#fff",
        justify="center", font=("Arial Bold", 16)).pack(anchor="center", pady=(5, 5),padx=(25, 0))  
inciarJogoUm = CTkButton(master=app, text="iniciar Jogo!", text_color="#fff", command=IniciarJogo).pack(anchor="center", pady=(0, 5),padx=(25, 0))

CTkLabel(master=app, text="Segunda fase!", text_color="#fff",
        justify="center", font=("Arial Bold", 24)).pack(anchor="center", pady=(40, 5),padx=(25, 0))  
CTkLabel(master=app, text="Insira o percentual de vezes que a nota de R$ 50 deverá aparecer do lado esquerdo.", text_color="#fff",
        justify="center", font=("Arial Bold", 16)).pack(anchor="center", pady=(10, 5),padx=(25, 0))
QuantidadeNotaEsquerdaJogoDois = CTkEntry(app, placeholder_text="Apenas Números!")
QuantidadeNotaEsquerdaJogoDois.pack(anchor="center", pady=(5, 5),padx=(25, 0))

CTkLabel(master=app, text="Insira o número de rodadas.", text_color="#fff",
        justify="center", font=("Arial Bold", 16)).pack(anchor="center", pady=(5, 5),padx=(25, 0))

NumeroRodadasJogoDois = CTkEntry(app, placeholder_text="Apenas Números!")
NumeroRodadasJogoDois.pack(anchor="center", pady=(0, 5),padx=(25, 0))

CTkLabel(master=app, text="Aperte o botão para iniciar o jogo!", text_color="#fff",
        justify="center", font=("Arial Bold", 16)).pack(anchor="center", pady=(5, 5),padx=(25, 0))  
inciarJogoDois = CTkButton(master=app, text="iniciar Jogo!", text_color="#fff", command=iniciarSegundoJogo, state=DISABLED)
inciarJogoDois.pack(anchor="center", pady=(0, 5),padx=(25, 0))

app.mainloop()
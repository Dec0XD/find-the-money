from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
from tkinter import Toplevel, Label, Canvas, ttk, Frame
import random
import time
import os
import csv

app = CTk()
app.geometry("{}x{}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
app.title("Find the money")

set_appearance_mode("dark")

def MostrarInformaçao():
    MostrarInformaçao = Toplevel()
    MostrarInformaçao.geometry("600x300")  # Ajuste para o tamanho desejado
    MostrarInformaçao.configure(bg='black')
    message = """
Bem vindo! Vamos dar início ao jogo.\n
Para jogar é bem simples:\n
1. Escolha um dos botões, ou da esquerda ou da direita, \ne tente encontrar a nota de 50 reais.
2. No início de cada rodada posicione o mouse no círculo vermelho.
3. Cuidado! Se demorar muito para escolher, voltará para o início do jogo."""
    label = Label(MostrarInformaçao, text=message)
    label.config(font=16, foreground='#fff', background='#000')
    label.pack()

def instruçoes3():
    instruçoes3 = Toplevel()
    instruçoes3.geometry("600x300")  # Ajuste para o tamanho desejado
    instruçoes3.configure(bg='black')
    message = """O jogo tem um formato padrão:
Nas duas fases a porcentagem das notas aparecerem do lado esquerdo é de 50%.
Na primeira fase o número de rodadas é 10.
Na segunda fase o número de rodadas é 40.
O tempo médio para a segunda fase é de 2.5 segundos
Obs: Você pode alterar esses valores escrevendo em suas respectivas caixas."""
    label = Label(instruçoes3, text=message)
    label.config(font=16, foreground='#fff', background='#000')
    label.pack()

def IniciarJogo():
    new_window = Toplevel(app)
    new_window.geometry("{}x{}+0+0".format(new_window.winfo_screenwidth(), new_window.winfo_screenheight()))
    new_window.configure(bg='black')
    
    #Carregando a nota de 50
    nota_50_path = os.path.dirname(os.path.abspath(__file__))
    image_50_path = os.path.join(nota_50_path, 'assets/50.jpg')
    nota_50_img = Image.open(image_50_path)
    #Carregando a nota de 2
    nota_5_path = os.path.dirname(os.path.abspath(__file__))
    image_5_path = os.path.join(nota_5_path, 'assets/5.jpg')
    nota_5_img = Image.open(image_5_path)
    
    nota_50_img = nota_50_img.resize((610, 200))
    nota_5_img = nota_5_img.resize((610, 200))
        
    nota_50_photo = ImageTk.PhotoImage(nota_50_img)
    nota_5_photo = ImageTk.PhotoImage(nota_5_img)

    canvas = Canvas(new_window, width=720, height=310)
    canvas.configure(background='black', highlightbackground='black')
    canvas.pack()
    
    # Cria um Frame para agrupar os botões e o círculo
    frame_botoes = Frame(new_window)
    frame_botoes.configure(background='black')
    frame_botoes.pack()

    BTNEsquerda = CTkButton(master=frame_botoes, text="E", width=150, height=150, fg_color='white', hover=None)
    BTNEsquerda.pack(side="left", padx=220, pady=100)

    canvas_circulo = Canvas(frame_botoes, width=150, height=150)
    canvas_circulo.pack(side="left")
    canvas_circulo.configure(background='black', highlightbackground='black')
    canvas_circulo.create_oval(0, 0, 100, 100, fill="red")

    BTNDireita = CTkButton(master=frame_botoes, text="D", width=150, height=150, fg_color='white', hover=None)
    BTNDireita.pack(side="left", padx=200, pady=100)

    # Define qual botão terá a nota de 50 reais
    if QuantidadeNotaEsquerda.get() == "":
        percentual_esquerda = 50/100
    elif int(QuantidadeNotaEsquerda.get()) >= 100:
        percentual_esquerda = 100/100
    else:
        percentual_esquerda = int(QuantidadeNotaEsquerda.get()) / 100

    if NumeroRodadas.get() == "" or NumeroRodadas.get() == "0":
        total_rodadas = 10
    else:
        total_rodadas = int(NumeroRodadas.get())

    rodadas_esquerda = round(total_rodadas * percentual_esquerda)
    rodadas = ["esquerda"] * rodadas_esquerda + ["direita"] * (total_rodadas - rodadas_esquerda)
    random.shuffle(rodadas)
    
    def FimDeJogo():
        new_window.after(10, lambda: BTNDireita.configure(state=DISABLED))
        new_window.after(10, lambda: BTNEsquerda.configure(state=DISABLED))
        
    global tempo_inicio, pontos, acerto, Total_Esquerdas, duracao, media_tempos
    pontos = 0 
    acerto = 0
    Total_Esquerdas = 0 
    duracao = 0
    tempo_inicio = time.time()
        
    tempos_resposta = []
    def acertou(button_clicked):
        global tempo_inicio, pontos, acerto, Total_Esquerdas, duracao, media_tempos
        duracao = tempo_inicio
        tempo_fim = time.time()
        tempo_decorrido = (tempo_fim - tempo_inicio)
        tempo_inicio = time.time()
        tempos_resposta.append(tempo_decorrido)

        media_tempos = sum(tempos_resposta) / len(tempos_resposta)

        if not rodadas:
            stop_timer()
            timer_label.config(font=40, foreground='#fff', background='#000',
                            text=f"Fim do jogo!\n Acumulado R$:{pontos}\n Acertos:{acerto}\n Total Esquerda:{Total_Esquerdas}\n Média de tempo: {media_tempos:.2f}")
            inciarJogoDois.configure(state=NORMAL)
            informationJogo.configure(state=NORMAL)
            FimDeJogo()

            with open('jogo_info.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Acumulado", "Acertos", "Total Esquerda", "Média de tempo"])
                writer.writerow([pontos, acerto, Total_Esquerdas, media_tempos])

            return

        button_clicked.configure(fg_color='red')  # Muda a cor para vermelho
        
        stop_timer()
        pontos += 50
        acerto += 1
        Total_Esquerdas += 1
        duracao = tempo_inicio
        print(f"Pontuação: {pontos}")
        new_window.after(500, lambda :canvas.create_image(390, 170, image=nota_50_photo))
        new_window.after(1000, lambda: canvas.delete("all"))
        new_window.after(500, lambda: button_clicked.configure(fg_color='SystemButtonFace'))  # Restaura a cor original
        new_window.after(10, lambda: BTNDireita.configure(state=DISABLED))
        new_window.after(1000, lambda: BTNDireita.configure(state=NORMAL))
        new_window.after(10, lambda: BTNEsquerda.configure(state=DISABLED))
        new_window.after(1000, lambda: BTNEsquerda.configure(state=NORMAL))
        new_window.after(1000, start_timer)
        rodada = rodadas.pop(0)
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_5 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_5 = BTNEsquerda
        nota_50.configure(command=lambda: acertou(nota_50))
        nota_5.configure(command=lambda: errou(nota_5))

    def errou(button_clicked):
        global tempo_inicio, pontos, acerto, Total_Esquerdas, duracao, media_tempos
        duracao = tempo_inicio
        tempo_fim = time.time()
        tempo_decorrido = (tempo_fim - tempo_inicio)
        tempo_inicio = time.time()
        tempos_resposta.append(tempo_decorrido)

        media_tempos = sum(tempos_resposta) / len(tempos_resposta)

        if not rodadas:
            stop_timer()
            timer_label.config(font=40, foreground='#fff', background='#000',
                            text=f"Fim do jogo!\n Acumulado R$:{pontos}\n Acertos:{acerto}\n Total Esquerda:{Total_Esquerdas}\n Média de tempo: {media_tempos:.2f}")
            inciarJogoDois.configure(state=NORMAL)
            informationJogo.configure(state=NORMAL)
            FimDeJogo()

            with open('jogo_info.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Acumulado", "Acertos", "Total Esquerda", "Média de tempo"])
                writer.writerow([pontos, acerto, Total_Esquerdas, media_tempos])

            return

        button_clicked.configure(fg_color='red')  # Muda a cor para vermelho
        stop_timer()
        pontos += 5
        new_window.after(500, lambda :canvas.create_image(390, 170, image=nota_5_photo))
        new_window.after(1000, lambda: canvas.delete("all"))
        new_window.after(500, lambda: button_clicked.configure(fg_color='SystemButtonFace'))  # Restaura a cor original
        new_window.after(10, lambda: BTNDireita.configure(state=DISABLED))
        new_window.after(1000, lambda: BTNDireita.configure(state=NORMAL))
        new_window.after(10, lambda: BTNEsquerda.configure(state=DISABLED))
        new_window.after(1000, lambda: BTNEsquerda.configure(state=NORMAL))
        new_window.after(1000, start_timer)
        rodada = rodadas.pop(0)
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_5 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_5 = BTNEsquerda
        nota_50.configure(command=lambda: acertou(nota_50))
        nota_5.configure(command=lambda: errou(nota_5))

    for rodada in rodadas:
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_5 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_5 = BTNEsquerda
        nota_50.configure(command=lambda: acertou(nota_50))
        nota_5.configure(command=lambda: errou(nota_5))



    # Cria um temporizador
    tempo_total = 5
    tempo_restante = 0
    timer_label = Label(new_window)
    timer_label.pack()

    # Adicione uma barra de progresso
    style = ttk.Style()
    style.configure("TProgressbar", thickness=50)

    progress = ttk.Progressbar(new_window, length=300, mode='determinate', maximum=tempo_total, style="TProgressbar")
    progress.pack()

    # Variável de controle para pausar o temporizador
    pausar_temporizador = False

    def countdown():
        nonlocal tempo_restante
        if tempo_restante < tempo_total and not pausar_temporizador:
            tempo_restante += 1
            timer_label.configure(background='black')
            progress['value'] = tempo_restante  # Atualiza a barra de progresso
            new_window.after(1000, countdown)
        elif tempo_restante >= tempo_total:
            timer_label.config(font=40,foreground='#fff', background='#000', text="O tempo acabou!")
            new_window.destroy()

    def start_timer():
        if not rodadas:  # Se todas as rodadas foram concluídas
            return
        nonlocal tempo_restante, pausar_temporizador
        tempo_restante = 0
        progress['value'] = 0  # Reinicia a barra de progresso
        pausar_temporizador = False
        countdown()

    def stop_timer():
        nonlocal pausar_temporizador
        pausar_temporizador = True
    
    # Inicia o temporizador
    start_timer()

def iniciarSegundoJogo():
    new_window = Toplevel(app)
    new_window.geometry("{}x{}+0+0".format(new_window.winfo_screenwidth(), new_window.winfo_screenheight()))
    new_window.configure(bg='black')
    
    #Carregando a nota de 100
    nota_100_path = os.path.dirname(os.path.abspath(__file__))
    image_100_path = os.path.join(nota_100_path, 'assets/100.jpg')
    nota_100_img = Image.open(image_100_path)
    #Carregando a nota de 50
    nota_50_path = os.path.dirname(os.path.abspath(__file__))
    image_50_path = os.path.join(nota_50_path, 'assets/50.jpg')
    nota_50_img = Image.open(image_50_path)
    #Carregando a nota de 10
    nota_10_path = os.path.dirname(os.path.abspath(__file__))
    image_10_path = os.path.join(nota_10_path, 'assets/10.jpg')
    nota_10_img = Image.open(image_10_path)
    #Carregando a nota de 2
    nota_5_path = os.path.dirname(os.path.abspath(__file__))
    image_5_path = os.path.join(nota_5_path, 'assets/5.jpg')
    nota_5_img = Image.open(image_5_path)
        
    nota_100_img = nota_100_img.resize((610, 200))
    nota_50_img = nota_50_img.resize((610, 200))
    nota_10_img = nota_10_img.resize((610, 200))
    nota_5_img = nota_5_img.resize((610, 200))
        
    nota_100_photo = ImageTk.PhotoImage(nota_100_img)
    nota_50_photo = ImageTk.PhotoImage(nota_50_img)
    nota_10_photo = ImageTk.PhotoImage(nota_10_img)
    nota_5_photo = ImageTk.PhotoImage(nota_5_img)
    
    canvas = Canvas(new_window, width=710, height=300)
    canvas.configure(background='black', highlightbackground='black')
    canvas.pack()
    
    # Cria um Frame para agrupar os botões e o círculo
    frame_botoes = Frame(new_window)
    frame_botoes.configure(background='black')
    frame_botoes.pack()

    # Cria botões e o círculo dentro do Frame
    BTNEsquerda = CTkButton(master=frame_botoes, text="E", width=150, height=150, fg_color='white', hover=None)
    BTNEsquerda.pack(side="left", padx=220, pady=100)

    canvas_circulo = Canvas(frame_botoes, width=150, height=150)
    canvas_circulo.pack(side="left")
    canvas_circulo.configure(background='black', highlightbackground='black')
    canvas_circulo.create_oval(0, 0, 100, 100, fill="red")

    BTNDireita = CTkButton(master=frame_botoes, text="D", width=150, height=150, fg_color='white', hover=None)
    BTNDireita.pack(side="left", padx=200, pady=100)

    
    # Define qual botão terá a nota de 50 reais
    if QuantidadeNotaEsquerdaJogoDois.get() == "":
        percentual_esquerdaJogoDois = 50/100
    elif int(QuantidadeNotaEsquerdaJogoDois.get()) >= 100:
        percentual_esquerdaJogoDois = 100/100
    else:
        percentual_esquerdaJogoDois = int(QuantidadeNotaEsquerdaJogoDois.get()) / 100

    if NumeroRodadasJogoDois.get() == "" or NumeroRodadasJogoDois.get() == "0":
        total_rodadas = 40
    else:
        total_rodadas = int(NumeroRodadasJogoDois.get())
    
    if mediajogo.get() == "" or mediajogo.get() == "0":
        quantidadetempo = media_tempos
    else:
        quantidadetempo = float(mediajogo.get())
        
    rodadas_esquerdaJogoDois = round(total_rodadas * percentual_esquerdaJogoDois)
    rodadas = ["esquerda"] * rodadas_esquerdaJogoDois + ["direita"] * (total_rodadas - rodadas_esquerdaJogoDois)
    random.shuffle(rodadas)
    
    if rodadas == total_rodadas:
        new_window.destroy()
    
    def FimDeJogo():
        new_window.after(10, lambda: BTNDireita.configure(state=DISABLED))
        new_window.after(10, lambda: BTNEsquerda.configure(state=DISABLED))
        
    global tempo_inicio, pontos, acerto, Total_Esquerdas, duracao
    pontos = 0 
    acerto = 0
    Total_Esquerdas = 0 
    duracao = 0
    tempo_inicio = time.time()
        
    tempos_resposta = []
    def acertou(button_clicked):
        global tempo_inicio, pontos, acerto, duracao
        duracao = tempo_inicio
        tempo_fim = time.time()
        tempo_decorrido = (tempo_fim - tempo_inicio - 1)
    
        tempos_resposta.append(tempo_decorrido)

        media_tempos = sum(tempos_resposta) / len(tempos_resposta)
        print('acertou',tempo_decorrido, quantidadetempo)
        if not rodadas:
            stop_timer()
            timer_label.config(font=40, foreground='#fff', background='#000',
                            text=f"Fim do jogo!\n Acumulado R$:{pontos}\n Acertos:{acerto}\n Média de tempo: {media_tempos:.2f}")
            inciarJogoDois.configure(state=NORMAL)
            FimDeJogo()

            with open('jogo_info_Fase2.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Acumulado", "Acertos", "Média de tempo"])
                writer.writerow([pontos, acerto, media_tempos])

            return

        button_clicked.configure(fg_color='red')  # Muda a cor para vermelho
        if tempo_decorrido < quantidadetempo:
            imagem_nota = nota_100_photo
            pontos += 100
        else:
            imagem_nota = nota_50_photo
            pontos += 50
        stop_timer()
        acerto += 1
        new_window.after(500, lambda :canvas.create_image(390, 170, image=imagem_nota))
        new_window.after(1000, lambda: canvas.delete("all"))
        new_window.after(500, lambda: button_clicked.configure(fg_color='SystemButtonFace'))  # Restaura a cor original
        new_window.after(10, lambda: BTNDireita.configure(state=DISABLED))
        new_window.after(1000, lambda: BTNDireita.configure(state=NORMAL))
        new_window.after(10, lambda: BTNEsquerda.configure(state=DISABLED))
        new_window.after(1000, lambda: BTNEsquerda.configure(state=NORMAL))
        new_window.after(1000, start_timer)
        rodada = rodadas.pop(0)
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_5 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_5 = BTNEsquerda
        nota_50.configure(command=lambda: acertou(nota_50))
        nota_5.configure(command=lambda: errou(nota_5))

    def errou(button_clicked):
        global tempo_inicio, pontos, acerto, duracao
        duracao = tempo_inicio
        tempo_fim = time.time()
        tempo_decorrido = (tempo_fim - tempo_inicio - 1)
        tempo_inicio = time.time()
        tempos_resposta.append(tempo_decorrido)

        media_tempos = sum(tempos_resposta) / len(tempos_resposta)
        print('errou',tempo_decorrido, media_tempos)
        if not rodadas:
            stop_timer()
            timer_label.config(font=40, foreground='#fff', background='#000',
                            text=f"Fim do jogo!\n Acumulado R$:{pontos}\n Acertos:{acerto}\n Média de tempo: {media_tempos:.2f}")
            inciarJogoDois.configure(state=NORMAL)
            FimDeJogo()

            with open('jogo_info_Fase2.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Acumulado", "Acertos", "Média de tempo"])
                writer.writerow([pontos, acerto, media_tempos])

            return

        button_clicked.configure(fg_color='red')  # Muda a cor para vermelho
        if tempo_decorrido < quantidadetempo:
            imagem_nota = nota_10_photo
            pontos += 10
        else:
            imagem_nota = nota_5_photo
            pontos += 5
        stop_timer()
        new_window.after(500, lambda :canvas.create_image(390, 170, image=imagem_nota))
        new_window.after(1000, lambda: canvas.delete("all"))
        new_window.after(500, lambda: button_clicked.configure(fg_color='SystemButtonFace'))  # Restaura a cor original
        new_window.after(10, lambda: BTNDireita.configure(state=DISABLED))
        new_window.after(1000, lambda: BTNDireita.configure(state=NORMAL))
        new_window.after(10, lambda: BTNEsquerda.configure(state=DISABLED))
        new_window.after(1000, lambda: BTNEsquerda.configure(state=NORMAL))
        new_window.after(1000, start_timer)
        rodada = rodadas.pop(0)
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_5 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_5 = BTNEsquerda
        nota_50.configure(command=lambda: acertou(nota_50))
        nota_5.configure(command=lambda: errou(nota_5))

    for rodada in rodadas:
        if rodada == "esquerda":
            nota_50 = BTNEsquerda
            nota_5 = BTNDireita
        else:
            nota_50 = BTNDireita
            nota_5 = BTNEsquerda
        nota_50.configure(command=lambda: acertou(nota_50))
        nota_5.configure(command=lambda: errou(nota_5))

    
        # Cria um temporizador
    tempo_total = 5
    tempo_restante = 0
    timer_label = Label(new_window)
    timer_label.pack()

    # Adicione uma barra de progresso
    style = ttk.Style()
    style.configure("TProgressbar", thickness=50)

    progress = ttk.Progressbar(new_window, length=300, mode='determinate', maximum=tempo_total, style="TProgressbar")
    progress.pack()

    # Variável de controle para pausar o temporizador
    pausar_temporizador = False

    def countdown():
        nonlocal tempo_restante
        if tempo_restante < tempo_total and not pausar_temporizador:
            tempo_restante += 1
            timer_label.configure(background='black')
            progress['value'] = tempo_restante  # Atualiza a barra de progresso
            new_window.after(1000, countdown)
        elif tempo_restante >= tempo_total:
            timer_label.config(font=40,foreground='#fff', background='#000', text="O tempo acabou!")
            new_window.destroy()

    def start_timer():
        if not rodadas:  # Se todas as rodadas foram concluídas
            return
        nonlocal tempo_restante, pausar_temporizador
        tempo_restante = 0
        progress['value'] = 0  # Reinicia a barra de progresso
        pausar_temporizador = False
        countdown()

    def stop_timer():
        nonlocal pausar_temporizador
        pausar_temporizador = True
    
    # Inicia o temporizador
    start_timer()

def InfosJogo():
    InfosJogo = Toplevel()
    InfosJogo.geometry("600x400")  # Ajuste para o tamanho desejado
    InfosJogo.configure(bg='black')
    message = f"""
No segundo jogo, o tempo será seu maior aliado (ou não)! 
Se você conseguir um tempo menor do que a média das outras pessoas 
em cada rodada, a nota que você encontrar terá seu valor dobrado. 

Por exemplo, considere que a média de tempo das pessoas que jogaram 
foi de 2 segundos e você apertou um dos lados em 1.5 segundos. Se 
você acertar o lugar da nota de 50, a nota e a pontuação que você 
receberá será de 100! O mesmo acontece para a nota de 5, que se 
transformará em 10!
No primeiro jogo, os resultados foram os seguintes: 
- Tempo médio da população: 1.3 s
- Seu tempo: {media_tempos:.2f}

Nesse caso, você tem que apertar o botão em menos de 1.3 segundos 
para ganhar o valor dobrado!

    """
    label_text = Label(InfosJogo, text=message)
    label_text.config(font=16, foreground='#fff', background='#000')
    label_text.pack()
def validate_input(event):
    # Verifica se o valor inserido é um dígito, a tecla backspace ou o ponto
    if not (event.char.isdigit() or event.char == "." or event.keysym == "BackSpace"):
        return "break"  # Ignora o evento se não for um dígito, ponto ou backspace
    elif event.char == "." and event.widget.get().count(".") > 0:
        return "break"  # Impede mais de um ponto na entrada
    
#Configuração do sidebar
sidebar_frame = CTkFrame(master=app, fg_color="#070F1F", width=500, height=800, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

#carregando a foto do GPDOC
logo_path = os.path.dirname(os.path.abspath(__file__))
image_logo_path = os.path.join(logo_path, 'assets/GPDOC.png')
logo_img_data = Image.open(image_logo_path)

logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(300, 310))

CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")
CTkLabel(master=sidebar_frame, text="Para mais informações", font=("Arial Bold", 16)).pack(pady=(38, 0), anchor="center")
#CTkLabel(master=sidebar_frame, text="clique aqui").pack(pady=(2, 0), anchor="center")

informationApp = CTkButton(master=sidebar_frame, text="Instruções Primeira Fase", command=MostrarInformaçao, width=200, height=50).pack(pady=(10,0), anchor="center")
informationJogo = CTkButton(master=sidebar_frame, text="Instruções Segunda Fase", command=InfosJogo, width=200, height=50, state=DISABLED)
informationJogo.pack(pady=(10,0), anchor="center")
informationJogo2 = CTkButton(master=sidebar_frame, text="Informações sobre o jogo", command=instruçoes3, width=200, height=50).pack(pady=(10,0), anchor="center")
# Final do sidebar

#Teste Scroll
#scrollable_content_frame = CTkScrollableFrame(master=app, fg_color="#CEC9DF")
#scrollable_content_frame.pack(expand=True, fill="both", padx=20, pady=20)

#Tela principal
CTkLabel(master=app, text="Primeira fase!", text_color="#fff",
        justify="center", font=("Arial Bold", 32)).pack(anchor="center", pady=(10, 5),padx=(25, 0))

CTkLabel(master=app, text="Insira o percentual (%) de vezes que a nota de R$ 50 deverá aparecer do lado esquerdo.", text_color="#fff",
        justify="center", font=("Arial Bold", 24)).pack(anchor="center", pady=(10, 5),padx=(25, 0))

QuantidadeNotaEsquerda = CTkEntry(app, placeholder_text="Apenas Números!", width=200, height=50)
QuantidadeNotaEsquerda.pack(anchor="center", pady=(5, 5),padx=(25, 0))
QuantidadeNotaEsquerda.bind("<Key>", validate_input)

CTkLabel(master=app, text="Insira o número de rodadas.", text_color="#fff",
        justify="center", font=("Arial Bold", 24)).pack(anchor="center", pady=(5, 5),padx=(25, 0))

NumeroRodadas = CTkEntry(app, placeholder_text="Apenas Números!", width=200, height=50)
NumeroRodadas.pack(anchor="center", pady=(0, 5),padx=(25, 0))
NumeroRodadas.bind("<Key>", validate_input)

CTkLabel(master=app, text="Aperte o botão para iniciar o jogo!", text_color="#fff",
        justify="center", font=("Arial Bold", 24)).pack(anchor="center", pady=(5, 5),padx=(25, 0))  
inciarJogoUm = CTkButton(master=app, text="iniciar Jogo!", text_color="#fff", command=IniciarJogo, width=200, height=50)
inciarJogoUm.pack(anchor="center", pady=(0, 5), padx=(25, 0))

CTkLabel(master=app, text="Segunda fase!", text_color="#fff",
        justify="center", font=("Arial Bold", 32)).pack(anchor="center", pady=(40, 5),padx=(25, 0))  
CTkLabel(master=app, text="Insira o percentual (%) de vezes que a nota de R$ 50 deverá aparecer do lado esquerdo.", text_color="#fff",
        justify="center", font=("Arial Bold", 24)).pack(anchor="center", pady=(10, 5),padx=(25, 0))

QuantidadeNotaEsquerdaJogoDois = CTkEntry(app, placeholder_text="Apenas Números!", width=200, height=50)
QuantidadeNotaEsquerdaJogoDois.pack(anchor="center", pady=(5, 5),padx=(25, 0))
QuantidadeNotaEsquerdaJogoDois.bind("<Key>", validate_input)

CTkLabel(master=app, text="Insira o número de rodadas.", text_color="#fff",
        justify="center", font=("Arial Bold", 24)).pack(anchor="center", pady=(5, 5),padx=(25, 0))

NumeroRodadasJogoDois = CTkEntry(app, placeholder_text="Apenas Números!", width=200, height=50)
NumeroRodadasJogoDois.pack(anchor="center", pady=(0, 5),padx=(25, 0))
NumeroRodadasJogoDois.bind("<Key>", validate_input)

CTkLabel(master=app, text="Insira a média de tempo desejada.", text_color="#fff",
        justify="center", font=("Arial Bold", 24)).pack(anchor="center", pady=(5, 5),padx=(25, 0))

mediajogo = CTkEntry(app, placeholder_text="Apenas Números! Ex:2.5", width=200, height=50)
mediajogo.pack(anchor="center", pady=(0, 5),padx=(25, 0))
mediajogo.bind("<Key>", validate_input)

CTkLabel(master=app, text="Aperte o botão para iniciar o jogo!", text_color="#fff",
        justify="center", font=("Arial Bold", 24)).pack(anchor="center", pady=(5, 5),padx=(25, 0))  
inciarJogoDois = CTkButton(master=app, text="iniciar Jogo!", text_color="#fff", command=iniciarSegundoJogo, state=DISABLED, width=200, height=50)
inciarJogoDois.pack(anchor="center", pady=(0, 5),padx=(25, 0))

app.mainloop()
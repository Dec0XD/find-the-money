from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image

app = CTk()
app.geometry("900x600")
app.resizable(0, 0)

set_appearance_mode("dark")

def MostrarInformaçao():
    CTkMessagebox(title="Informações sobre a aplicação", 
                  message="Informações.")

sidebar_frame = CTkFrame(master=app, fg_color="#070F1F", width=200, height=800, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("assets/GPDOC.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(100, 110))

CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")
CTkLabel(master=sidebar_frame, text="Para mais informações").pack(pady=(38, 0), anchor="center")
CTkLabel(master=sidebar_frame, text="clique aqui").pack(pady=(2, 0), anchor="center")

information = CTkButton(master=sidebar_frame, text="informações", command=MostrarInformaçao).pack(pady=(10,0), anchor="center")

def InfosJogo():
    CTkMessagebox(title="Informações sobre o jogo", 
                message="""
Bem vindo! Vamos dar início ao jogo.\n
Para jogar é bem simples:\n
1. Escolha uma caixinha branca, ou da esquerda ou da direita, e tente encontrar a nota de 100 reais.
2. No início de cada rodada posicione o mouse no círculo vermelho.
3. Cuidado! Se demorar muito para escolher, voltará para o início do jogo."""
                )


def IniciarJogo():
    NotaEsquerda = QuantidadeNotaEsquerda.get()
    NRodadas = NumeroRodadas.get()
    print(NotaEsquerda)
    print(NRodadas)
    
CTkLabel(master=app, text="Configuração", text_color="#fff",
        justify="center", font=("Arial Bold", 24)).pack(anchor="center", pady=(0, 5),padx=(25, 0))

CTkLabel(master=app, text="Insira o percentual de vezes que a nota de R$ 100 deverá aparecer do lado esquerdo.", text_color="#fff",
        justify="center", font=("Arial Bold", 16)).pack(anchor="center", pady=(0, 5),padx=(25, 0))
QuantidadeNotaEsquerda = CTkEntry(app, placeholder_text="Apenas Números!")
QuantidadeNotaEsquerda.pack(padx=20, pady=20)

CTkLabel(master=app, text="Insira o número de rodadas.", text_color="#fff",
        justify="center", font=("Arial Bold", 16)).pack(anchor="center", pady=(0, 5),padx=(25, 0))
NumeroRodadas = CTkEntry(app, placeholder_text="Apenas Números!")
NumeroRodadas.pack(padx=20, pady=20)

CTkLabel(master=app, text="Aperte o botão para iniciar o jogo!", text_color="#fff",
        justify="center", font=("Arial Bold", 16)).pack(anchor="center", pady=(0, 5),padx=(25, 0))  
inciarJogo = CTkButton(master=app, text="inicar Jogo!", text_color="#fff", command=InfosJogo).pack(anchor="center")



app.mainloop()
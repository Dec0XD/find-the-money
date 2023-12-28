from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image

app = CTk()
app.geometry("900x600")
app.resizable(0, 0)

set_appearance_mode("dark")

sidebar_frame = CTkFrame(master=app, fg_color="#070F1F", width=200, height=800, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("assets/GPDOC.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(100, 110))

CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")
CTkLabel(master=sidebar_frame, text="Para mais informações").pack(pady=(38, 0), anchor="center")
CTkLabel(master=sidebar_frame, text="clique aqui").pack(pady=(2, 0), anchor="center")



app.mainloop()
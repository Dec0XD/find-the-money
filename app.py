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


app.mainloop()
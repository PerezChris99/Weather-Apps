from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezone import Timezone
from datetime import datetime
import requests
import pytz
import json

root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

#search box
search_image=PhotoImage(file="search.png")
myimage=Label(root,image=search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search.png")
myimage=Label(root,image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040")
myimage.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="logo.png")

root.mainloop()






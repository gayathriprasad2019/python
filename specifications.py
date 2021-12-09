import tkinter as tk
from PIL import Image,ImageTk


window = tk.Tk()
window.title("Specifications")



text = tk.Text(window, background="SeaGreen",fg="black",height=8, width=50)
scroll = tk.Scrollbar(window)
text.configure(yscrollcommand=scroll.set)
text.pack(side=tk.LEFT)


scroll.config(command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

insert_text = """Specifications

Emission Norm Compliance :BS VI
Engine Displ. :1997 cc
Max Power :246.74bhp@5500rpm
Max Torque :365NM@1500-4000rpm
Top Speed :217 Km/h
Sunroof :NA
Adjustable Driver Seat :Yes
Adj. Front Passenger Seat :Yes
Heated/Cooled Seats :NA """

text.insert(tk.END, insert_text)
tk.mainloop()

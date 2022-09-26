# import time
# for i in range(10):
# 	print(f"{i+1}",end="\r")
# 	time.sleep(.1)
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

root = tk.Tk()
root.title('hidroponik desa songo')
root.geometry('300x70')

def farenheit_to_celcius(f):
	"""Convert farenheit to celcius"""
	return (f-32) * 5/9


frame = ttk.Frame(root)
options = {'padx':5, 'pady':5}

# sensor tangki 3 float

# tangki1_entry = tk.StringVar()
# tangki1_entry = ttk.Entry(frame, textvariable="testas")
# tangki1_entry.grid(column=1, row=0, **options)

# sensor tds 1 float
# aktuator pompa 4 boolean
# ppm target 1 int 1-1500

tangki1_label = ttk.Label(frame, text='farenheit')
tangki1_label.grid(column=0, row=0, sticky='W', **options)

tangki1 = tk.StringVar()
tangki1_entry = ttk.Entry(frame, textvariable=tangki1)
tangki1_entry.grid(column=1, row=0, **options)
tangki1_entry.focus()

def convert_button_clicked():
	"""Handle convert button click event"""
	try:
		f = float(tangki1.get())
		c = farenheit_to_celcius(f)
		result = f"{f} Farenheit = {c:.2f} Celcius"
		result_label.config(text=result)
	except ValueError as error:
		showerror(title="Error", message=error)

result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

convert_button = ttk.Button(frame, text="Convert")
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

frame.grid(padx=10, pady=10)
root.mainloop()
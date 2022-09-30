# import time
# for i in range(10):
# 	print(f"{i+1}",end="\r")
# 	time.sleep(.1)
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

root = tk.Tk()
root.title('hidroponik desa songo')
root.geometry('800x600')

frame = ttk.Frame(root)
options = {'padx':5, 'pady':5}

# sensor tangki 3 float

# tangki1_entry = tk.StringVar()
# tangki1_entry = ttk.Entry(frame, textvariable="testas")
# tangki1_entry.grid(column=1, row=0, **options)

# sensor tds 1 float
# aktuator pompa 4 boolean
# ppm target 1 int 1-1500

hidroponik_Label = ttk.Label(frame)
hidroponik_Label.config(text='hidroponik')
hidroponik_Label.grid(row=0, column=1, **options)

frame.grid(padx=10, pady=10)
root.mainloop()

# def farenheit_to_celcius(f):
# 	"""Convert farenheit to celcius"""
# 	return (f-32) * 5/9

# def convert_button_clicked():
# 	"""Handle convert button click event"""
# 	try:
# 		f = float(tangki1.get())
# 		c = farenheit_to_celcius(f)
# 		result = f"{f} Farenheit = {c:.2f} Celcius"
# 		result_label.config(text=result)
# 	except ValueError as error:
# 		showerror(title="Error", message=error)


# tangki1_label = ttk.Label(frame, text='farenheit')
# tangki1_label.grid(column=0, row=1, sticky='W', **options)

# tangki1 = tk.StringVar()
# tangki1_entry = ttk.Entry(frame, textvariable=tangki1)
# tangki1_entry.grid(column=1, row=1, **options)
# tangki1_entry.focus()

# result_label = ttk.Label(frame)
# result_label.grid(row=2, columnspan=3, **options)

# convert_button = ttk.Button(frame, text="Convert")
# convert_button.grid(column=2, row=1, sticky='W', **options)
# convert_button.configure(command=convert_button_clicked)

# arduino
# int x;
# int a;
# String def = "#6";

# void setup() {
#  Serial.begin(9600);

# }
# void loop() {
#  if (Serial.available() == 0);
#  String x = Serial.readString();
#  x.trim();
#  if (x != def && x != "") def = x;
#     Serial.print(def);
#     Serial.print("#");
#     Serial.println("6");
# }

# sensor Ultrasonik 3 r
# sensor tds 1 r
# aktuator pompa 4 w/r, 0/1
# aktuator mode 1 w/r, 0/1
# nilai ppm target 1 w/r, 0-1500
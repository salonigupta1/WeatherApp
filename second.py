import tkinter as tk
from tkinter import Menu
from tkinter import ttk

def _quit():
    win.quit()
    win.destroy()
    exit()
    
win = tk.Tk()
win.title("Python Projects")

menuBar = Menu()
win.config(menu = menuBar)

fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = _quit)
menuBar.add_cascade(label = "File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff = 0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label = "About")
menuBar.add_cascade(label = "Help", menu=helpMenu)

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill="both")

 

weather_conditions_frame = ttk.Labelframe(tab1, text= 'Current weather condtions')
weather_conditions_frame.grid(column=0, row=0, padx=8, pady=4)
weather_conditions_frame.grid_configure(column=0, row=1, padx=8, pady=4)  

weather_cities_frame = ttk.LabelFrame(tab1, text='Latest Observation for ')
weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)


ttk.Label(weather_cities_frame, text="Location:  ").grid(column=0, row=0)

city =tk.StringVar()
citySelected = ttk.Combobox(weather_cities_frame, width=24, textvariable=city)
citySelected['values'] = ('Los Angeles', 'London', 'Rio de Janeiro, Brazil')
citySelected.grid(column=1, row=0)
citySelected.current(0)

max_width = max([len(x)for x in citySelected['values']])
new_width = max_width
new_width = max_width - 4
citySelected.config(width=new_width)

ENTRY_WIDTH = max_width + 3
ttk.Label(weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='W')
updated = tk.StringVar()
updatedEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')


ttk.Label(weather_conditions_frame, text="Weather:").grid(column=0, row=2, sticky='W')
weather = tk.StringVar()
weatherEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=weather, state='readonly')
weatherEntry.grid(column=1, row=2, sticky='W')

ttk.Label(weather_conditions_frame, text="Temperature:").grid(column=0, row=3, sticky='W')
temp = tk.StringVar()
tempEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=temp, state='readonly')
tempEntry.grid(column=1, row=3, sticky='W')

ttk.Label(weather_conditions_frame, text="Dewpoint:").grid(column=0, row=4, sticky='W')
dew = tk.StringVar()
dewEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=dew, state='readonly')
dewEntry.grid(column=1, row=4, sticky='W')

ttk.Label(weather_conditions_frame, text="Relative Humidity:").grid(column=0, row=5, sticky='W')
humidity = tk.StringVar()
humidityEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=humidity, state='readonly')
humidityEntry.grid(column=1, row=5, sticky='W')

ttk.Label(weather_conditions_frame, text="Wind:").grid(column=0, row=6, sticky='W')
wind = tk.StringVar()
windEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wind, state='readonly')
windEntry.grid(column=1, row=6, sticky='W')

ttk.Label(weather_conditions_frame, text="Visibility:").grid(column=0, row=7, sticky='W')
visibility = tk.StringVar()
visibilityEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=visibility, state='readonly')
visibilityEntry.grid(column=1, row=7, sticky='W')

ttk.Label(weather_conditions_frame, text="MSL Pressure:").grid(column=0, row=8, sticky='W')
msl = tk.StringVar()
mslEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=msl, state='readonly')
mslEntry.grid(column=1, row=8, sticky='W')

ttk.Label(weather_conditions_frame, text="Altimeter:").grid(column=0, row=10, sticky='W')
altimeter = tk.StringVar()
altimeterEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=altimeter, state='readonly')
altimeterEntry.grid(column=1, row=10, sticky='W')

for child in weather_conditions_frame.winfo_children():
    child.grid_configure(padx=6, pady=6)
    child.grid_configure(padx=4, pady=2)
    

ttk.Label(weather_cities_frame, text="Location:  ").grid(column=0, row=0)

city =tk.StringVar()
citySelected = ttk.Combobox(weather_cities_frame, width=24, textvariable=city)
citySelected['values'] = ('Los Angeles', 'London', 'Rio de Janeiro, Brazil')
citySelected.grid(column=1, row=0)
citySelected.current(0)





win.mainloop()


import tkinter as tk
from tkinter import Menu
from tkinter import ttk


def _quit():
    win.quit()
    win.destroy()
    exit()
    
win = tk.Tk()
win.title("EduHub")

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

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')


tabControl.pack(expand=1, fill="both")

 

Teachers_frame = ttk.Labelframe(tab1, text= 'TimeTable')
Teachers_frame.grid(column=0, row=0, padx=8, pady=4)
Teachers_frame.grid_configure(column=0, row=1, padx=8, pady=4)  

Teachers = ttk.LabelFrame(tab1, text='Latest Observation for ')
Teachers.grid(column=0, row=0, padx=8, pady=4)


ttk.Label(Teachers, text="Teacher's Name:  ").grid(column=0, row=0)

Teach =tk.StringVar()
TeachSelected = ttk.Combobox(Teachers, width=24, textvariable=Teach)
TeachSelected['values'] = ('Teacher 1', 'Teacher 2', 'Teacher 3', 'Teacher 4', 'Teacher 5', 'Teacher 6', 'Teacher 7', 'Teacher 8', 'Teacher 9')
TeachSelected.grid(column=1, row=0)
TeachSelected.current(0)

max_width = max([len(x)for x in TeachSelected['values']])
new_width = max_width
new_width = max_width - 4
TeachSelected.config(width=new_width)


ENTRY_WIDTH = max_width + 3
ttk.Label(Teachers_frame, text="8-8:50:").grid(column=0, row=1, sticky='W')
Time1 = tk.StringVar()
Time1Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time1, state='readonly')
Time1Entry.grid(column=1, row=1, sticky='W')


ttk.Label(Teachers_frame, text="8:50-9:40:").grid(column=0, row=2, sticky='W')
Time2 = tk.StringVar()
Time2Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time2, state='readonly')
Time2Entry.grid(column=1, row=2, sticky='W')

ttk.Label(Teachers_frame, text="9:40-10:30:").grid(column=0, row=3, sticky='W')
Time3 = tk.StringVar()
Time3Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time3, state='readonly')
Time3Entry.grid(column=1, row=3, sticky='W')

ttk.Label(Teachers_frame, text="10:30-11:20:").grid(column=0, row=4, sticky='W')
Time4 = tk.StringVar()
Time4Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time4, state='readonly')
Time4Entry.grid(column=1, row=4, sticky='W')

ttk.Label(Teachers_frame, text="11:20-12:10:").grid(column=0, row=5, sticky='W')
Time5 = tk.StringVar()
Time5Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time5, state='readonly')
Time5Entry.grid(column=1, row=5, sticky='W')

ttk.Label(Teachers_frame, text="12:10-1:00:").grid(column=0, row=6, sticky='W')
Time6 = tk.StringVar()
Time6Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time6, state='readonly')
Time6Entry.grid(column=1, row=6, sticky='W')

ttk.Label(Teachers_frame, text="1:00-2:00:").grid(column=0, row=7, sticky='W')
Time7 = tk.StringVar()
Time7Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time7, state='readonly')
Time7Entry.grid(column=1, row=7, sticky='W')

ttk.Label(Teachers_frame, text="2:00-4:00:").grid(column=0, row=8, sticky='W')
Time8 = tk.StringVar()
Time8Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time8, state='readonly')
Time8Entry.grid(column=1, row=8, sticky='W')

ttk.Label(Teachers_frame, text="4:00-5:00:").grid(column=0, row=10, sticky='W')
Time9 = tk.StringVar()
Time9Entry = ttk.Entry(Teachers_frame, width=ENTRY_WIDTH, textvariable=Time9, state='readonly')
Time9Entry.grid(column=1, row=10, sticky='W')

for child in Teachers_frame.winfo_children():
    child.grid_configure(padx=6, pady=6)
    child.grid_configure(padx=4, pady=2)
    

ttk.Label(Teachers, text="Teacher's Name:  ").grid(column=0, row=0)

city =tk.StringVar()
citySelected = ttk.Combobox(Teachers, width=24, textvariable=city)
citySelected['values'] = ('Teacher 1', 'Teacher 2', 'Teacher 3', 'Teacher 4', 'Teacher 5', 'Teacher 6', 'Teacher 7', 'Teacher 8', 'Teacher 9')
citySelected.grid(column=1, row=0)
citySelected.current(0)

Dictionary = {'Teacher 1': {'8:00-8:50': 'Class-A1A', '8:50-9:40': 'Class-A1B', '9:40-10:30': 'Class-A1C',
                      '10:30-11:20': 'Chamber', '11:20-12:10': 'Chamber', '12:10-1:00': 'Class-A1D',
                      '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Chemistry Lab', '4:00-5:00': 'Chamber'},

        'Teacher 2': {'8:00-8:50': 'NA', '8:50-9:40': 'Chamber', '9:40-10:30': 'Class-A1D',
                      '10:30-11:20': 'Class-A1A', '11:20-12:10': 'Class-A1B', '12:10-1:00': 'Class-A1E',
                      '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Chemistry Lab'},

        'Teacher 3': {'8:00-8:50': 'Class-A1B', '8:50-9:40': 'Class-A1C', '9:40-10:30': 'Chamber',
                      '10:30-11:20': 'Chamber', '11:20-12:10': 'Chamber', '12:10-1:00': 'Class-A1A',
                      '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Physics Lab'},

        'Teacher 4': {'8:00-8:50': 'Class-A1C', '8:50-9:40': 'Class-A1D', '9:40-10:30': 'Chamber',
                      '10:30-11:20': 'Chamber', '11:20-12:10': 'Chamber', '12:10-1:00': 'Class-A1B',
                      '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Physics Lab'},

        'Teacher 5': {'8:00-8:50': 'NA', '8:50-9:40': 'Chamber', '9:40-10:30': 'Class-A1E',
                      '10:30-11:20': 'Chamber', '11:20-12:10': 'Class A1A', '12:10-1:00': 'Class-A1C',
                      '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Computer Lab'},

        'Teacher 6': {'8:00-8:50': 'Class-A1D', '8:50-9:40': 'Class-A1A', '9:40-10:30': 'Chamber',
                      '10:30-11:20': 'Class-A1E', '11:20-12:10': 'Chamber', '12:10-1:00': 'NA',
                      '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Computer Lab'},

        'Teacher 7': {'8:00-8:50': 'NA', '8:50-9:40': 'Class-A1E', '9:40-10:30': 'Class-A1A',
                      '10:30-11:20': 'Chamber', '11:20-12:10': 'Chamber', '12:10-1:00': 'Chamber',
                      '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Manufacturing Lab'},

        'Teacher 8': {'8:00-8:50': 'NA', '8:50-9:40': 'Chamber', '9:40-10:30': 'Class-A1B',
                      '10:30-11:20': 'Class-A1D', '11:20-12:10': 'Class-A1E', '12:10-1:00': 'Chamber',
                      '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Manufacturing Lab'},

        'Teacher 9': {'8:00-8:50': 'NA', '8:50-9:40': 'Class-A1A', '9:40-10:30': 'Chamber',
                      '10:30-11:20': 'Class-A1C', '11:20-12:10': 'Class-A1D', '12:10-1:00': 'NA',
                      '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Engineering Graphics Lab'},

        'Teacher 10': {'8:00-8:50': 'Class-A1E', '8:50-9:40': 'Chamber', '9:40-10:30': 'Chamber',
                       '10:30-11:20': 'Class-A1B', '11:20-12:10': 'Class-A1C', '12:10-1:00': 'Chamber',
                       '1:00-2:00': 'Lunch Time', '2:00-4:00': 'Engineering Graphics Lab'}}




Time1.set(Dictionary['Teacher 1']['8:00-8:50'])
Time2.set(Dictionary['Teacher 1']['8:50-9:40'])
Time3.set(Dictionary['Teacher 1']['9:40-10:30'])
Time4.set(Dictionary['Teacher 1']['10:30-11:20'])
Time5.set(Dictionary['Teacher 1']['11:20-12:10'])
Time6.set(Dictionary['Teacher 1']['12:10-1:00'])
Time7.set(Dictionary['Teacher 1']['1:00-2:00'])
Time8.set(Dictionary['Teacher 1']['2:00-4:00'])
Time9.set(Dictionary['Teacher 1']['4:00-5:00'])








win.mainloop()
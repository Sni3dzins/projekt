import pandas 
#izdrukā visus datus
dati = pandas.read_csv('OOP_dati.csv')
print(dati)

#Izdrukā visas klases
list = dati["Klase"].to_list()
print(list)

#Izdrukā vidējo atzimī matemātikā procentos
print(dati['Matemātika'].mean())

#Izdrukā minimālo atzīmi valodā procentos
print(dati['Valoda'].min())

#izdrukā maksimālo atzīmi dabaszinībās procentos
print(dati['Dabaszinības'].max())

# Izdrukā mediānu
print(dati['Valoda'].median())


import tkinter as tk
from tkinter import Canvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

def display_average_grades_window(data_frame):
    """
    Displays a Tkinter window with a bar chart of average grades.

    :param data_frame: Pandas DataFrame with student data.
    """
    # Izrēķina vidējas atzīmes
    subjects = ['Matemātika', 'Valoda', 'Dabaszinības']
    average_grades = data_frame[subjects].mean()

    # Izveido Tkinter logu
    root = tk.Tk()
    root.title('Vidējās atzīmes pēc priekšmetiem')

    #Izveido matplotlib figūru
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Stabiņu diagramma
    ax.bar(subjects, average_grades, color='skyblue')
    ax.set_title('Vidējās atzīmes procentos pēc priekšmetiem')
    ax.set_xlabel('Priekšmets')
    ax.set_ylabel('Vidējā atzīme procentos')

    # Iegūt Matplotlib figūru Tkinter logā
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    root.mainloop()

# Jūsu studentu dati
students_data = {
    'Vārds': ['Anna', 'Jānis', 'Līga','Māris', 'Inese', 'Miks'],
    'Uzvārds': ['Bērziņa', 'Liepiņš', 'Ozoliņa','Sēļenieks', 'Meldere', 'Bērziņa'],
    'Matemātika': [87, 92, 78, 90, 85, 82],
    'Valoda': [95, 88, 85, 75, 94, 82],
    'Dabaszinības': [78, 90, 82, 88, 79, 70],
}

# Izveidojiet Pandas DataFrame no datiem
students_df = pd.DataFrame(students_data)

# Izsauciet funkciju, lai izveidotu Tkinter logu ar bar grafiku
display_average_grades_window(students_df)



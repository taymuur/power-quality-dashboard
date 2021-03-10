import tkinter
from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import ImageTk, Image
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

data = pd.read_excel(r"C:\Users\Taimur Shahzad Gill\Documents\Atom\dashboard-script\Dashboard data.xlsx")   #Change the path value as required

def cancel():
    window.destroy()

def graph1():
    figure1 = plt.Figure(figsize=(5,4), dpi=100)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, window)
    line1.get_tk_widget().place(x=775,y=200)
    
    df1 = DataFrame(data, columns=['Time','Voltage'])
    
    df1 = df1[['Time','Voltage']].groupby('Time').sum()
    df1.plot(kind='line', legend=True, ax=ax1, color='b', marker='o', fontsize=10)
    ax1.set_title('Voltage Vs. Time')

def graph2():
    figure2 = plt.Figure(figsize=(5,4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, window)
    line2.get_tk_widget().place(x=775, y=200)
    
    df2 = DataFrame(data, columns=['Time','Current'])
    
    df2 = df2[['Time','Current']].groupby('Time').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('Current Vs. Time')

def graph3():
    
    # for first bar chart
    figure3 = plt.Figure(figsize=(3,2), dpi=75)
    ax3 = figure3.add_subplot(111)
    bar3 = FigureCanvasTkAgg(figure3, window)
    bar3.get_tk_widget().place(x=100, y=475)
    
    df3 = DataFrame(data, columns=['Voltage','Time'])
    df3 = df3[['Voltage','Time']].groupby('Time').sum()
    df3.plot(kind='bar', legend=True, ax=ax3, color='r', fontsize=10)
    ax3.set_title('Voltage Vs. Time')
    
    # for second bar chart
    figure4 = plt.Figure(figsize=(3,2), dpi=75)
    ax4 = figure4.add_subplot(111)
    bar4 = FigureCanvasTkAgg(figure4, window)
    bar4.get_tk_widget().place(x=320, y=475)
    
    df4 = DataFrame(data, columns=['Current','Time'])
    df4 = df4[['Current','Time']].groupby('Time').sum()
    df4.plot(kind='bar', legend=True, ax=ax4, color='c', fontsize=10)
    ax4.set_title('Current Vs. Time')
    
    # for pie/donut chart
    df5 = DataFrame(data, columns=['Current','Voltage'])
    total = df5.sum(axis=0)
    labels = list(df5.columns)
    sizes = [total[0], total[1]]
    explode = (0, 0.1)  # only "explode" the 2nd slice
    
    figure5 = plt.Figure(figsize=(3,2), dpi=75)
    ax5 = figure5.add_subplot(111)
    ax5.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    pie1 = FigureCanvasTkAgg(figure5, window)
    pie1.get_tk_widget().place(x=540, y=475)
    
    
def systemDashboardGUI():
    global window

    window = Tk()
    window.title("Dashboard")

    #Initialise setup
    
    window.configure(background="#f3f3f4")
    window.minsize(width=1300, height=750)
    
    img1_path = r"C:\Users\Taimur Shahzad Gill\Documents\Atom\dashboard-script\pkflag.png"   #Change the path value as required
    my_image = ImageTk.PhotoImage(Image.open(img1_path)) 
    my_image1 = Label(image=my_image)
    my_image1.place(x=1100, y=40)

    img2_path = r"C:\Users\Taimur Shahzad Gill\Documents\Atom\dashboard-script\pknavylogo.png"   #Change the path value as required 
    my_image12 = ImageTk.PhotoImage(Image.open(img2_path))
    my_image2 = Label(image=my_image12)
    my_image2.place(x=50, y=40)

    
    figure = plt.Figure(figsize=(5,4), dpi=100)
    ax = figure.add_subplot(111)
    line = FigureCanvasTkAgg(figure, window)
    line.get_tk_widget().place(x=775,y=200)
    
    df = DataFrame(data, columns=['Voltage','Current'])
    
    df = df[['Voltage','Current']].groupby('Voltage').sum()
    df.plot(kind='line', legend=True, ax=ax, color='r', marker='o', fontsize=10)
    ax.set_title('Current Vs Voltage')
            
       
    # Components
    
    title = Label(window, text="PKS3 (USER INTERFACE)")
    title.config(font=("Ariel", 35,  "bold"), bg="#f3f3f4", fg="navy blue")

    title.place(x=340, y=40)

    title2 = Label(window, text="SYSTEMS DIVISION")
    title2.config(font=("Ariel", 30, "bold"), bg="#f3f3f4", fg="navy blue")

    title2.place(x=420, y=115)

    Button(window, text="Voltage", width=18, height = 2,bd=0, command=graph1, activebackground="white", fg=("white"),
           bg="navy blue", font=("Ariel", 18)).place(x=150, y=250),

    Button(window, text="Current", width=18 ,height = 2,bd=0, command=graph2, activebackground="white", bg="navy blue",
           fg=("white"), font=("Ariel", 18)).place(x=470, y=250)
    
    Button(window, text="Current & Voltage ", width=18 ,height = 2, bd=0, command=graph3, bg="navy blue", fg=("white"),
           font=("Ariel", 18)).place(x=150, y=370)

    Button(window, text="Exit", width=18 ,height = 2, bd=0, command=cancel, bg="navy blue", fg=("white"),
           font=("Ariel", 18)).place(x=470, y=370)
    

    
    window.mainloop()

systemDashboardGUI()
from tkinter import *
import pyodbc
import matplotlib.pyplot as plt


squarefeet =0
dollars =0

def callingallsnakes():
    functionCobra()
    functionViper()

def functionCobra():
      connection = pyodbc.connect('Trusted_Connection=yes', driver='{SQL Server}',server='RITHVIK-LAPTOP\RITHVIKSSQL', database='Python')
      cursor = connection.cursor();
      cursor.execute("SELECT SquareFeet FROM PyHouse ")
      global squarefeet
      squarefeet = cursor.fetchall()
      connection.close()

def functionViper():
      connection = pyodbc.connect('Trusted_Connection=yes', driver='{SQL Server}',server='RITHVIK-LAPTOP\RITHVIKSSQL', database='Python')
      cursor = connection.cursor();
      cursor.execute("SELECT Dollars FROM PyHouse ")
      global dollars
      dollars = cursor.fetchall()
      connection.close()     
 
def graph():
    global squarefeet
    x = squarefeet
    global dollars
    y = dollars
    plt.scatter(x,y,marker="o")
    plt.show();

def mainframe():
    root = Tk()
    root.geometry("500x500")
    global headinglabel
    headinglabel = Label(root, text="Python", width=25, font=("Courier", 44))
    headinglabel.place(relx=0.5, rely=0.1, anchor='center')
    global textname
    textname = Text(root,height=1,width=25)
    textname.place(relx=0.50, rely=0.25, anchor='center')
    global textage
    textage = Text(root,height=1,width=25)
    textage.place(relx=0.50, rely=0.35, anchor='center')
    buttonidk = Button(root, text="Send to Database", width=25, command=functionAndaconda)
    buttonidk.place(relx=0.50, rely=0.45, anchor='center')
    global commandlabel
    commandlabel = Label(root, text="")
    commandlabel.place(relx=0.50, rely=0.50, anchor='center')
    graph()
    root.mainloop()

def functionAndaconda():
   connection = pyodbc.connect('Trusted_Connection=yes', driver='{SQL Server}',server='RITHVIK-LAPTOP\RITHVIKSSQL', database='Python')
   cursor = connection.cursor() 
   global textname
   global textage   
   SQLCommand = ("INSERT INTO PyHouse " "(squareFeet,dollars ) " "VALUES (?,?)") 
   Values = [int(textname.get("1.0",END)), int(textage.get("1.0",END))] 
   cursor.execute(SQLCommand,Values) 
   global commandlabel
   commandlabel.config(text="Record Saved")
   connection.commit() 
   connection.close()
   callingallsnakes()
   

   
      

mainframe()

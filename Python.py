from tkinter import *
import pyodbc
import matplotlib.pyplot as plt
import numpy as np 

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

def estimateco(x,y):
    n = np.size(x) 
  
    # mean of x and y vector 
    meanx, meany = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    xy = np.sum(y*x - n*meany*meanx) 
    xx = np.sum(x*x - n*meanx*meanx)  
  
    # calculating regression coefficients 
    b_1 = xy / xx 
    b_0 = meany - b_1*meanx 
    return(b_0, b_1) 

def graph(x,y,b):
    plt.scatter(x, y, color = "m",  marker = "o", s = 30)  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
    li = plt.plot(x, y_pred, color = "g") 
    print(li[0].get_data())
    plt.xlabel('Square Feet') 
    plt.ylabel('Dollars') 
    plt.show()
    
def pythongraph():
     callingallsnakes()
     x = np.array(squarefeet)
     y = np.array(dollars)
     b = estimateco(x,y)
     graph(x,y,b)
  
def prediction():
     callingallsnakes()
     x = np.array(squarefeet)
     y = np.array(dollars)
     b = estimateco(x,y)
     global inputsF
     output = int(inputsF.get("1.0",END))
     d = (output*b[1])+b[0]
     global predictlabel
     predictlabel.config(text=d)

def mainframe():
    root = Tk()
    root.geometry("500x500")
    global headinglabel
    headinglabel = Label(root, text="Python", width=25, font=("Courier", 44))
    headinglabel.place(relx=0.5, rely=0.1, anchor='center')
    global textsquarefeet
    textsquarefeet = Text(root,height=1,width=25)
    textsquarefeet.place(relx=0.50, rely=0.25, anchor='center')
    sflabel = Label(root,text="SquareFeet:")
    sflabel.place(relx=0.20, rely=0.25, anchor='center')
    global textdollars
    textdollars = Text(root,height=1,width=25)
    textdollars.place(relx=0.50, rely=0.35, anchor='center')
    dlabel = Label(root,text="Dollars:")
    dlabel.place(relx=0.20, rely=0.35, anchor='center')
    buttonidk = Button(root, text="Send to Database", width=25, command=functionAndaconda)
    buttonidk.place(relx=0.50, rely=0.45, anchor='center')
    global commandlabel
    commandlabel = Label(root, text="")
    commandlabel.place(relx=0.50, rely=0.50, anchor='center')
    global linearreg 
    linearreg = Button(root, text="Linear Regression Graph", width= 25, command=pythongraph)
    linearreg.place(relx=0.50, rely=0.60, anchor='center')
    global inputsF
    inputsF = Text(root,height=1,width=25)
    inputsF.place(relx=0.50, rely=0.75, anchor='center')
    labelpredsF = Label(root,text="SquareFeet")
    labelpredsF.place(relx=0.20, rely=0.75, anchor='center')
    global predictamount 
    predictamount = Button(root, text="Predict", width= 25, command=prediction)
    predictamount.place(relx=0.50, rely=.80, anchor='center')
    global predictlabel
    predictlabel = Label(root, text="")
    predictlabel.place(relx=0.50, rely=0.85, anchor='center')
    root.mainloop()

    

def functionAndaconda():
   connection = pyodbc.connect('Trusted_Connection=yes', driver='{SQL Server}',server='RITHVIK-LAPTOP\RITHVIKSSQL', database='Python')
   cursor = connection.cursor() 
   global textname
   global textage   
   SQLCommand = ("INSERT INTO PyHouse " "(squareFeet,dollars ) " "VALUES (?,?)") 
   Values = [int(textsquarefeet.get("1.0",END)), int(textdollars.get("1.0",END))] 
   cursor.execute(SQLCommand,Values) 
   global commandlabel
   commandlabel.config(text="Record Saved")
   connection.commit() 
   connection.close()  
   
  


mainframe()

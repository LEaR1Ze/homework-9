import mysql.connector
import tkinter as tk
from tkinter import *


  


connection = mysql.connector.connect(host="_______",user="_____",password="_________",database="_____") 


print ("connect successful!!") 
ttr=connection.cursor()
def rrt():
    inf1 = entry.get()
    inf2 = entry2.get()
    inf3 = entry3.get()

    terp = "INSERT INTO users (inf1, inf2, inf3) VALUES (%s,%s,%s)"
    prop = (inf1, inf2, inf3)
    ttr.execute(terp,prop)
    connection.commit()

def output():

    inf4 = entry4.get()

 
    ttr.execute("SELECT concat(inf1,' ',inf2,' ',inf3) as name FROM users where id= %(pr)s", {"pr": inf4} ) 
 
    data = ttr.fetchall()
    
    if data:
        for row in data:
          fild1 = row[0]
        label4["text"]=fild1
        
    else:
        label4.config(text = "Користувача не існує")

    for row in data:
      fild1 = row[0]
    label4["text"]=fild1
     
def input2():
    ttr.execute("SELECT count(*) FROM users")
    data = ttr.fetchall()
    for row in data:
      cn = row[0]-1
        
    ttr.execute("SELECT * FROM users")
    data = ttr.fetchall()

    text_box.delete('1.0', END) 

    while cn >=0:
        text_box.insert(1.0,data[cn])
        text_box.insert(1.0,'\n')
        cn -= 1
    

window = tk.Tk()

label  = tk.Label(text="Поле 1")
label2  = tk.Label(text="Поле 2")
label3  = tk.Label(text="Поле 3")
label4  = tk.Label(text="Поле 4")

entry = tk.Entry()
entry2 = tk.Entry()
entry3 = tk.Entry()
entry4 = tk.Entry()

text_box = tk.Text(
    fg ="black",
    bg ="white"
)

button = tk.Button(
    text="Ввод",
    fg ="black",
    bg ="grey",
    width=20,
    height=2,
    command=rrt
)

button2 = tk.Button(
    text="Вивод",
    fg ="white",
    bg ="red",
    width=20,
    height=2,
    command=output
)

button3 = tk.Button(
    text="Таблиця",
    fg ="white",
    bg ="green",
    width=20,
    height=2,
    command=input2

)

label.pack()
entry.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
label4.pack()
entry4.pack()
text_box.pack()
button.pack()
button2.pack()
button3.pack()

window.mainloop()
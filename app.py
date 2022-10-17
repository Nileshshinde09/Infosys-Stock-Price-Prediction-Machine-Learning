from cProfile import label
from tkinter import *
import numpy as np
import pandas  as pd
import joblib
import tkinter.messagebox as tmsg

root = Tk()

def showresult(value):
    Entry(root,text = "%s" %("Closing Price : {}") ).grid(row=30, column=4)

def printSomething():
    label = Label(root, text= "Hey whatsup bro, i am doing something very interresting.")
    label.pack()   
    label.grid(row=30, column=4)

def predict_price():
    input_data = (float(Openvalue.get()),float(Highvalue.get()),float(Lowvalue.get()),float(Volumevalue.get()))
    print(input_data)
    input_D = np.array(input_data)
    input_re = input_D.reshape(1,-1)
    classifier = joblib.load("model_Infosys.joblib")
    output = classifier.predict(input_re)
    # Entry(root,text = "%s" %(output[0])).grid(row=30, column=4)


root.geometry("400x900")
root.minsize(620,650)
root.maxsize(620,650)
root.configure(background="yellow")


#Heading
Label(root, text="Boston House Priceing", font="comicsansms 30 bold", padx=95,background="yellow").grid(row=0, column=4)
# Open,High,Low,Volume
#Text for our form
Open = Label(root, text="Open",background="yellow",width=12,height=2, font="Arial 20 bold")
High = Label(root, text="High",background="yellow",width=12,height=2, font="Arial 20 bold")
Low = Label(root, text="Low",background="yellow",width=12,height=2, font="Arial 20 bold")
Volume = Label(root, text="Volume",background="yellow",width=12,height=2, font="Arial 20 bold")



#Pack text for our form
Open.grid(row=1, column=4,pady=7)
High.grid(row=3, column=4,pady=7)
Low.grid(row=5, column=4,pady=7)
Volume.grid(row=7, column=4,pady=7)



# Tkinter variable for storing entries
Openvalue = StringVar()
Highvalue = StringVar()
Lowvalue = StringVar()
Volumevalue = StringVar()




#Entries for our form
Openentry = Entry(root, textvariable=Openvalue,width=40)
Highentry = Entry(root, textvariable=Highvalue,width=40)
Lowentry = Entry(root, textvariable=Lowvalue,width=40)
Volumeentry = Entry(root, textvariable=Volumevalue,width=40)



# Packing the Entries
Openentry.grid(row=2, column=4,)
Highentry.grid(row=4, column=4)
Lowentry.grid(row=6, column=4)
Volumeentry.grid(row=8, column=4)


#Checkbox & Packing it
# foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue,background="yellow")
# foodservice.grid(row=27, column=4)

#Button & packing it and assigning it a command
Button(text="ENTER", command=predict_price,bg="orange",height=3,width=8).grid(row=28, column=4,pady=45)



root.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 19:01:16 2019

@author: dedbo
"""


from tkinter import Tk,Frame,Label,Button,LEFT,RIGHT,BOTTOM,TOP,filedialog
from PIL import ImageTk, Image
from animal_predict import animalprediction

root = Tk()
root.title("DESKTOP GUI")
root.geometry("1920x1080+0+0")
path = ''

def home():
    destroy()
    title()
    frame()
    select()

def frame():
    left = Frame(root, width = 600, height = 600, bd = 1 , relief = "raise")
    left.pack(side=LEFT)
    img = Image.open("ars_1.jpg")
    img = ImageTk.PhotoImage(img)
    lbl = Label(left, image = img)
    lbl.image = img 
    lbl.pack()
    
    right = Frame(root, width = 600, height = 600, bd = 1 , relief = "raise")
    right.pack(side=RIGHT)
    img1 = Image.open("ars_2.jpg")
    img1 = ImageTk.PhotoImage(img1)
    lbl1 = Label(right, image = img1)
    lbl1.image = img1 
    lbl1.pack()
    
def title():
    tops = Frame(root, width = 1365, height = 100, bd = 3 , relief = "raise")
    tops.pack()
    
    lbl = Label(tops,
                width=1365,
                text="Welcome \n Animal Recognition System",
                font=('Times 33 bold'),
                fg='Blue')
    lbl.pack()
    
def destroy():
    for window in root.winfo_children():
        window.destroy()

def openfn():
    filename = filedialog.askopenfilename(title='Select Image')
    return filename
    
def resize():
    global path
    path = openfn()
    hsize = 600
    img = Image.open(path)
    wpercent = (hsize / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(wpercent)))
    img = img.resize((wsize, hsize), Image.ANTIALIAS)
    return img

def open_img():
    global button
    img = resize()
    
    destroy()
    title()
    
    btn2 = Button(root,
                  text='Homepage',
                  command=home,
                  font=("Arial Bold",20))
    
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack(side=LEFT)
    
    btn2.pack(side=TOP)
    
    button = Button(root,text='Predict',
                    command=predict,
                    font=("Arial Bold",20))
    button.pack(side=BOTTOM)

def select():
    btn = Button(
            root, text='SELECT\nIMAGE', 
            command=open_img,
            font=("Arial Bold",30))
    btn.pack( anchor='center')

def predict():
    pred = animalprediction(path)
    
    if pred == "Not Found":
        pred = pred
    else:
        pred = 'The animal\nclass name\nis ' + pred
    
    lbl1 = Label(root,text=pred,
                font=("Arial Bold",33),
                fg='BLUE')
    lbl1.pack(anchor='center')
    button.destroy()
    

if __name__ == '__main__':
    home()
    
root.mainloop()

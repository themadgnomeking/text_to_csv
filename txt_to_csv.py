from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from curses import window
import pandas as pd
from os.path import exists
import csv
import pandas

root = Tk()
root.geometry("700x350")

style=ttk.Style(root)

label = Label(root, text = "Click the button to browse the file", font = "Arial 15 bold")
label.pack(pady = 20)



file_path = "D:\Projects\Python\data_conversion\data"

day_of_week = ["Monday",
               "Tuesday",
               "Wednesday",
               "Thursday",
               "Friday",
               "Saturday",
               "Sunday"]
date = []


def open_file():
    #open file from location selected
    file = filedialog.askopenfilename(initialdir=file_path,
                                        title="Select a file", 
                                        filetypes=[("Text files","*.txt"), ("All files", "*.*")])
    ### original open filed
    f = open(file, encoding="utf8") #opens file from location and sets the encoding to prevent corruption
    #txt_file = ((str(f)[-41:-31]).replace("_","/")) #strips the date out of the file string
    txt_file = ((str(f)[-41:-31])) #strips the date out of the file string
    #set_date(txt_file)
    convert_txt_to_csv(f, txt_file)
    print(txt_file)
    f.close()    

'''
def set_date(date):
    date.append(date)
    count = 1
    for d in date:
        pass
'''

def convert_txt_to_csv(file, date_):
    if exists(file_path + "\DSC"+date_+".csv"):
        pass
        fix_file_format(date_)
    else:
        dataframe1 = pd.read_csv(file)
        print(dataframe1)
        dataframe1.to_csv('data\DSC' + str(date_)  + '.csv', index = False)
        fix_file_format(date_)


def fix_file_format(date_):
    data = []
    list_new = []

    with open('data\DSC'+date_+'.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    for d in data:
        new_list = []
        split_first = list(d[0].split(" "))
        count = 0

        for l in split_first:
            new_list.append(l)
            print(count)
            print(l)
        new_list.append(d[1].strip())
        #print(d[1])
        new_list.append(d[2].lstrip())
        
        list_new.append(new_list)
    
    
    #print(list_new)    
    #print(list_new[0])
    #print(data[0][:3][0][6:])
    
 
button = ttk.Button(root, text="Open", command=open_file)
button.pack(pady = 5)

root.mainloop()

#convert_txt_to_csv()

#ask to find file to convert
#take file and sort into a list of lists
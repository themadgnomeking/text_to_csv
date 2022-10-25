from tkinter import *
from tkinter import filedialog
from curses import window
import pandas as pd
from os.path import exists
import csv
import pandas


file_path = "D:\Projects\Python\data_conversion"

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
    file_path = filedialog.askopenfilename(initialdir="D:\Projects\Python\data_conversion",
                                        title="Select a file", 
                                        filetypes=[("Text files","*.txt"), ("All files", "*.*")])
    ### original open filed
    file = open(file_path, encoding="utf8") #opens file from location and sets the encoding to prevent corruption
    txt_file = ((str(file)[-41:-31]).replace("_","/")) #strips the date out of the file string
    #set_date(txt_file)
    convert_txt_to_csv(file)
    print(txt_file)
    file.close()    

'''
def set_date(date):
    date.append(date)
    count = 1
    for d in date:
        pass
'''

def convert_txt_to_csv(file):
    if exists("D:\Projects\Python\data_conversion\DSC.csv"):
        pass
        fix_file_format()
    else:
        dataframe1 = pd.read_csv(file)
        print(dataframe1)
        dataframe1.to_csv('DSC.csv', index = False)
        fix_file_format()


def fix_file_format():
    
    data = []
    list_new = []

    with open('DSC.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    for d in data:
        new_list = []
        split_first = list(d[0].split(" "))
        
        count = 0
        for l in split_first:
            count += 1
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
    

   

    
    

window = Tk()
button = Button(text="Open", command=open_file)
button.pack()
window.mainloop()

#convert_txt_to_csv()

#ask to find file to convert
#take file and sort into a list of lists
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from curses import window
import pandas as pd
from os.path import exists
import csv, os
from datetime import date, timedelta
import datetime

debug_mode = True #turn to false once testing is done

root = Tk()
root.geometry("700x350")

style=ttk.Style(root)

label = Label(root, text = "Click the button to browse the file", font = "Arial 15 bold")
label.pack(pady = 20)



file_path = "D:\Projects\Python\data_conversion\data" #change this to fit your location needs, this is set presently to make it easy on me

day_of_week = ["Monday",
               "Tuesday",
               "Wednesday",
               "Thursday",
               "Friday",
               "Saturday",
               "Sunday"]
date_list = []


def open_file():
    #open file from location selected
    file = filedialog.askopenfilename(initialdir=file_path,
                                        title="Select a file", 
                                        filetypes=[("Text files","*.txt"), ("All files", "*.*")])
    ### original open filed
    f = open(file, encoding="utf8") #opens file from location and sets the encoding to prevent corruption
    txt_file = ((str(f)[-41:-31])) #strips the date out of the file string from the end of the file that spits out as per the open
    #date_strip(text_file)
    set_date(txt_file)
    convert_txt_to_csv(f, txt_file)
    f.close()

def date_strip(text_file):
    txt_file = ((str(text_file)[-41:-31])) #strips the date out of the file string from the end of the file that spits out as per the open   
    return txt_file    


def set_date(date):
    new_date = datetime.datetime.strptime(date, "%m_%d_%Y")
    count = 0
    while count < 7:
        future_date = new_date + timedelta(days = count)
        date_string = datetime.date.strftime(future_date, "%m/%d/%Y")
        date_list.append(str(date_string))
        count += 1
        #print(str(date) + " this is the data coming in")
        #print(date_string + " " + str(count))



#original
def convert_txt_to_csv(file, date_):
    if exists(file_path + "DSC-"+date_+".csv"):
        pass
        fix_file_format(date_)
        # overwrite file with new data
    else:
        dataframe1 = pd.read_csv(file)
        print(dataframe1)
        dataframe1.to_csv('data\DSC-' + str(date_)  + '.csv', index = False)
        fix_file_format(date_)


def fix_file_format(date_):
    data = []
    list_new = []

    #converts the CSV file into a list
    with open('data\DSC-'+date_+'.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    #reads the list and formats further to seperate to first name, last name, day, date, status    
    for d in data:
        new_list = []
        split_first = list(d[0].split(" "))
        second_ = d[1].strip() 
        thrid_ = (d[2].strip()).split(": ")

        #splits the first entry int 3 seperate entrys, first name, last name, day
        for l in split_first: 
            new_list.append(l)
     
        new_list.append(second_) #handles the date and removes the spaces

        for l in thrid_:
            new_list.append(l)#handlees the status and removes the spaces

        list_new.append(new_list)
    
    #take 5 entries and put them in a list
    #append list with missing data (days of week and dates)
    #add OFF as the last item 
        
    #print(count)
    #print(temp_list)
    #print(date_list)
    #print(list_new[:5])

 
button = ttk.Button(root, text="Open", command=open_file)
button.pack(pady = 5)

root.mainloop()

#convert_txt_to_csv()

#ask to find file to convert
#take file and sort into a list of lists
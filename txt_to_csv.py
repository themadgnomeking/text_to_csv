from operator import itemgetter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from curses import window
import pandas as pd
from os.path import exists
import csv, datetime
from datetime import date, timedelta
import numpy as np


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

final_list = []

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

def set_date(date):
    new_date = datetime.datetime.strptime(date, "%m_%d_%Y")
    count = 0
    while count < 7:
        future_date = new_date + timedelta(days = count)
        date_string = datetime.date.strftime(future_date, "%m/%d/%Y")
        date_list.append(str(date_string))
        count += 1

#original
def convert_txt_to_csv(file, date_):
    if exists(file_path + "DSC-"+date_+".csv"):
        pass
        fix_file_format(date_)
        # overwrite file with new data
    else:
        dataframe1 = pd.read_csv(file)
        #print(dataframe1)
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
    add_data_to_list(list_new)


def add_data_to_list(list_input):
    global final_list
    tmp_list = []
    lst_count = 0

    # save entries 5 at a time into a separate list
    for tl in list_input:
        if len(tmp_list) < 5:
            tmp_list.append(tl)
    # compare the 3rd position in each entry to day of week variable - sorts in order
    for count, tl in enumerate(tmp_list):
        if len(tmp_list) < 7:
            # if missing any day add new data in format [first, last, "day of week", "date of day", schedule, "OFF"]
            if day_of_week[count] != tl[2]:
                tmp_list.append([tl[0], tl[1], day_of_week[count], date_list[count], tl[4], "OFF"])
            else:
                pass

    tmp_list.sort(key=itemgetter(3))
    final_list += tmp_list
    #print(final_list)
    tmp_list = []
   #print(final_list)

    #print(tmp_list)
print(final_list)
button = ttk.Button(root, text="Open", command=open_file)
button.pack(pady = 5)

root.mainloop()

#convert_txt_to_csv()

#ask to find file to convert
#take file and sort into a list of lists
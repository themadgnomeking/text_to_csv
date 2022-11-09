from operator import itemgetter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from curses import window
from typing import final
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


def old_add_data_to_list(list_input):
    final_list = []
    tmp_list = []
    lst_count = 0
    while lst_count < len(list_input):
    # save entries 5 at a time into a separate list
        

        """for tl in list_input[(lst_count - 5):lst_count]:
            if len(tmp_list) < 5:
                tmp_list.append(tl)

        # compare the 3rd position in each entry to day of week variable - sorts in order
        print(tmp_list)"""
        '''for count, tl in enumerate(tmp_list):
            #print(len(tmp_list))
            
            if len(tmp_list) < 7:
                if day_of_week[count] != tl[2]:
                    tmp_list += [[tl[0], tl[1], day_of_week[count], date_list[count], tl[4], "OFF"]]
                    """if day_of_week[count] == tmp_list[count-1][2]:
                        #tmp_list += [[tl[0], tl[1], day_of_week[count], date_list[count], tl[4], "OFF"]]
                        print(f"the current count - 1 is: {tmp_list[count - 1]}, the current day_of_week[count] is {day_of_week[count]}")
                        #print([[tl[0], tl[1], day_of_week[count], date_list[count], tl[4], "OFF"]])
                        #print(temp_count)
                        pass
                    else:
                        tmp_list += [[tl[0], tl[1], day_of_week[count], date_list[count], tl[4], "OFF"]]
                        pass
                elif day_of_week[count] == 5:
                    tmp_list += [[tl[0], tl[1], "Saturday", date_list[5], tl[4], "OFF"]]
                    if len(tmp_list) == 7:
                        temp_count = 0
                elif day_of_week[count] == 6:
                    tmp_list += [[tl[0], tl[1], "Sunday", date_list[6], tl[4], "OFF"]]
                    temp_count = 0
                    pass"""
            if len(tmp_list) == 7: # once the list gets to 7 sort and add a space
                tmp_list.sort(key=itemgetter(3))
                tmp_list.append([])
                final_list += tmp_list
                #final_list.append([])'''
        
        
        lst_count += 5
        #print(tmp_list)
        tmp_list.clear()
    #print(final_list[:80])



def add_data_to_list(list_input):
    final_list = []
    name_list_temp = []
    day_of_week_comp = []
    list_count = 0

    while list_count < len(list_input):
        
        for n in list_input[list_count:]:
            if not name_list_temp:
                name_list_temp.append(n)
            if len(name_list_temp) > 0 and n[0] == name_list_temp[0][0]:
                name_list_temp.append(n)
                if n[3].isalpha():
                    day_of_week_comp.append(n[3])
                else:
                    day_of_week_comp.append(n[2])
        #print(f"this is the lenth of the name_list_temp variable: {len(name_list_temp)}")
        temp_var = len(name_list_temp)

        diff = list(set(day_of_week_comp).symmetric_difference(set(day_of_week)))

        for d in diff:
            nl = name_list_temp
            nl.append([nl[0][0], nl[0][1], d, date_list[day_of_week.index(d)], "OFF"])
            #print(nl[0])
            #print(nl)
            #print(d)

        name_list_temp.pop(0)
        name_list_temp.sort(key= itemgetter(3))
        name_list_temp.append([])

        #day_of_week_comp.clear()
        final_list += name_list_temp

        name_list_temp.clear()
        list_count += temp_var

        #print(name_list_temp)
        #print(name_list_temp)
        pass
    print(final_list)
    #print(day_of_week_comp)
    #print(diff)

button = ttk.Button(root, text="Open", command=open_file)
button.pack(pady = 5)

root.mainloop()

#convert_txt_to_csv()

#ask to find file to convert
#take file and sort into a list of lists
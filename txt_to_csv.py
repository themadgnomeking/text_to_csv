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


def add_data_to_list(list):
    
    lst_loc = 0
    tmp_list = []
    #incom_lst = list[lst_loc-5:lst_loc]
    
    for count, tl in enumerate(list):
        
        #print(tl)
        # enumerate through the groups of 5 entries
        # verify all days/dates are in (shoudl be a total lenght of 7
        if count == lst_loc:
            if tl[2] == "Monday":
                tmp_list.append(tl)
            elif tl[2] == "Tuesday":
                tmp_list.append([tl[0], tl[1], "Monday", date_list[0], tl[4], "OFF"])
                tmp_list.append(tl)
            elif tl[2] == "Wednesday":
                tmp_list.append([tl[0], tl[1], "Monday", date_list[0], tl[4], "OFF"])
                tmp_list.append([tl[0], tl[1], "Tuesday", date_list[1], tl[4], "OFF"])
                tmp_list.append(tl)
            print(count == lst_loc)
        if count == lst_loc + 1:
            if tl[2] == "Tuesday":
                tmp_list.append(tl)
            elif tl[2] == "Wednesday":
                tmp_list.append([tl[0], tl[1], "Tuesday", date_list[1], tl[4], "OFF"])
                tmp_list.append(tl)
            elif tl[2] == "Thursday":
                tmp_list.append([tl[0], tl[1], "Tuesday", date_list[1], tl[4], "OFF"])
                tmp_list.append([tl[0], tl[1], "Wednesday", date_list[2], tl[4], "OFF"])
                tmp_list.append(tl)
        if count == lst_loc + 2:
            if tl[2] == "Wednesday":
                tmp_list.append(tl)
            elif tl[2] == "Thursday":
                tmp_list.append([tl[0], tl[1], "Wednesday", date_list[2], tl[4], "OFF"])
                tmp_list.append(tl)
            elif tl[2] == "Friday":
                tmp_list.append([tl[0], tl[1], "Wednesday", date_list[2], tl[4], "OFF"])
                tmp_list.append([tl[0], tl[1], "Thursday", date_list[3], tl[4], "OFF"])
                tmp_list.append(tl)
        #needs to be workd one
        if count == lst_loc + 3:
            if tl[2] == "Thursday":
                tmp_list.append(tl)
            elif tl[2] == "Friday":
                tmp_list.append([tl[0], tl[1], "Thursday", date_list[3], tl[4], "OFF"])
                tmp_list.append(tl)
            elif tl[2] == "Saturday":
                tmp_list.append([tl[0], tl[1], "Thursday", date_list[3], tl[4], "OFF"])
                tmp_list.append([tl[0], tl[1], "Friday", date_list[4], tl[4], "OFF"])
                tmp_list.append(tl)
        #needs to be worked on
        if count == lst_loc + 4:
            if tl[2] == "Friday":
                tmp_list.append(tl)
                tmp_list.append([tl[0], tl[1], "Saturday", date_list[5], tl[4], "OFF"])
                tmp_list.append([tl[0], tl[1], "Sunday", date_list[6], tl[4], "OFF"])
            elif tl[2] == "Saturday":
                tmp_list.append([tl[0], tl[1], "Friday", date_list[4], tl[4], "OFF"])
                tmp_list.append(tl)
            elif tl[2] == "Sunday":
                tmp_list.append([tl[0], tl[1], "Friday", date_list[4], tl[4], "OFF"])
                tmp_list.append([tl[0], tl[1], "Saturday", date_list[5], tl[4], "OFF"])
                tmp_list.append(tl)
            #tmp_list += tl
            
        # Add to a temporary list
        # sort list 
        # add to main list to be converted
        #print(lst_loc)
        #print(tmp_list)
        """
        #print(count)
        if count == 0:
            tmp_list += incom_lst
        #print(count < lst_loc)
        #print(lst_loc < len(list))
        if lst_loc < len(list):
            #add missing information
            #print(len(tmp_list[(lst_loc - 5):]))
            #print(4 < len(tmp_list[(lst_loc - 5):]) < 7)
            if 4 < len(tmp_list[(lst_loc - 5):]) < 7:
                #print(tl[2])
                if tl[2] != "Monday" and count == (lst_loc - 5):
                    tmp_list.append([tl[0], tl[1], "Monday", date_list[0], tl[4], "OFF"])
                    print(1)
                    #print([tl[0], tl[1], day_of_week[0], date_list[0], tl[4], "OFF"])

                if (tl[2] != "Tuesday" and count == (lst_loc - 4)) and (tl[2] != "Tuesday" and count == (lst_loc - 5)):                    
                    tmp_list.append([tl[0], tl[1], "Tuesday", date_list[1], tl[4], "OFF"])
                    print(2)

                print(tl[2] != "Wednesday")
                print(count == (lst_loc - 5))
                if tl[2] != "Wednesday" and count == (lst_loc - 5):
                    tmp_list.append([tl[0], tl[1], "Wednesday", date_list[2], tl[4], "OFF"])
                    print(3)

                if tl[2] != "Thursday" and count == (lst_loc - 4) and tl[2] != "Thursday" and count == (lst_loc - 3) and tl[2] != "Thursday" and count == (lst_loc - 2):
                    tmp_list.append([tl[0], tl[1], "Thursday", date_list[3], tl[4], "OFF"])
                    print(4)

                if (tl[2] != "Friday" and count == (lst_loc - 3)) and (tl[2] != "Friday" and count == (lst_loc - 2)) and (tl[2] != "Friday" and count == (lst_loc - 1)):
                    tmp_list.append([tl[0], tl[1], "Friday", date_list[4], tl[4], "OFF"])
                    print(5)
                if tl[2] != "Saturday" and count == (lst_loc - 2):
                    if count == (lst_loc - 1):
                        tmp_list.append([[tl[0], tl[1], "Saturday", date_list[5], tl[4], "OFF"]])
                        print(6)
                if tl[2] != "Sunday" and count == (lst_loc - 1) :
                    tmp_list.append([tl[0], tl[1], "Sunday", date_list[6], tl[4], "OFF"])
                    print(7)
            print(count)
        else:
            break
        
        lst_loc += 5
        #print(lst_loc)

            
                
            #print(count, tl)"""
    print(tmp_list)
    #print(enumerate(list))

    
    #print(tmp_list)
    #print(len(list))
    #print(tmp_list[(lst_loc-5):])

 
button = ttk.Button(root, text="Open", command=open_file)
button.pack(pady = 5)

root.mainloop()

#convert_txt_to_csv()

#ask to find file to convert
#take file and sort into a list of lists
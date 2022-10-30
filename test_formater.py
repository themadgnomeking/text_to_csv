import pandas as pd
import csv

read_file = pd.read_csv (r'data\data_subset_conversion.txt')
read_file.to_csv (r'data\data_subset_conversion.csv', index=None)

with open("data\data_subset_conversion.csv", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)


day_of_week = ["Monday",
               "Tuesday",
               "Wednesday",
               "Thursday",
               "Friday",
               "Saturday",
               "Sunday"]


#print(data[:5])
#print(len(data))

"""target = len(data)
list_count = 5

end_list = []

for f in range(int(len(data)/5)):
    alter_list = data[list_count-5:list_count]
    temp_list = []
    #print(temp_list)
    print("-----------------------------------")
    for count, l in enumerate(alter_list):
        temp_list.append(l)

        
        
    print(temp_list)
    #print(len(temp_list))
    list_count+=5

    pass"""



"""def add_missing_data(list):
    print(list)
    pass"""


def matchEle():
    A = [5, 4, 9, 12, 23, 31]
    B = [4, 12, 31, 33]
    for i in A:
        for j in B:
            if i == j:
                print(i)

matchEle()
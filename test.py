from operator import itemgetter




day_of_week = ["Monday",
               "Tuesday",
               "Wednesday",
               "Thursday",
               "Friday",
               "Saturday",
               "Sunday"]

date_test = [
    "10/31/2022",
    "11/01/2022",
    "11/02/2022",
    "11/03/2022",
    "11/04/2022",
    "11/05/2022",
    "11/06/2022",
]


testing_data = [["Aaron", "Larsen", "Monday", "10/31/2022", "8 am to 4:30 pm", "On Queue 8 am"],
["Aaron", "Larsen", "Tuesday", "11/01/2022", "8 am to 4:30 pm", "On Queue 8 am"],
["Aaron", "Larsen", "Friday", "11/04/2022", "8 am to 4:30 pm", "On Queue 8 am"],
["Aaron", "Larsen", "Saturday", "11/05/2022", "8 am to 4:30 pm", "On Queue 8 am"],
["Aaron", "Larsen", "Sunday", "11/06/2022", "8 am to 4:30 pm", "On Queue 8 am"],
["Aida", "Martinez", "Tuesday", "11/01/2022", "7 am to 3:30 pm", "PTO 7 am"],
["Aida", "Martinez", "Wednesday", "11/02/2022", "7 am to 3:30 pm", "On Queue"],
["Aida", "Martinez", "Thursday", "11/03/2022", "7 am to 3:30 pm", "On Queue"],
["Aida", "Martinez", "Friday", "11/04/2022", "7 am to 3:30 pm", "On Queue"],
["Aida", "Martinez", "Saturday", "11/05/2022", "7 am to 3:30 pm", "On Queue"],
["Aimee", "Hill", "Monday", "10/31/2022", "10 am to 6:30 pm", "On Queue 10 am"],
["Aimee", "Hill", "Thursday", "11/03/2022", "10 am to 6:30 pm", "On Queue 10 am "],
["Aimee", "Hill", "Friday", "11/04/2022", "10 am to 6:30 pm", "On Queue 10 am"],
["Aimee", "Hill", "Saturday", "11/05/2022", "10 am to 6:30 pm", "On Queue 10 am "],
["Aimee", "Hill", "Sunday", "11/06/2022", "10 am to 6:30 pm", "On Queue 10 am"],
["Aisha", "Reyes", "Monday", "10/31/2022", "11:30 am to 8 pm", "On Queue 11:30 am "],
["Aisha", "Reyes", "Tuesday", "11/01/2022", "11:30 am to 8 pm", "On Queue 11:30 am "],
["Aisha", "Reyes", "Wednesday", "11/02/2022", "11:30 am to 8 pm", "On Queue 11:30 am "],
["Aisha", "Reyes", "Thursday", "11/03/2022", "11:30 am to 8 pm", "On Queue 11:30 am "],
["Aisha", "Reyes", "Saturday", "11/05/2022", "11:30 am to 8 pm", "On Queue 11:30 am "],
["Alina", "Pierce", "Monday", "10/31/2022", "6:30 am to 3 pm", "On Queue 6:30 am"],
["Alina", "Pierce", "Thursday", "11/03/2022", "6:30 am to 3 pm", "On Queue 6:30 am "],
["Alina", "Pierce", "Friday", "11/04/2022", "6:30 am to 3 pm", "On Queue 6:30 am"],
["Alina", "Pierce", "Saturday", "11/05/2022", "6:30 am to 3 pm", "On Queue 6:30 am "],
["Alina", "Pierce", "Sunday", "11/06/2022", "6:30 am to 3 pm", "On Queue 6:30 am"],
["Alister", "Moore", "Monday", "10/31/2022", "9 am to 5:30 pm", "On Queue 9 am "],
["Alister", "Moore", "Tuesday", "11/01/2022", "9 am to 5:30 pm", "On Queue 9 am"],
["Alister", "Moore", "Wednesday", "11/02/2022", "9 am to 5:30 pm", "On Queue 9 am "],
["Alister", "Moore", "Thursday", "11/03/2022", "9 am to 5:30 pm", "On Queue 9 am "],
["Alister", "Moore", "Sunday", "11/06/2022", "9 am to 5:30 pm", "On Queue 9 am"],
["Amber", "Uttecht", "Monday", "10/31/2022", "11:30 am to 8 pm", "PTO 11:30 am"],
["Amber", "Uttecht", "Tuesday", "11/01/2022", "11:30 am to 8 pm", "Chat 11:30 am"],
["Amber", "Uttecht", "Wednesday", "11/02/2022", "11:30 am to 8 pm", "Chat 11:30 am "],
["Amber", "Uttecht", "Thursday", "11/03/2022", "11:30 am to 8 pm", "Chat 11:30 am "],
["Amber", "Uttecht", "Saturday", "11/05/2022", "11:30 am to 8 pm", "Chat 11:30 am "],
["Amber", "Uttecht", "Sunday", "11/06/2022", "11:30 am to 8 pm", "Chat 11:30 am "],
["Andrea", "Soria", "Monday", "10/31/2022", "6:30 am to 3 pm", "Chat 6:30 am"],
["Andrea", "Soria", "Tuesday", "11/01/2022", "6:30 am to 3 pm", "Chat 6:30 am"],
["Andrea", "Soria", "Friday", "11/04/2022", "6:30 am to 3 pm", "Chat 6:30 am"],
["Andrea", "Soria", "Saturday", "11/05/2022", "6:30 am to 3 pm", "Chat 6:30 am"],
["Andrea", "Soria", "Sunday", "11/06/2022", "6:30 am to 3 pm", "Chat 6:30 am"],
["Angie", "Singleton", "Monday", "10/31/2022", "5 am to 1:30 pm", "On Queue 5 am"],
["Angie", "Singleton", "Tuesday", "11/01/2022", "5 am to 1:30 pm", "On Queue 5 am"],
["Angie", "Singleton", "Wednesday", "11/02/2022", "5 am to 1:30 pm", "On Queue 5 am"],
["Angie", "Singleton", "Thursday", "11/03/2022", "5 am to 1:30 pm", "On Queue 5 am"],
["Angie", "Singleton", "Saturday", "11/05/2022", "5 am to 1:30 pm", "PTO 5 am"],
["Ann", "Anschau", "Monday", "10/31/2022", "10 am to 6:30 pm", "On Queue 10 am"],
["Ann", "Anschau", "Wednesday", "11/02/2022", "10 am to 6:30 pm", "On Queue 10 am"],
["Ann", "Anschau", "Thursday", "11/03/2022", "10 am to 6:30 pm", "On Queue 10 am"],
["Ann", "Anschau", "Friday", "11/04/2022", "10 am to 6:30 pm", "On Queue 10 am"],
["Ann", "Anschau", "Saturday", "11/05/2022", "10 am to 6:30 pm", "On Queue 10 am"],]

test_arron = [["Aaron", "Larsen", "Monday", "10/31/2022", "8 am to 4:30 pm", "On Queue 8 am"],
["Aaron", "Larsen", "Tuesday", "11/01/2022", "8 am to 4:30 pm", "On Queue 8 am"],
["Aaron", "Larsen", "Friday", "11/04/2022", "8 am to 4:30 pm", "On Queue 8 am"],
["Aaron", "Larsen", "Saturday", "11/05/2022", "8 am to 4:30 pm", "On Queue 8 am"],
["Aaron", "Larsen", "Sunday", "11/06/2022", "8 am to 4:30 pm", "On Queue 8 am"],]

test_amber = [["Amber", "Uttecht", "Monday", "10/31/2022", "11:30 am to 8 pm", "PTO 11:30 am"],
["Amber", "Uttecht", "Tuesday", "11/01/2022", "11:30 am to 8 pm", "Chat 11:30 am"],
["Amber", "Uttecht", "Wednesday", "11/02/2022", "11:30 am to 8 pm", "Chat 11:30 am "],
["Amber", "Uttecht", "Thursday", "11/03/2022", "11:30 am to 8 pm", "Chat 11:30 am "],
["Amber", "Uttecht", "Saturday", "11/05/2022", "11:30 am to 8 pm", "Chat 11:30 am "],
["Amber", "Uttecht", "Sunday", "11/06/2022", "11:30 am to 8 pm", "Chat 11:30 am "],]
tmp_list = []



#create a second list from main list with same name (no matter how many, min 5, max 7)

day_list_comp = []

for l in test_arron:
    day_list_comp.append(l[2])

diff = list(set(day_list_comp).symmetric_difference(set(day_of_week)))
#print(diff)

name_list_temp = []
day_of_week_comp = []
final_list = []
temp_count = 0


def add_missing_days():

    for n in testing_data:
        if not name_list_temp:
            name_list_temp.append(n)
        if len(name_list_temp) > 0 and n[0] == name_list_temp[0][0]:
            name_list_temp.append(n)
            day_of_week_comp.append(n[2])
    print(f"this is the lenth of the name_list_temp variable: {len(name_list_temp)}")

    diff = list(set(day_of_week_comp).symmetric_difference(set(day_of_week)))

    for d in diff:
        nl = name_list_temp
        nl.append([nl[0][0], nl[0][1], d, date_test[day_of_week.index(d)], "OFF"])

    name_list_temp.pop(0)
    name_list_temp.sort(key= itemgetter(3))
    name_list_temp.append([])

    day_of_week_comp.clear()
    #print(name_list_temp)
    #print(name_list_temp)

add_missing_days()

print(len(testing_data))
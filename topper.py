"""

THIS WAS THE CODE CHALLENGE given

maths_marks = [{user_name: "rishabh", mark: 100}, {user_name: "ankan", mark: 50}, {user_name: "vaibhav", mark: 50}]
english_marks = [{user_name: "rishabh", mark: 60}, {user_name: "ankan", mark: 70}, {user_name: "vaibhav", mark: 80}]
science_marks = [{user_name: "rishabh", mark: 30}, {user_name: "ankan", mark: 90}, {user_name: "vaibhav", mark: 40}]

mark_list = [maths_marks, english_marks, science_marks]

find_topper(mark_list) # should return the topper user_name
The code should add the marks of all subjects(here it is maths,english and science) of every user and it should return the username who is having highest marks. So, here ankan is having highest marks(50+70+90).
NOTE: Code should be such that, even if we have 100 (or) 1000 username with marks, it should return the username who is having highest marks.

"""

# Importing Libraries
from collections import defaultdict

# maths_marks = [
#     {"user_name": "rishabh", "mark": 100},
#     {"user_name": "ankan", "mark": 50},
#     {"user_name": "vaibhav", "mark": 50},
# ]
# english_marks = [
#     {"user_name": "rishabh", "mark": 60},
#     {"user_name": "ankan", "mark": 70},
#     {"user_name": "vaibhav", "mark": 80},
# ]
# science_marks = [
#     {"user_name": "rishabh", "mark": 30},
#     {"user_name": "ankan", "mark": 90},
#     {"user_name": "vaibhav", "mark": 40},
# ]


def find_topper(mark_list):
    """ This function is to derive the topper in the class with provided mark sheets inside a mark_list argument. """
    
    user_name = set()  # empty list for usernames

    data = [
        person_mark for mark in mark_list for person_mark in mark
    ]  # to get all the dictionary data together as lists

    for i in data:
        user_name.add(i["user_name"])  # filling up the user_names list

    induvidual_data = []  # Empty list for Segregated data

    for i in user_name:
        seggregated_data = list(filter(lambda x: x["user_name"] == i, data))
        induvidual_data.append(
            list(map(lambda x: (x["user_name"], x["mark"]), seggregated_data))
        )

    print(f"Induvidual user data after segregation: \n\n{induvidual_data}\n")

    marks_list = defaultdict(
        list
    )  # Empty dictionary with list to store grouped user data

    for i in induvidual_data:
        for user, mark in i:
            marks_list[user].append(
                mark
            )  # This loop is to fill the above empty list with group value as dict

    final_sheet = {
        key: sum(values) for key, values in marks_list.items()
    }  # final_sheet will have summed up values of marks of each user

    print("Summed-up Mark List as below\n")

    for name, marks in final_sheet.items():
        print(f"{name}: {marks}")  # Printing marks of each euser

    print()  # Empty line print

    print(
        f"The Highest Marks in the class is '{max(final_sheet, key=final_sheet.get)}'"
    )  # Final output


# mark_list = [
#     maths_marks,
#     english_marks,
#     science_marks,
# ]  # Multiple Marks sheet has been passed

# find_topper(mark_list)

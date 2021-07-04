<<<<<<< HEAD
import math
print(math.atan2(22, 2))
print(math.copysign(22, 78))
=======
from topper import find_topper
if __name__ == "__main__":

    maths_marks = [
    {"user_name": "rishabh", "mark": 100},
    {"user_name": "ankan", "mark": 50},
    {"user_name": "vaibhav", "mark": 50},
]
    english_marks = [
    {"user_name": "rishabh", "mark": 60},
    {"user_name": "ankan", "mark": 70},
    {"user_name": "vaibhav", "mark": 80},
]
    science_marks = [
    {"user_name": "rishabh", "mark": 30},
    {"user_name": "ankan", "mark": 90},
    {"user_name": "vaibhav", "mark": 40},
]

    mark_list = [
    maths_marks,
    english_marks,
    science_marks,
]  # Multiple Marks sheet has been passed

    find_topper(mark_list)
>>>>>>> origin/main

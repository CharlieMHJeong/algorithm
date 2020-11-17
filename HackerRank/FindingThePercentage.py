"""
The first line contains the integer , the number of students' records.
The next  lines contain the names and marks obtained by a student, each value separated by a space.
The final line contains query_name, the name of a student to query.
Example:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

56.00
"""

def number_of_records():
    # n = int(input("Enter number of Students: "))
    n = int(input(""))
    return n

def put_student_records():
    n = number_of_records()
    record_dict = {}
    for _ in range(n):
        name, *mark_inputs = input().split()
        marks = list(map(float, mark_inputs))
        record_dict[name] = marks
    return record_dict

mark_dict = put_student_records()
studentname = input()

if studentname in mark_dict:
    score_list = mark_dict[studentname]
    ave = sum(score_list)/len(score_list)
    print("{:.2f}".format(ave))

    

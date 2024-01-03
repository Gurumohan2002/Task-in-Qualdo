import operator

data = [{"roll_no": 1, "name": "John", "games": ["cricket", "football"],
        "marks": {"maths": 90, "science": 93, "history": 81}, "rank": 1},
       {"roll_no": 2, "name": "Mick", "games": ["football", "hockey"],
        "marks": {"maths": 95, "science": 86, "cs": 70}, "rank": 2},
       {"roll_no": 3, "name": "June", "games": ["badminton", None],
        "marks": {"maths": 92, "science": 92, "geography": 78}, "rank": 3},
       {"roll_no": 4, "name": "Adam", "games": ["soccer", "badminton"],
        "marks": {"maths": 86, "science": 91, "cs": 82}, "rank": 4},
       {"roll_no": 5, "name": "Robb", "games": ["cricket", None],
        "marks": {"maths": 88, "science": 90, "economics": 84}, "rank": 5},
       {"roll_no": 6, "name": "Arya", "games": ["football", "hockey"],
        "marks": {"maths": 89, "science": 88, "history": 97}, "rank": 6}
       ]
# Get the details of students studied ‘cs’ subject using lambda function

student_cs= list(filter(lambda student : "cs" in student["marks"],data))
for x in student_cs:
    print(x)
print("\n")

rank_values=[]
for student in data:
    rank_values.append(student["rank"])
    
print(rank_values)

# Update the student ranks by calculating the sum of three times the marks in maths, 
# two times the marks in science, and leaving the marks in other subjects as they are. 
# Insert the key percentage, which represents the percentage of sum of marks calculated obtained by each student. 
# Remove null values in the games.

for student in data:
    st_values=list(student["marks"].values())
    # print(st_values)
    total_marks = 3 * student['marks'].get('maths', 0) + 2 * student['marks'].get('science', 0)+st_values[2]
    # print(total_marks)
    student['total_marks'] = total_marks
    
for student in data:
    print(student)
print("\n")

sorted_list = sorted(data, key=operator.itemgetter('total_marks'),reverse=True)
for x in sorted_list:
    print(x)
print("\n")

rank = 1
for student in sorted_list:
    # s=sorted(student, key = lambda x:student["total_marks"], reverse=True)
    student["rank"]=rank
    rank += 1
    
for x in sorted_list:
    print(x)
print("\n")

for student in data:
    student['percentage'] = (student['total_marks']) *100/  600
    student['games'] = [game for game in student['games'] if game is not None]
    


for student in data:
    print(student)

print("\n")

# Create a new dataframe containing the student's name, their percentage, 
# their previous rank, their current rank, along with the change in ranks which is in sorted order by new rank. 
# If the rank has decreased or increased by one, the value should be -1 or 1, respectively. 
# If they are in the same position, the value should be a hyphen.

new_data = []

i=0
for student in data:
    student_dict = {
        'name': student['name'],
        'percentage': student['percentage'],
        'new_rank': student['rank'], 
        'old_rank': rank_values[i] 
    }
    i=i+1
    new_data.append(student_dict)

sorted_one= sorted(new_data, key=lambda x: x['new_rank'])
for student in sorted_one:
    print(student)
    
print("\n")

for i in range(0, len(sorted_one)):
    
    change = sorted_one[i]['old_rank'] - sorted_one[i]['new_rank']
    
    if change >= 1:
        sorted_one[i]['changed_rank'] = change
        
    elif change <= -1:
        sorted_one[i]['changed_rank'] = change
        
    else:
        sorted_one[i]['changed_rank'] = "-"

for student in sorted_one:
    print(student)
    
print("\n")


students_data = {}
working = True
print("Welcome to the grade analyzer, you can input students names and their grades, and when youre done, just write done")
counter = 0
while working:
  name = input("Enter student name (or 'done'): ")
  if '1' in name or '2' in name or '3' in name or '4' in name or '5' in name or '6' in name or '7' in name or '8' in name or '9' in name or '0' in name:
    print("Invalid name, only letters can be accepted")
    continue
  if name.lower() == "done":
    working = False
  else:
    grade_text = input(f"Score for {name}: ")
    if not grade_text.isdigit():
      while not grade_text.isdigit():
        print("Invalid grade, please enter a numeric grade between 0 and 100.")
        grade_text = input(f"Score for {name}: ")
        if grade_text.isdigit():
            break
      print("Invalid grade, please enter a numeric grade between 0 and 100.")
    grade = int(grade_text)
    if grade not in range(0, 101):
      print("Invalid grade, please enter a grade between 0 and 100.")
      continue

    if grade >= 90:
      letter_grade = "A"
    elif grade >= 80:
      letter_grade = "B"
    elif grade >= 70:
      letter_grade = "C"
    elif grade >= 60:
      letter_grade = "D"
    else:
      letter_grade = "F"
    counter += 1
    students_data[counter] = {"name": name, "grade": grade, "letter_grade": letter_grade}
total_sum = 0
grade_list1 = []
if len(students_data) == 0:
  print("No students data entered.")
else:
    for x in range(counter):
      grade_list1.append(students_data[x+1]["grade"])
    average = round(sum((grade_list1)) / len(grade_list1), 2)
    max_grade = max(grade_list1)
    min_grade = min(grade_list1)
    passed = 0
    failed = 0
    for x in students_data:
        if students_data[x]["grade"] >= 60:
            passed += 1
        else:
            failed += 1
    #failed - number of grades below 60
    # passed - number of grades above or equal to 60 
    #gradelist1 - list of all the grades
    #maxgrade and mingrade are obvious
    #ive also got a dictionary #students_data with all the students names, grades and letter grades inside of dictionary-number
    #this dictionary logic i think was hardest for me here to comprehend but i think i handled it pretty well
    print("===== CLASS REPORT ===== \n")
    for x in students_data:
        print(f"{students_data[x]['name']} | {students_data[x]['grade']} | {students_data[x]['letter_grade']}")
    print(f"📈 Class Average :{average}")
    print(f"📉 Highest Grade :{max_grade}")
    print(f"📉 Lowest Grade :{min_grade}")
    print(f"✅ Passed :{passed}")
    print(f"❌ Failed :{failed}")
#i remember that i also need to attach the name of the student with highest grade and lowest 
# but its a little hard for me

# this code gives an output with different amount of spaces between the columns, i want to make it more organized 
# and with the same amount of spaces between the columns,
#asked ai how to do that and its possible but i dont know that method so its just gonna stay like that
#there are 2 methods i didnt know how to work with before, ai in vs code implemented them,i googled and figured out their logic so i think it is valid 
# to add "continue" and "is.digit" to my code
# i actually really enjoyed making all of this

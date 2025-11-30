#name:Rounak Mahato
#date:
#title:grade book analyzer

import csv
print("=== mini grade book analyzer ===")
print("choose input method:")
print("1.Manual Entry")
print("2.Entry through csv")

choice=input("enter choice 1 or 2:")
#dictionary to store student names and garades
grades={}
if choice=="1":
    a=int(input("how many students do you want to enter?"))
    for i in range(a):
        name=input(F"Enter name of student {i+1}:")
        marks=input("Enter marks of student seperated by spaces: ").split()
        marks=[float(m) for m in marks]
        grades[name]= marks

elif choice=="2":
 filename=input("grades.csv:")
with open(grades,'r')as file:
    reader= csv.reader(file)
    for row in reader:
            name = row[0]
            marks = [float(x) for x in row[1:]]
            grades[name] = marks
    else:
      print("Invalid choice.")
    exit()

print("\n=== Grade Report ===")
for student, marks in grades.items():
    total = sum(marks)
    avg = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    print(f"\nStudent: {student}")
    print(f"  Marks: {marks}")
    print(f"  Total: {total}")
    print(f"  Average: {avg:.2f}")
    print(f"  Highest: {highest}")
    print(f"  Lowest: {lowest}")


all_marks = [m for marks in grades.values() for m in marks]
if all_marks:
    print("\n=== Class Summary ===")
    print(f"Class Average: {sum(all_marks)/len(all_marks):.2f}")
    print(f"Highest Mark in Class: {max(all_marks)}")
    print(f"Lowest Mark in Class: {min(all_marks)}")
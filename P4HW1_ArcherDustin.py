#CTI-110
#P4HW1 - Grade List
#Dustin A
#11/1/22

#Ask user for 6 grades for 6 modules
#Add them to a list

grades = []

for grade in range(6):
    grade = int(input("Please Input Grades For Modules:"))
    grades.append(grade)

print("Grades:",grades)

print("The Highest Grade was:", max(grades))

print("The Lowest Grade was:", min(grades))

total = sum(grades)
count = len(grades)

average = total / count

print("Total is:",total)

print("Average is:",average)

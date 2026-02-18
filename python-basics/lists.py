# Name : Kimberley Gitau
# Date : 18/02/2026
# Program to show lists in python

friends = ["Rachel", "Phoebe", "Ross", "Chandler", "Monica", "Joel"]

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)
friends.append("Jack")
print(friends)

new_friends = ["Joel", "Steve", "Gentrix", "Benedict", "Dawn","Leslie", "Egan" ]
print(len(new_friends))

# New list of students
students = friends + new_friends

print(students)
print(len(students))

students.pop()
print(students)

students.insert(5,"Jenny")
print(students)

students.insert(9,"Breana")
print(students)

# extend
students.extend("James")
print(students)

# Remove
students.remove("Benedict")
print(students)

# copy
new_students = students.copy()
print(students)







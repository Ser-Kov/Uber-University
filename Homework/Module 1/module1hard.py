grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
abc_students = sorted(list(students))
list_grades = []
for i in grades:
    middle = sum(i) / len(i)
    list_grades.append(middle)
dict_grades = dict(zip(abc_students, list_grades))
print(dict_grades)

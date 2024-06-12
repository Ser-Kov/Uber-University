# Решил довести программку до ума)) Как если бы журнал заполнял учитель
grades = []
students = []
quantity_students = int(input('Введите количество студентов в классе: '))
count = 0
while count < quantity_students:
    count += 1
    names = str(input('Введите имя учащегося: '))
    marks = int(input('Введите оценки по порядку без пробелов и запятых: '))
    students.append(names)
    list_marks = list(map(int, str(marks)))
    grades.append(list_marks)
    list_grades = []
    for i in grades:
        middle = sum(i) / len(i)
        list_grades.append(middle)
    dict_grades = dict(zip(students, list_grades))
    print(dict_grades)

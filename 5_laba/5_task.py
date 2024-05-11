def update_school(action, **kwargs):
    global school
    if action == "change":
        class_name, new_students = kwargs["class_name"], kwargs["new_students"]
        if class_name in school:
            school[class_name] = new_students
            print(f"Количество учащихся в классе {class_name} изменено на {new_students}.")
        else:
            print("Класс не найден.")
    elif action == "add":
        class_name, students = kwargs["class_name"], kwargs["students"]
        school[class_name] = students
        print(f"в класс {class_name} добавлено {students} учащихся.")
    elif action == "delete":
        class_name = kwargs["class_name"]
        if class_name in school:
            del school[class_name]
            print(f"Класс {class_name} удален.")
        else:
            print("Класс не найден.")
    elif action == "dump":
        total_students = sum(school.values())
        print(f"Общее количество учащихся: {total_students}")
        print("Распределение учеников по классам:")
        for class_name, students in school.items():
            print(f"{class_name}: {students} учеников")

# Инициализация словаря
school = {"1а": 20, "1б": 22, "2б": 25, "6а": 30, "7в": 28}

# Пример использования функции
update_school("change", class_name="1а", new_students=23)
update_school("add", class_name="8а", students=24)
update_school("delete", class_name="1б")
update_school("dump")

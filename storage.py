

#файл для добавления
def save_task(task_description):
    with open('textovick.txt', "w") as file:
        file.write("задача сохранена: " + task_description + "\n")


#файл для чтения
def read_task():
    try:
        with open('textovick.txt', "r") as file:
            task_description = file.read()
            print("Задача:", task_description)
    except FileNotFoundError:
        print("Файл не найден")

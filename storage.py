

#файл для добавления
def save_task(task_description):
    with open('textovick.txt', "a") as file:
        file.write("задача сохранена: " + task_description + "\n")


#файл для чтения
def read_task():
    try:
        with open('textovick.txt', "r") as file:
            lines = file.readlines()
            number = 1

            for line in lines:
                print(f"{number}. {line.strip()}")
                number += 1
    except FileNotFoundError:
        print("Файл не найден")

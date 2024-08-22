
#файл для добавления
def save_task(task_description):
    with open('textovick.txt', "a") as file:
        file.write("задача сохранена: " + task_description + "\n")
    print(f"Задача '{task_description}' успешно добавлена!")


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



def remove_task(number):
    index = number - 1
    with open('textovick.txt', 'r') as file:
        lines = file.readlines()

    if 0 <= index < len(lines):
        lines.pop(index)

        with open('textovick.txt', 'w') as file:
            file.writelines(lines)
        print(f"Задача успешно удалена.")
    else:
        print("Неверный индекс задачи. Убедитесь, что индекс находится в допустимом диапазоне.")
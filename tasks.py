# task_description - строка, содержащая текст задачи
# статус False для невыполненной задачи

def add_task(task_list, task_description):
    task_list.append({"описание": task_description, "статус": False})
    print(f"Задача '{task_description}' успешно добавлена!")

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
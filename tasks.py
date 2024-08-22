# task_description - строка, содержащая текст задачи
# статус False для невыполненной задачи

def add_task(task_list, task_description):
    task_list.append({"описание": task_description, "статус": False})
    print(f"Задача '{task_description}' успешно добавлена!")

def remove_task(task_list, number):
    index = number - 1  # Преобразуем номер задачи в индекс

    if 0 <= index < len(task_list):
        removed_task = task_list.pop(index)
        print(f"Задача '{removed_task}' удалена.")
    else:
        print("Неверный номер задачи. Задача не найдена.")
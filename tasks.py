from todo import task_list # список для хранения задач

# task_description - строка, содержащая текст задачи
# статус False для невыполненной задачи

def add_task(task_description):
    task_list.append({"описание": task_description, "статус": False})
    print(f"Задача '{task_description}' успешно добавлена!")
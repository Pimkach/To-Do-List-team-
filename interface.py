from tasks import add_task
from storage import save_task
from storage import read_task


def interface(task_list):
    print ("Добро пожаловать!")

    vubor = None
    while vubor != '4':
        vubor = input("""Что сегодня будем делать?
        1.Добавить задачу.
        2.Просмотр задачи.
        3.Удаление задачи.
        4.Выход.
        Ввод: """)
        if vubor == "1":
            task_description = input('Введите описание задачи: ')
            add_task(task_list, task_description)
            save_task(task_description)
        if vubor == "2":
            read_task()
        if vubor == "3":
            print('работает')
        if vubor == "4":
            exit()

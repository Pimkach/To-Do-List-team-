from interface import interface
from tasks import add_task, remove_task
from storage import save_task, read_task

task_list = [] # список для хранения задач

def main():
    while True:
        vubor = interface()

        while vubor != 4:
            if vubor == "1":
                task_description = input('Введите описание задачи: ')
                add_task(task_list, task_description)
                save_task(task_description)
                break
            if vubor == "2":
                read_task()
                break
            if vubor == "3":
                print('Какую задачу вы хотите удалить?')
                read_task()
                number = int(input('\nВведите номер задачи, которая должна быть удалена: '))
                remove_task(number)
                break
            if vubor == "4":
                exit()


main()
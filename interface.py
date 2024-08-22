print ("Добро пожаловать!")

vubor = None
while vubor not in ['1', '2','3','4']:
    vubor = input("""Что сегодня будем делать?
    1.Добавить задачу.
    2.Просмотр задачи.
    3.Удаление задачи.
    4.Выход.
    Ввод: """)
    if vubor == "1":
        print("работает")
    if vubor == "2":
        print("работает")
    if vubor == "3":
        print('работает')
    if vubor == "4":
        exit()
input()

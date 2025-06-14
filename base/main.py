import psycopg2
from database_control.worker_control import (add_worker, change_worker,
                                             com_checker, del_worker,
                                             find_worker)

from base import data_user_ask

conn = psycopg2.connect(
    database="all_workers",
    user="postgres",
    password="pass_word",
    host="localhost",
    port="5432",
)

cur = conn.cursor()

while True:
    main_menu = input(
        ""
        "1. НАЙТИ     работника\n"
        "2. ДОБАВИТЬ  нового работника\n"
        "3. ИЗМЕНИТЬ  данные работника\n"
        "4. УДАЛИТЬ   работника\n\n\n"
        "5. ВЫЙТИ\n--->| "
    )

    match main_menu:
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
        case "1":
            ask = input("1. Найти определенного\n2. Показать всех\n--->| ")
            match ask:
                case "1":
                    data = data_user_ask("FIND")
                    data_result = com_checker(
                        cur, "FIND", data[0], data[1], data[2], data[3]
                    )
                    worker = find_worker(cur, conn, data_result[0], data_result[1])
                    input()

                case "2":
                    cur.execute("SELECT * FROM workers")
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
                    input()

                case _:
                    print("ERROR")
        # —————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
        case "2":
            name = input("name: ")
            surname = input("surname: ")
            email = input("email: ")
            add_worker(cur, conn, name, surname, email)
            input()
        # —————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
        case "3":
            worker_id = input("Введите ID:\n--->| ")
            data = data_user_ask("CHANGE")
            data_result = com_checker(
                cur, "CHANGE", name=data[0], surname=data[1], email=data[2]
            )
            change_worker(cur, worker_id, data_result[0], data_result[1])
            input()

        # —————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
        case "4":
            worker_id = input("Введите id\n--->| ")
            del_worker(cur, conn, worker_id)
            input()
        # —————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
        case "5":
            cur.close()
            conn.close()
            break
        # —————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
        case _:
            print("ERROR")
            input()


#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
##################################################################################################################||
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||


def info(row):
    return (
        f"| ID: {row[0]} "
        f"| NAME: {row[1]} "
        f"| SURNAME: {row[2]} "
        f"| EMAIL: {row[3]} "
        f"| DATE: {row[4]}\n"
        f"|{"-" * 100}|")

#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
##################################################################################################################||
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||


def com_checker(cur, mode, id=None, name=None, surname=None, email=None, start_date=None):

    fields = []
    values = []

    if mode == "FIND":
        if id is not None:
            fields.append("id = %s")
            values.append(id)

    if name is not None:
        fields.append("name = %s")
        values.append(name)

    if surname is not None:
        fields.append("surname = %s")
        values.append(surname)

    if email is not None:
        fields.append("email = %s")
        values.append(email)

    if start_date is not None:
        fields.append("start_date = %s")
        values.append(start_date)

    if not fields:
        print("Нет данных")
        return "Нет данных"

    return fields, values


#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
##################################################################################################################||
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||

def add_worker(cur, conn, name: str, surname: str, email: str):

    cur.execute("SELECT * FROM workers WHERE email = %s", (email,))
    row = cur.fetchone()
    if row:
        print("Почта занята")
        return "Почта занята"

    try:
        cur.execute(
            "INSERT INTO workers (name, surname, email) VALUES (%s, %s, %s)",
            (name, surname, email),
        )
        conn.commit()

    except:
        print("ERROR")
        conn.rollback()
        return "ERROR"

    print("Работник успешно добавлен")
    return "Работник успешно добавлен"

#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
##################################################################################################################||
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||


def find_worker(cur, conn, fields: list[str], values: list):
    try:
        sen = f"SELECT * FROM workers WHERE {' AND '.join(fields)}"
        cur.execute(sen, values)
        rows = cur.fetchall()
        if rows:
            print(f"Найдено:\n|{"-" * 100}|")
            for row in rows:
                print(info(row))
            return rows
    except:
        conn.rollback()

    print("Ничего не найдено")
    return False

#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
##################################################################################################################||
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||

def change_worker(cur, id, fields: list[str], values: list):


    cur.execute(
        "SELECT * FROM workers WHERE id = %s", (id, )
    )
    row = cur.fetchone()
#——————————————————————————————————————————————||——||
    if row:
        print(f"Было: {info(row)}")

        values.append(id)
        sen = f"UPDATE workers SET {', '.join(fields)} WHERE id = %s"
        cur.execute(sen, values)
        conn.commit()

        cur.execute(
            "SELECT * FROM workers WHERE id = %s", (id,)
        )
        row = cur.fetchone()
        print(f"Стало: {info(row)}")
        return "Данные изменены"

    print("Никого не найдено по данному id")
    return False

#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
##################################################################################################################||
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||

def del_worker(cur, conn, id):

    cur.execute(
        "SELECT * FROM workers WHERE id = %s", (id,)
    )
    row = cur.fetchone()
    if row:
        print(f"Вы уверены что хотите удалить запись:\n\n{info(row)}")
        ask_sure = input("Напишите YES - чтобы удалить\n\n\n--->| ")

        if ask_sure == "YES":
            try:
                cur.execute(
                    "DELETE FROM workers WHERE id = %s", (id,)
                )
                conn.commit()
                print("Запись удалена")
                return "Запись удалена"
            except:
                print("ERROR")
                conn.rollback()

    print("Запись НЕ удалена")
    return "Запись НЕ удалена"
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||
##################################################################################################################||
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————||




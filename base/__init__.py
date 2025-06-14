
def data_user_ask(mode):
    print("Напишите или оставьте пустым.")
    name = input("name: ")
    if not name:
        name = None

    surname = input("surname: ")
    if not surname:
        surname = None

    email = input("email: ")
    if not email:
        email = None

    if mode == "FIND":
        id = input("ID:")
        if not id:
            id = None
        return id, name, surname, email
    return name, surname, email

def data_for_new_worker():
    name = input("name: ")
    surname = input("surname: ")
    email = input("email: ")
    return name, surname, email
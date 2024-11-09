import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="adminpanel",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()
create_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

create_table2 = '''
    CREATE TABLE IF NOT EXISTS tasks(
        id SERIAL PRIMARY KEY,
        password VARCHAR(100) NOT NULL,
        task VARCHAR(255) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
'''
cursor.execute(create_table2)
connection.commit()

def quest(quest1=None, quest2=None):
    if quest1 == "Ես Ադմիննեմ":
        return True
    elif quest2 == "Ես Աշխատակից եմ":
        return True
    else:
        return False

def admin(admin_username, admin_password):
    if admin_username == "" and admin_password == "":
        return False
    select = '''
        SELECT * FROM users WHERE password = (%s);
    '''
    cursor.execute(select, (admin_password,))
    connection.commit()
    users = cursor.fetchone()
    print(f"Բառի Գալուստ ձեր էջ ադմին՝ {users[1]}")
    return True

def addition(username_input,password_input):
     if username_input == "" and password_input == "":
        return False
     insert = '''
        INSERT INTO users (username, password) VALUES (%s, %s);
     '''
     cursor.execute(insert, (username_input, password_input,))
     connection.commit()
     insert2 = '''
         INSERT INTO tasks (password, task) VALUES (%s, %s);
     '''
     cursor.execute(insert2, (password_input, "Դուք այսօր առաջադրանք դեռ չունեք",))
     connection.commit()
     return True

def tasks(tasks_input, password1_input):
    if tasks_input == "" and password1_input == "":
        return False
    update = '''
        UPDATE tasks SET task = (%s) WHERE password = (%s);
    '''
    cursor.execute(update, (tasks_input, password1_input,))
    connection.commit()
    return True

def delete_account(password_input, password4_input):
    delete = '''
        DELETE FROM users WHERE password = (%s);
    '''
    cursor.execute(delete, (password_input,))
    connection.commit()
    delete2 = '''
        DELETE FROM tasks WHERE password = (%s);
    '''
    cursor.execute(delete2, (password4_input,))
    connection.commit()
    return True

def sign_in(password_input):
    if password_input == "":
        return False
    select = '''
        SELECT * FROM users WHERE password = (%s);
    '''
    cursor.execute(select, (password_input,))
    connection.commit()
    users = cursor.fetchone()
    print(users[1])
    return True

def see_tasks(password_input3):
    if password_input3 == "":
        return False
    select = '''
        SELECT * FROM tasks WHERE password = (%s);
    '''
    cursor.execute(select, (password_input3,))
    connection.commit()
    task = cursor.fetchone()
    print(task[2])
    return True

while True:
    print("Ես Ադմիննեմ")
    print("Ես Աշխատակից եմ")
    quest_input = input("Նշեք թե որնեք դուք:  ")
    if quest(quest1=quest_input):
        Username = input("Գրեք ադմինի անունը։  ")
        password2 = input("Գրեք ադմինի գաղտնաբառը։  ")
        if admin(admin_username=Username, admin_password=password2):
            while True:
                print("-" * 25)
                print("Ավելացնել Աշղատակից։ A")
                print("Փոփողել առաջադրանքները։  T")
                print("Հեռացնել աշխատակցին։  D")
                print("-" * 25)
                while True:
                    command = input("Ընտրեք Կամանդը։  ")
                    if command == "A":
                        add = input("Գրեք Աշխատակցի անունը։  ")
                        add2 = input("Գրեք Աշղատակցի գաղտնաբառը։  ")
                        if addition(username_input=add, password_input=add2):
                            print("Տվյալները հաջողությամբ գրանցվեցին")
                        else:
                            print("-" * 25)
                            print("Գործողությունները դատարկ են!!")
                            print("-" * 25)
                    elif command == "T":
                        tasks_input2 = input("Գրեք Առաջադրանքը։  ")
                        password_input3 = input("Գրեք գաղտնաբառը ն թե ումնեք ուզում փոխել")
                        if tasks(tasks_input=tasks_input2, password1_input=password_input3):
                            print("Առաջադրանքները հաջողությամբ ուղարկվեցին")
                        else:
                            print("Գործողությունները դատարկ են !!")
                    elif command == "D":
                        password_inp = input("Գրեք աշխատակցու գաղտնաբառը")
                        password_inp2 = input("Նույնականացրեք աշխատակցու գաղտնաբառը")
                        if delete_account(password_input=password_inp, password4_input=password_inp2):
                            print("Տվյալները Հաջողությամբ ջնջվեցին")
                        else:
                            print("-" * 25)
                            print("Գործողությունները դատարկ են !!")
                            print("-" * 25)
                    else:
                        print("-" * 25)
                        print("Այդպիսի կոմանդ չկա !!")
                        print("-" * 25)

        else:
            print("-" * 25)
            print("Այդպիսի ադմին չկա!!")
            print("-" * 25)
    elif quest(quest2=quest_input):
        password_input5 = input("Գրեք գաղտնաբառը")
        if sign_in(password_input=password_input5):
            print("-" * 25)
            print("Նայել առաջադրանքները։ S")
            print("-" * 25)
            while True:
                command = input("Ընտրեք կամանդը")
                if command == "S":
                    password_input3 = input("Գրեք գաղտնաբառը")
                    if see_tasks(password_input3=password_input3):
                        print("Գործողությունը կատարված է")
                    else:
                        print("-" * 25)
                        print("Սխալ է նորից փորձեք")
                        print("-" * 25)
                else:
                    print("Այդպիսի կամանդ չկա !!")
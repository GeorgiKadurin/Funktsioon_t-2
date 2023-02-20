from OmaModul import *


Login=["User1", "User2"]
password_=["s1mple", "juppi"]
while True:
    print(Login)
    print(password_)
    a=str(input("Вы хотите войти в систему? ")) #yas/no
    if a=="yas":
        print("Авторизуйтесь")
        print("Укажите свой логин и пароль")
        logi=input("Логин: ")
        pass_=input("Пароль: ")
        if logi in Login and pass_ in password_:
            print("Вы успешно Авторизовались ")

        else:
            print("Не верный логин или пароль")
            d=str(input("Вы хотите восстановить пароль? "))
            if  d=="yas":
                print("Восстановление пароля")
                Logit = input("Введите имя пользователя: ")
                pas_o = input("Введите старый пароль: ")
                pas_n = input("Введите новый пароль: ")
                repass(Login, password_, Logit, pas_o, pas_n)
                
                
            else:
                 d=="no"
                 print()
                 f=str(input("Вы хотите восстановить забытый пароль? "))
                 if f=="yas":
                    Logit= input("Введите имя пользователя: ")
                    reepasss(password_, Logit, Login)
                      

    elif a=="no":
         b=str(input("Вы хотите регнутся? "))
         b=="yas"
         print("Регистрация")
         Login,password_=reg(Login,password_)
    else:
         b=="no"
         c=str(input("Закончить работу? ")) #ainult yas
         if c=="yas":
            print("Конец") 
            break

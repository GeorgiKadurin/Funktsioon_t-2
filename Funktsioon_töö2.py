from OmaModul import *


logt=["User1", "User2"]
pasw=["s1mple", "juppi"]
while True:
    print(logt)
    print(pasw)
    a=str(input("Вы хотите войти в систему? ")) #yas/no
    if a=="yas":
        print("Авторизуйтесь")
        print("Укажите свой логин и пароль")
        logi=input("Логин: ")
        pass_=input("Пароль: ")
        if logi in logt and pass_ in pasw:
            print("Вы успешно Авторизовались ")

        else:
            print("Не верный логин или пароль")
            d=str(input("Вы хотите восстановить пароль? "))
            if  d=="yas":
                username = input("Введите имя пользователя: ")
                old_password = input("Введите старый пароль: ")
                new_password = input("Введите новый пароль: ")
                reset_password(logt, pasw, username, old_password, new_password)
                
            else:
                 d=="no"
                 print()
                 f=str(input("Вы хотите восстановить забытй пароль? "))
                 if f=="yas":
                      username = input("Введите имя пользователя: ")
                      j=сброс_пароля

    elif a=="no":
         b=str(input("Вы хотите регнутся? "))
         b=="yas"
         print("Регистрация")
         logt,pasw=reg(logt,pasw)
    else:
         b=="no"
         c=str(input("Закончить работу? ")) #ainult yas
         if c=="yas":
            print("Конец") 
            break



  

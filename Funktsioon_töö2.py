from OmaModul import *


logt=["User1", "User2"]
pas=["s1mple", "juppi"]
while True:
    print(logt)
    print(pas)
    a=str(input("Вы хотите войти в систему? ")) #yas/no
    if a=="yas":
        print("Авторизуйтесь")
        print("Укажите свой логин и пароль")
        logi=input("Логин: ")
        pass_=input("Пароль: ")
        if logi in logt and pass_ in pas:
            print("Вы успешно Авторизовались ")

        elif print("Не верный логин или пароль"):
            print("")


    elif a=="no":
         b=str(input("Вы хотите регнутся? "))
         b=="yas"
         print("Регистрация")
         logt,pas=reg(logt,pas)
    else:
         b=="no"
         c=str(input("Закончить работу? ")) #ainult yas
         if c=="yas":
            print("Конец") 
            break
       



  

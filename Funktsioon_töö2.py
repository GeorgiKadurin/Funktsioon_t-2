from math import*
from random import*
from OmaModul import *

logt=["User1", "User2"]
pas=["s1mple", "juppi"]
while True:
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


    else: 
        a=="no"
        b=str(input("Вы хотите регнутся? "))
        if b=="yas":
            print("Регистрация")
            b1=str(input("Автоматическое создание пароля: "))
            b1=="yas"
            spin=salasõna
            print("Пароль:", spin)

            #b1=="no"
            #if b2=str(input("Cамостоятельное создание пароля")):
            #print()
        else:
            b=="no"
            c=str(input("Закончить работу? ")) #ainult yas
            if c=="yas":
                print("Конец") 
                break




  

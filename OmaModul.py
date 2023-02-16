from random import *
#def salasõna(k:int)->bool:
#    """
#    Määrme salasõna..
#    :parem int sala:Järjend salasõna numbridest
#    :rtype: bool
#    """
#    k='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;!_*-+()/#¤%&'
#    salasõna=''.join(random.choice(k) for x in range(12)) #Выбирает 12 рандомных символов.
#    return salasõna



import string
def Salasona(k: int)->bool:
    """
    Määrme salasõna..
    :parem int k:Järjend salasõna numbridest
    :rtype: bool
    """
    saladus=""
    for i in range(k):
        t=choice(string.ascii_letters) #Aa...Zz
        num=choice([1,2,3,4,5,6,7,8,9,0])
        sym=choice(["*","-",".","!","_"])
        t_num=[t,str(num),sym]
        saladus+=choice(t_num)
    return saladus

def reg(logt:list, pas:str)->bool:
    """
    Määrme reg..
    :parem logt list, pas str:Järjend salasõna numbridest
    :rtype: bool
    """
    n=input("Напишите свое имя: ")
    tehe=int(input("2-Задать свой пароль, 1-сгенерировать его случайным образом\n "))

    if tehe==1:
        salasona=Salasona(12)
        logt.append(n)
        pas.append(salasona)
 

    elif tehe==2:
       pas=input("Напишите свой пароль: ")
       if any(c.islower() for c in pas) and any(c.isupper() for c in pas) and any(c.isdigit() for c in pas) and any(c in '.,:;!_*-+()/#¤%&' for c in pas):
            print("Вы создали пароль")
            logt.append(n)
            pas.append(str(salasona))
       else:
            print("Ошибка")
        
       
    return logt,pas





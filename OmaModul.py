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




def repass(Login:str, password_:str, Logit:str,  pas_o:str, pas_n:str)->bool:
    """
    Määrme repass Muutuja, mille juurde sisestate esmalt vana parooli ja seejärel uue ning idee kohaselt tuleks asendada.
    :parem Login str, password_ str, Logit str,  pas_o str, pas_n str:Järjend repass 
    :rtype: str
    """
    if  Logit in Login and  pas_o in password_:
        index = Login.index( Logit)
        password_[index] = pas_n
        print(f"Пароль изменен")

     
   


def reuser(log_o:str, log_n:str, Login:str)->str:
   """
    Määrme repass(Переменная при который вы вписываете сначала старого юзера, а потом нового)
    :parem log_o str, log_n str, Login str:Järjend repass 
    :rtype: str
   """
  

   if log_o in Login:
        index = Login.index(log_o)
        Login[index] = log_n
        print("Имя юзера было изменено.")








    #
def reepasss(password_:int, logit:str, Login:str)->bool:
    """
    Määrme reepasss (Переменная меняющая пароль на новый)
    :parem ppassw:int, user:int,logt:int:Järjend reepasss
    :rtype: bool
    """
    if logit in Login:
        index = Login.index(logit)
        pas_n = Salasona()
        password_[index] = pas_n
        print(f"Новый пароль {Login}: {pas_n}")
       

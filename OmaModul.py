from random import*
import random

def salasõna()->any:
    """
    Määrme salasõna muutuja loomiseks parool 12 sümbolist
    :parem int sala:Järjend salasõna numbridest
    :rtype: bool
    """
    k='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;!_*-+()/#¤%&'
    salasõna=''.join(random.choice(k) for _ in range(12))
    return salasõna




import string
def Salasona(k:int)->bool:
    """
    Määrme salasõna muutuja loomiseks parool 12 sümbolist
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
    Määrme reg muutuja parooli kontrollimiseks
    :parem logt list, pas str:Järjend salasõna numbridest
    :rtype: bool
    """
    n=input("Kirjutage oma nimi: ")
    tehe=int(input("2-Määrake oma parool, 1-genereerige see juhuslikult\n "))

    if tehe==1:
        salasona=Salasona(12)
        logt.append(n)
        pas.append(salasona)
 

    elif tehe==2:
       pas=input("Kirjutage oma parool: ")
       if any(c.islower() for c in pas) and any(c.isupper() for c in pas) and any(c.isdigit() for c in pas) and any(c in '.,:;!_*-+()/#¤%&' for c in pas):
            print("Olete loonud parooli")
            logt.append(n)
            pas.append(str(salasona))
       else:
            print("Viga")
        
       
    return logt,pas




def repass(Login:str, password_:str, Logit:str,  pas_o:str, pas_n:str)->str:
    """
    Määrme repass muutuja, mille juurde sisestate esmalt vana parooli ja seejärel uue ning idee kohaselt tuleks asendada.
    :parem Login str, password_ str, Logit str,  pas_o str, pas_n str:Järjend repass 
    :rtype: str
    """
    if  Logit in Login and  pas_o in password_:
        l = Login.index( Logit)
        password_[l] = pas_n
        print("Parool muudetud")

     
   

def reuser(log_o:str, log_n:str, Login:str)->str:
    """
#    Määrme repass muutuja, kuhu sisestate kõigepealt vana kasutaja ja seejärel uue
#    :parem log_o str, log_n str, Login str:Järjend repass 
#    :rtype: str
#   """
    if  log_o in Login:
        y = Login.index(log_o)
        Login[y] = log_n
        print("Kasutajanimi on edukalt muudetud.")
  


def reepasss(password_:int, logit:str, Login:str)->bool:
    """
    Määrme reepasss muutuv parooli muutmine uueks
    :parem ppassw:int, user:int,logt:int:Järjend reepasss
    :rtype: bool
    """
    if logit in Login: 
        x = Login.index(logit)     
        pas_n = salasõna()
        password_[x] = pas_n
        print(f"Kasutaja parool {logit} on muudetud järgmiselt: {pas_n}")

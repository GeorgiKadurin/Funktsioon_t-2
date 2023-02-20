from OmaModul import *


Login=["User1", "User2"]
password_=["s1mple", "juppi"]
while True:
    print(Login)
    print(password_)
    a=str(input("Kas soovite süsteemi sisse logida? ")) #yas/no
    if a=="yas":
        print("Autoriseerima")
        print("Määrake oma kasutajanimi ja parool")
        logi=input("Login: ")
        pass_=input("Parool: ")
        if logi in Login and pass_ in password_:
            print("Olete Sisse Loginud ")

        else:
            print("Vale sisselogimine või parool")
            d=str(input("Kas soovite parooli taastada? "))
            if  d=="yas":
                print("Parooli taastamine")
                Logit = input("Sisestage Kasutaja nimi: ")
                pas_o = input("Sisestage vana parool: ")
                pas_n = input("Sisestage uus parool: ")
                repass(Login, password_, Logit, pas_o, pas_n)
                print()
            else: 
                d=="no"
                k=str(input("Kas soovite taastada sisselogimise? "))
                if k=="yas":
                   log_o = input("Sisestage praegune kasutajanimi: ")
                   log_n = input("Sisestage uus kasutajanimi: ")
                   reuser(Login, log_o, log_n)

                
                else:
                    k=="no"
                    print()
                    f=str(input("Kas soovite unustatud parooli taastada? "))
                    if f=="yas":
                        logit= input("Sisestage oma kasutajanimi: ")
                        reepasss(password_, logit, Login)
                      

    elif a=="no":
         b=str(input("Kas soovite registreeruda? "))
         b=="yas"
         print("Registreerimine")
         Login,password_=reg(Login,password_)

    else:
         f=="no"
         b=="no"
         c=str(input("Töö lõpetada? ")) #ainult yas
         if c=="yas":
            print("Lõpuks") 
            break

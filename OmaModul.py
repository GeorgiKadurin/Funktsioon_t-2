from random import*

def salasõna(sala:int)->any:
    """
    Määrme salasõna..
    :parem int sala:Järjend salasõna numbridest
    :rtype: any
    """
    süm=".,:;!_*-+()/#¤%&0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    sala=''.join(random.choice(süm) for _ in range(12))

    return sala
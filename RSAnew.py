import random
import tkinter

def RSA(msg):
    
    def GCD(x,y):
        if(y == 0):
            return x
        else:
            return GCD(y, x % y)
    def invMod(e,eular):
        for i in range(eular):
            if (e*i)%eular==1:
                return i
        return None
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    def generate_prime():
        while True:
            p = random.randint(2, 80)
            if is_prime(p):
                return p
    
    p = generate_prime()
    print("p is " , p)
    q = generate_prime()
    print("q is " , q)
    # ct=0
    
    # for i in range(2, 200):
    #     z=random.randrange(2,200)
    #     for x in range(2, z):
    #         if (z%x==0):
    #             break
    #     else:
    #         if(ct==1 and z!=p):
    #             print(z)
    #             q=z
    #             break  
    #         if(ct==0):
    #             print(z)
    #             p=z
    #             ct+=1
            

    #p=47
    #q=17
    n=p*q
    eular = (p-1)*(q-1)
    print("eular is",eular)
    e=random.randrange(1,eular)

    # while(e<eular):
    #     if(GCD(e,eular)!=1):
    #         e = e+1
    #     else:
    #         d=invMod(e,eular)
    #         if(d!=None):
    #             break
    #         else:
    #             e = e+1
    while True:
        e = random.randrange(1, eular)
        if GCD(e, eular) == 1:
            d = invMod(e, eular)
            if d is not None:
                break

    print("e is",e)
    #e=5
    #d=invMod(e,eular)
    print("d is",d)
    def cipher(msg):
        C = [(ord(M) ** e) % n for M in msg]
        return C
    def decipher(cipher):
        #M = [chr((C ** d) % n) for C in cipher]
        M = [chr((cipher[i] ** d) % n) for i in range(len(cipher))]
        return ''.join(M)

    #msg="The name's Bond"
    print("Original msg:"+ msg)
    cipher = cipher(msg)
    print("Ciphered:", cipher)
    top = tkinter.Tk()
    top.geometry("350x450")
    top.configure(bg='black')
    lbl = tkinter.Label(top, text  = "Ciphered text is "+' '.join(str(i) for i in cipher),fg='white',bg='black')
    lbl.pack()
    
    deciphered = decipher(cipher)
    lbl2 = tkinter.Label(top, text = "Deciphered text is " + deciphered,fg='white',bg='black')
    lbl2.pack()

    print("Deciphered:", deciphered)

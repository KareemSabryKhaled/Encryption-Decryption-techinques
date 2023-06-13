import random
import tkinter



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

ct=0
for i in range(100, 200):
    z=random.randrange(100,200)
    for x in range(2, z):
        if (z%x==0):
            break
    else:
        if(ct==1 and z!=p):
            print(z)
            q=z
            break  
        if(ct==0):
            print(z)
            p=z
            ct+=1
        



def cipherRSA(msg):
    n = p * q
    eular = (p - 1) * (q - 1)
    print("eular is", eular)
    e = random.randrange(1, eular)

    while (e < eular):
        if (GCD(e, eular) != 1):
            e = e + 1
        else:
            break

    print("e is", e)
    d = invMod(e, eular)
    print("d is", d)
    C = [(ord(M) ** e) % n for M in msg]

    biglist = []
    biglist.append(C)
    biglist.append(d)
    biglist.append(n)
    lst_str = [str(x) for x in biglist]
    result = '-'.join(lst_str)

    return result
def decipherRSA(cipher):
    string_list = cipher.split('-')
    output_list = [int(x) if x.isdigit() else x for x in string_list]
    string_list = output_list[0]
    int_list = eval(string_list)
    ciphered = int_list
    d = output_list[1]
    n = output_list[2]
    M = [chr((C ** d) % n) for C in ciphered]
    return ''.join(M)
#cipher(msg)
# print("Original msg:"+ msg)
# cipher = cipher(msg)
# print("Ciphered:", cipher)
# c='-'.join(str(e) for e in cipher)
# return c

#deciphered = decipher(cipher)
#print("Deciphered:", deciphered)

#client(str(cipher))
# top = tkinter.Tk()
# top.geometry("350x450")
# top.configure(bg='black')
# lbl = tkinter.Label(top, text  = "Ciphered text is "+' '.join(str(i) for i in cipher),fg='white',bg='black')
# lbl.pack()
#
#
# lbl2 = tkinter.Label(top, text = "Deciphered text is " + deciphered,fg='white',bg='black')
# lbl2.pack()

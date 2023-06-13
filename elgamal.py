import random
from math import pow
a=random.randint(2,10)
#list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def prime_gen():

    while True:
        #q = random.randint(pow(10,20),pow(10,50))
        #q = random.choice(list_of_primes)
        q = random.randint(2, 1000)
        if is_prime(q):
            return q

#To fing gcd of two numbers
def greatest_comm_divisor(a,b):
    if a<b:
        return greatest_comm_divisor(b,a)
    elif a%b==0:
        return b
    else:
        return greatest_comm_divisor(b,a%b)

#For key generation i.e. large random number
def generate_key(q):
    #key= random.randint(pow(10,20),q)
    key = random.randint(2, q)
    while greatest_comm_divisor(q,key)!=1:
        #key=random.randint(pow(10,20),q)
        key = random.randint(2, q)
    return key

def prime_check(n):
    flag = False

    if a == 1:
        #print(num, "is not a prime number")
        return False
    elif a > 1:
        # check for factors
        for i in range(2, a):
            if (a % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            #print(num, "is not a prime number")
            return False
        else:
            #print(num, "is a prime number")
            return True

def is_prime(number):
    """
    Returns True if the number is prime, else False.
    """

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c;
        y=(y*y)%c
        b=int(b/2)
    return x%c

#For asymetric encryption
def encryption_elgamal(msg):
    #msg,q,h,g
    key, q, h, g = starter()
    ct=[]
    k=generate_key(q)
    s=power(h,k,q)
    p=power(g,k,q)
    for i in range(0,len(msg)):
        ct.append(msg[i])
    #print("g^k used= ",p)
    #print("g^ak used= ",s)
    for i in range(0,len(ct)):
        ct[i]=s*ord(ct[i])
    biglist = []
    biglist.append(ct)
    biglist.append(p)
    biglist.append(key)
    biglist.append(q)
    lst_str = [str(x) for x in biglist]
    result = '-'.join(lst_str)

    return result

#For decryption
def decryption_elgamal(string_list):
    string_list = string_list.split('-')
    output_list = [int(x) if x.isdigit() else x for x in string_list]
    string_list = output_list[0]
    int_list = eval(string_list)
    ct = int_list
    p = output_list[1]
    key = output_list[2]
    q = output_list[3]
    pt=[]
    h=power(p,key,q)
    for i in range(0,len(ct)):
        pt.append(chr(int(ct[i]/h)))
    d_msg=''.join(pt)
    return d_msg

def starter():

    q= prime_gen()
    g=random.randint(2,q)
    key=generate_key(q)
    h=power(g,key,q)
    #ct, p = encryption(msg, q, h, g)
    #cncryptedemsglast = str(ct) + '-' + str(q)
    #client(cncryptedemsglast)
    return key, q, h, g
#msg = input("trial: ")
#print("g used=",g)
#print("g^a used=",h)
#key,q,h,g = starter()
#combined=encryption(msg)


#
# string_list = combined.split('-')
# output_list = [int(x) if x.isdigit() else x for x in string_list]
# string_list = output_list[0]
# int_list = eval(string_list)




#print("Original Message=",msg)

#
# print("Encrypted Maessage=",ct)
#pt=decryption(combined)
#d_msg=''.join(pt)
#print("Decryted Message=",d_msg)
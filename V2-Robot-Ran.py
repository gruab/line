# v2 robot 



import string
import time as  time



name = ["rocky" , "monkey"]

print("Checking in today?")  
time.sleep(.9)

nameOftheuser = str(input("Starting off,  with your name? \n")).upper()
#print(type(nameOftheuser))



listOfmenu = "Chicken wing , black coffe , rice blow \n nae , momo , smoothie"
#drink = "coco , sprit , cold water and warm water \n ice coffe , cold coffe, and normal coffe"


#if those name come in then do this
if nameOftheuser == "PRASANT" or nameOftheuser == "AARYAN" or nameOftheuser == "K" or nameOftheuser == "":
    time.sleep(.5)
    print("..")
    time.sleep(.5)
    bad = input("uhm , are you happenes to be bad huh? ")
    if bad  == "yes":
        time.sleep(.5)
        print("Oh... \n...")
        time.sleep(1)
        print("okie")
        time.sleep(.9)
        money = int(input("So , how much money you got today? \n: "))
        if bad == "yes" and money > 5:
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("uhm, i guess you can come in today \n ")
        else:
            print("not day then")
            exit()
    
print("..") 
time.sleep(1)
print("..") 
time.sleep(1)
print("Okay" , nameOftheuser , "This is our menu:\n")
time.sleep(.8)
print(listOfmenu)
time.sleep(1)
oder  = input("So what would you like form my meun  " + nameOftheuser + "\n: ")

#price of the foodey#
if oder == "Chicken wing":
    price = 4
    

elif oder == "black coffe":
    price = 2
     
elif oder == "smoothie":
    price = 6
     

elif oder == "momo":
    price = 2
     

elif oder == "rice blow":
    chciken = input("Do you want chicken too?")
    if chciken == "yes":
        price = 6
        many = input("how many " + oder + " with chicken would you like:")
        total = int(many) * int(price)
        print(total)
    else:
        price = 4
        many = input("how many " + oder + " would you like:")
        total = int(many) * int(price)
        print(total)    
else:
    time.sleep(.7)
    print("Not today, sorry we dont have" , oder , " today \n" )
    exit()

many = input("how many " + oder + " would you like:")
total = int(many) * int(price)
print("Your total is gonna be $ " , total)



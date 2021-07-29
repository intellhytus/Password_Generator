#!/usr/bin/python3
import random
import os

lower = "abcdefghijklmnopqrstuvqwxyzç" 
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ" 
numbers = "1234567890" 
symbols = "\{;!@#$%&*()+_-^~áàãâ<>=[}]{" 
all = lower + upper + numbers + symbols
length = 28
password = "".join(random.sample(all,length))
print("Your password is:\n",password)

'''O trecho de código acima é responsável por receber os caracteres
e dispor em uma ordem aleatória'''

save = input("Do you want to save your password? [Y/N]\n>>>")

if(save == "Y" or save == "y"):
    
    try:
        archive_name = "saved pass"
        archive = open(archive_name, 'r+')
        delete = input("File already exists. Do you want to subscribe the file? [Y/N]\n>>>")
        if(delete == "Y" or delete == "y"):
            archive_name = "saved pass"
            way = os.getcwd()
            way1 = way + "/" + archive_name
            os.remove(way1)
            archive = open(archive_name, 'w+')
            archive.writelines(password)
            print("Your password has been saved at: \n ", way1)
        elif(delete == "N" or delete == "n"):
            pass
        else:
            print("Syntax Error")
    except FileNotFoundError:
        try:
            archive_name = "saved pass"
            archive = open(archive_name, 'r+')
        except FileNotFoundError:
            archive = open(archive_name, 'w+')
            archive.writelines(password)
            way = os.getcwd()
            print("You password has been saved in: \n", way + "/" + archive_name)
        arquivo.close()
elif(save == "N" or save == "n"):
    pass
else:
    print("Syntax Error")

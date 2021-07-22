#CRYPTER: welcome to my crytopgraphy machine

from colorama import Fore, Back, Style
from tool import talk1
import time

print("")
print("   #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#   ")
print("   #                                   #   ")
print("   #             !        !            #   ")
print("   #         _________________         #   ")
print("   #         |  ~~~     ~~~  |         #   ")
print("   #        {|   *       *   |}        #   ")
print("   #         |       $       |         #   ")
print("   #         |   <=======>   |         #   ")
print("   #    ___________________________    #   ")
print("   #   |      @*************@      |   #   ")
print("   #   |      *      I      *      |   #   ")
print("   #   |      *     am      *      |   #   ")
print("   #   |      *   CRYPTER   *      |   #   ")
print("   #   |      @*************@      |   #   ")
print("   #                                   #   ")
print("   #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#   ")
print("")
print("")

time.sleep(0.75)

def machine():

    # creating key strings
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    # auto generating the vaules of strings
    # value will be generted by taking last to first
    # concatinated with the rest of the string

    values = keys[-1] + keys[0:-1]
    # print(keys)
    # print(values)

    # creating two dictionaries
    encrytDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))

    # user input
    message = input(Fore.BLUE + "Enter your secret message: ")
    time.sleep(0.5)
    mode = input(Fore.BLUE + "Crypto Mode : Encode(E) OR Decode(D)")

    #encode and decode
    if mode.upper() == 'E':
        newMessage = ''.join([encrytDict[letter]
                              for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter]
                              for letter in message.lower()])
    else:
        print("Please try again, wrong choice entered")

    return newMessage.capitalize()

print(machine())

#CRYTER: !THANKYOU! for using my machine
__author__ = 'ApricotHacker'
print("Hello and welcome to my Simple Python Calculator !\nAll you need to do, is to enter a number,\nthe operation you would like to do,\nand the second number !")
print("\n*******************")
print("Restrictions : ")
print("Numbers : Infinite.")
print("Operands Available : +, -, *, /, ** .")
print("*******************\n")
num1 = raw_input("Enter the first number : ")
operand = raw_input("Enter the operand : ")
num2 = raw_input("Enter the second number : ")

if operand=="+" :
    print("%s + %s = %s") % (num1,num2, int(num1)+int(num2))
elif operand=="-" :
    print("%s - %s = %s") % (num1,num2, int(num1)-int(num2))
elif operand=="*" :
    print("%s * %s = %s") % (num1,num2, int(num1)*int(num2))
elif operand=="/" :
    print("%s / %s = %s") % (num1,num2, int(num1)/int(num2))
elif operand=="**" :
    print("%s **2 %s = %s") % (num1,num2, int(num1)**int(num2))

''' Sorry for the lack of PRO-IZM
I know this code is stupid as fock '''

# Creator : Ofek Mizrahi
# AKA - ApricotHacker ( @ApricotHacker - GitHub )
# Assignment for : Barak Nehmad ( AKA @SandSpider2234 - GitHub )
# Enter grade of assignment here :
'''
<Input your comments here>
'''


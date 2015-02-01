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

# CR: Your program should be able to handle exceptions well. If I input a string (or anything which isn't an int)
#     as one of the parameters, the program just exits without any exceptions.
#     A try;except statement, which catches exceptions and allows for retries, would work well here!

# CR: Perhaps implement here some kind of ReadKey function, so the user can see the result before the program exits.
#     Maybe another raw_input but with no implications?

''' Sorry for the lack of PRO-IZM
I know this code is stupid as fock '''

# Creator : Ofek Mizrahi
# AKA - ApricotHacker ( @ApricotHacker - GitHub )
# Assignment for : Barak Nehmad ( AKA @SandSpider2234 - GitHub )
# Enter grade of assignment here :
'''
I shit you not, I've been trying to look for small mistakes here and there, but couldn't find anything except for two.
This is an overall well designed code, which does what I asked you to do (and much, much more!!!)

Grade: 95! Great job!
'''


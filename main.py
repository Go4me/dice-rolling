import random

#defining a function to call random numbers,and it would have two parameters min;for lower parameter and max for mkaximum range
def rolldice(min,max):
    while True:          #to make the while loop to be in infinite condition True is been given
        print("rolling dice..")
        number= random.randint(min,max)   #randint function to generate random number(integer) in between min and max
        print(f"your number : {number}")  #do print the random value which is stored in the number variable
        again = input("do you want to roll again?(y/n)")   #if user wants to stop he can
        if again.lower()=='n':
            break   #comes out of the loop
rolldice(1,6)  #die have a number range from 1 to 6
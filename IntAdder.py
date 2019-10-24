#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program adds all previously occuring integers including the one inputted
# and gives the sum

def main():

    # variable 
    loop_adder = 0
    answer = 0
    # process
    # input
    value_1 = int(input("Enter a number of your choice: "))
    print("")

    while loop_adder <= value_1:
        answer = loop_adder + answer
        loop_adder += 1
    
    print ("The sum is " + str(answer))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:20:10 2019

Author: David Baraona
Course Number: DSCI 15310
Section Number: 002
Due Date: November 6, 2019
"""
print(__doc__)

import pandas as pd

#reads in the csv file
foodData = pd.read_csv("/Users/davidbaraona/Desktop/Group Project.csv")

#converts the csv file into a list
mylist = foodData['food'].tolist()
priceList = foodData['price'].tolist()

"""
def cookBook():
     
    This function opens a menu which allows an imput to be entered. 
    There is no argument though will accept a selection until option 8 is selected 
    
    print(cookBook.__doc__)
    
    data = pd.read_csv("/Users/davidbaraona/Desktop/Recipe List.csv")
 
    endProgram = 'no'
    while endProgram == 'no':
            print ('0 for About:')
            print ('1 for Appetizers: ')
            print ('2 for Sandwiches: ')
            print ('3 for Soups: ')
            print ('4 for Meatless: ')
            print ('5 for Chicken: ')
            print ('6 for Beef: ')
            print ('7 for Pork: ')
            print ('8 for Fish: ')
            print ('9 for Shellfish: ')
            print ('10 for Desserts: ')
            print ('11 for FastFood & Others:' )
            print ('12 for Exit:')
            choice = int(input('enter your selection: '))
            if choice == 0:
                print('')
            elif choice == 1:
                
                print 
            elif choice == 2:
                
                print 
            elif choice == 3:
                 
                print 
            elif choice == 4:
                
                print 
            elif choice == 4:
                
                print 
            elif choice == 5:
                
                print 
            elif choice == 7:
                
                print
            elif choice == 8:
                
                print
            elif choice == 9:
                
                print
            elif choice == 10:
                
                print
            elif choice == 11:
                
                print
            elif choice == 12:
                endProgram == 'yes'
"""

def cheapMeal():
    """
    The function cheapMeal() accepts no arguments and performs the tasks
    needed to help the user find a cheap meal including displaying different
    entrees, sides, and drinks for the user to choose from. Also calculates
    and displays the total cost of the meal
    """
    print(cheapMeal.__doc__)

    print("\nMain entree:\n")
    print(mylist[0:10])
    cheapEntree = input("What is your choice?\n")
    
    if cheapEntree == mylist[0]:
        cheapEPrice = priceList[0]
    elif cheapEntree == mylist[1]:
        cheapEPrice = priceList[1]
    elif cheapEntree == mylist[2]:
        cheapEPrice = priceList[2]
    elif cheapEntree == mylist[3]:
        cheapEPrice= priceList[3]
    elif cheapEntree == mylist[4]:
        cheapEPrice = priceList[4]
    elif cheapEntree == mylist[5]:
        cheapEPrice = priceList[5]
    elif cheapEntree == mylist[6]:
        cheapEPrice = priceList[6]
    elif cheapEntree == mylist[7]:
        cheapEPrice = priceList[7]
    elif cheapEntree == mylist[8]:
        cheapEPrice = priceList[8]
    elif cheapEntree == mylist[9]:
        cheapEPrice = priceList[9]
    
    print("\nPick first side:\n")
    print(mylist[10:21])
    cheapSide1 = input("What is your first side?\n")
    
    if cheapSide1 == mylist[10]:
        cheapS1Price = priceList[10]
    elif cheapSide1 == mylist[11]:
        cheapS1Price = priceList[11]
    elif cheapSide1 == mylist[12]:
        cheapS1Price = priceList[12]
    elif cheapSide1 == mylist[13]:
        cheapS1Price = priceList[13]
    elif cheapSide1 == mylist[14]:
        cheapS1Price = priceList[14]
    elif cheapSide1 == mylist[15]:
        cheapS1Price = priceList[15]
    elif cheapSide1 == mylist[16]:
        cheapS1Price = priceList[16]
    elif cheapSide1 == mylist[17]:
        cheapS1Price = priceList[17]
    elif cheapSide1 == mylist[18]:
        cheapS1Price = priceList[18]
    elif cheapSide1 == mylist[19]:
        cheapS1Price = priceList[19]
    elif cheapSide1 == mylist[20]:
        cheapS1Price = priceList[20]
    
    print("\nPick second side:\n")
    print(mylist[10:21])
    cheapSide2 = input("What is your second side?\n")
    
    if cheapSide2 == mylist[10]:
        cheapS2Price = priceList[10]
    elif cheapSide2 == mylist[11]:
        cheapS2Price = priceList[11]
    elif cheapSide2 == mylist[12]:
        cheapS2Price = priceList[12]
    elif cheapSide2 == mylist[13]:
        cheapS2Price = priceList[13]
    elif cheapSide2 == mylist[14]:
        cheapS2Price = priceList[14]
    elif cheapSide2 == mylist[15]:
        cheapS2Price = priceList[15]
    elif cheapSide2 == mylist[16]:
        cheapS2Price = priceList[16]
    elif cheapSide2 == mylist[17]:
        cheapS2Price = priceList[17]
    elif cheapSide2 == mylist[18]:
        cheapS2Price = priceList[18]
    elif cheapSide2 == mylist[19]:
        cheapS2Price = priceList[19]
    elif cheapSide2 == mylist[20]:
        cheapS2Price = priceList[20]
    
    print("\nPick your drink:\n")
    print(mylist[21:22])
    cheapDrink = input("\nWhat is your drink?\n")
    
    if cheapDrink == mylist[21]:
        cheapDPrice = priceList[21]
    
    print("\nYour meal is: ")
    print(cheapEntree + ",",cheapSide1 + ",",cheapSide2 + ",", cheapDrink)
    
    cheapTotal = cheapEPrice + cheapS1Price + cheapS2Price + cheapDPrice
    print("\nYour total cost is: ")
    print("$",cheapTotal)
    print("\nGood choice!")
    
def healthyMeal():
    """
    The function healthyMeal() accepts no arguments and performs the tasks
    needed to help the user find a healthy meal including displaying different
    entrees, sides, and drinks for the user to choose from. Also calculates
    and displays the total cost of the meal
    """
    print(healthyMeal.__doc__)

    print("\nMain entree:\n")
    print(mylist[22:32])
    healthyEntree = input("What is your choice?\n")
    
    if healthyEntree == mylist[22]:
        healthyEPrice = priceList[22]
    elif healthyEntree == mylist[23]:
        healthyEPrice = priceList[23]
    elif healthyEntree == mylist[24]:
        healthyEPrice = priceList[24]
    elif healthyEntree == mylist[25]:
        healthyEPrice = priceList[25]
    elif healthyEntree == mylist[26]:
        healthyEPrice = priceList[26]
    elif healthyEntree == mylist[27]:
        healthyEPrice = priceList[27]
    elif healthyEntree == mylist[28]:
        healthyEPrice = priceList[28]
    elif healthyEntree == mylist[29]:
        healthyEPrice = priceList[29]
    elif healthyEntree == mylist[30]:
        healthyEPrice = priceList[30]
    elif healthyEntree == mylist[31]:
        healthyEPrice = priceList[31]
    
    print("\nPick first side:\n")
    print(mylist[32:41])
    healthySide1 = input("What is your first side?\n")
    
    if healthySide1 == mylist[32]:
        healthyS1Price = priceList[32]
    elif healthySide1 == mylist[33]:
        healthyS1Price = priceList[33]
    elif healthySide1 == mylist[34]:
        healthyS1Price = priceList[34]
    elif healthySide1 == mylist[35]:
        healthyS1Price = priceList[35]
    elif healthySide1 == mylist[36]:
        healthyS1Price = priceList[36]
    elif healthySide1 == mylist[37]:
        healthyS1Price = priceList[37]
    elif healthySide1 == mylist[38]:
        healthyS1Price = priceList[38]
    elif healthySide1 == mylist[39]:
        healthyS1Price = priceList[39]
    elif healthySide1 == mylist[40]:
        healthyS1Price = priceList[40]
    
    print("\nPick second side:\n")
    print(mylist[32:41])
    healthySide2 = input("what is your second side?\n")
    
    if healthySide2 == mylist[32]:
        healthyS2Price = priceList[32]
    elif healthySide2 == mylist[33]:
        healthyS2Price = priceList[33]
    elif healthySide2 == mylist[34]:
        healthyS2Price = priceList[34]
    elif healthySide2 == mylist[35]:
        healthyS2Price = priceList[35]
    elif healthySide2 == mylist[36]:
        healthyS2Price = priceList[36]
    elif healthySide2 == mylist[37]:
        healthyS2Price = priceList[37]
    elif healthySide2 == mylist[38]:
        healthyS2Price = priceList[38]
    elif healthySide2 == mylist[39]:
        healthyS2Price = priceList[39]
    elif healthySide2 == mylist[40]:
        healthyS2Price = priceList[40]
    
    print("\nPick your drink:\n")
    print(mylist[41:48])
    healthyDrink = input("\nWhat is your drink?\n")
    
    if healthyDrink == mylist[41]:
        healthyDPrice = priceList[41]
    elif healthyDrink == mylist[42]:
        healthyDPrice = priceList[42]
    elif healthyDrink == mylist[43]:
        healthyDPrice = priceList[43]
    elif healthyDrink == mylist[44]:
        healthyDPrice = priceList[44]
    elif healthyDrink == mylist[45]:
        healthyDPrice = priceList[45]
    elif healthyDrink == mylist[46]:
        healthyDPrice = priceList[46]
    elif healthyDrink == mylist[47]:
        healthyDPrice = priceList[47]
    
    print("\nYour meal is: ")
    print(healthyEntree + ",",healthySide1 + ",",healthySide2 + ",",healthyDrink)
    
    healthyCost = healthyEPrice + healthyS1Price + healthyS2Price + healthyDPrice
    print("\nYour total cost is: ")
    print("$",healthyCost)
    print("\nGood choice!")

def quickMeal():
    """
    The function quickMeal() accepts no arguments and performs the tasks
    needed to help the user find a quick meal including displaying different
    entrees, sides, and drinks for the user to choose from. Also calculates
    and displays the total cost of the meal
    """
    print(quickMeal.__doc__)
    
    print("\nMain entree:\n")
    print(mylist[48:59])
    quickEntree = input("What is your choice?\n")
    
    if quickEntree == mylist[48]:
        quickEPrice = priceList[48]
    elif quickEntree == mylist[49]:
        quickEPrice = priceList[49]
    elif quickEntree == mylist[50]:
        quickEPrice = priceList[50]
    elif quickEntree == mylist[51]:
        quickEPrice = priceList[51]
    elif quickEntree == mylist[52]:
        quickEPrice = priceList[52]
    elif quickEntree == mylist[53]:
        quickEPrice = priceList[53]
    elif quickEntree == mylist[54]:
        quickEPrice = priceList[54]
    elif quickEntree == mylist[55]:
        quickEPrice = priceList[55]
    elif quickEntree == mylist[56]:
        quickEPrice = priceList[56]
    elif quickEntree == mylist[57]:
        quickEPrice = priceList[57]
    elif quickEntree == mylist[58]:
        quickEPrice = priceList[58]
    
    print("\nPick first side:\n")
    print(mylist[59:65])
    quickSide1 = input("What is your first side?\n")
    
    if quickSide1 == mylist[59]:
        quickS1Price = priceList[59]
    elif quickSide1 == mylist[60]:
        quickS1Price = priceList[60]
    elif quickSide1 == mylist[61]:
        quickS1Price = priceList[61]
    elif quickSide1 == mylist[62]:
        quickS1Price = priceList[62]
    elif quickSide1 == mylist[63]:
        quickS1Price = priceList[63]
    elif quickSide1 == mylist[64]:
        quickS1Price = priceList[64]
    
    print("\nPick second side:\n")
    print(mylist[59:65])
    quickSide2 = input("what is your second side?\n")
    
    if quickSide2 == mylist[59]:
        quickS2Price = priceList[59]
    elif quickSide2 == mylist[60]:
        quickS2Price = priceList[60]
    elif quickSide2 == mylist[61]:
        quickS2Price = priceList[61]
    elif quickSide2 == mylist[62]:
        quickS2Price = priceList[62]
    elif quickSide2 == mylist[63]:
        quickS2Price = priceList[63]
    elif quickSide2 == mylist[64]:
        quickS2Price = priceList[64]
    
    print("\nPick your drink:\n")
    print(mylist[65:69])
    quickDrink = input("\nWhat is your drink?\n")
    
    if quickDrink == mylist[65]:
        quickDPrice = priceList[65]
    elif quickDrink == mylist[66]:
        quickDPrice = priceList[66]
    elif quickDrink == mylist[67]:
        quickDPrice = priceList[67]
    elif quickDrink == mylist[68]:
        quickDPrice = priceList[68]
    
    print("\nYour meal is: ")
    print(quickEntree + ",",quickSide1 + ",",quickSide2 + ",",quickDrink)
    
    quickCost = quickEPrice + quickS1Price + quickS2Price + quickDPrice
    print("\nYour total cost is: ")
    print("$",quickCost)
    print("\nGood choice!")

def fastFood():
    """
    The function fastFood() accepts no arguments and performs the tasks
    needed to help the user find a fast food restaurant to eat at
    """
    print(fastFood.__doc__)
    
    print("\nFast food:\n")
    print(mylist[69:81])
    fastFoodChoice = input("What is your choice?\n")
    print("\nYour meal is: ")
    print(fastFoodChoice)
    print("\nGood choice!")
    
def restaurant():
    """
    The function restaurant() accepts no arguments and performs the tasks
    needed to help the user find a restaurant to eat at
    """
    print(restaurant.__doc__)
    
    print("\nRestaurants:\n")
    print(mylist[81:98])
    restaurantChoice = input("What is your choice?\n")
    print("\nYour meal is: ")
    print(restaurantChoice)
    print("\nGood choice!")


option = 'yes'

#loop used to restart after an error and to let the user go through until they  choose no
while option != 'no':
    meal = input("What type of meal do you choose? cheap meal at home, healthy meal at home, quick meal at home, fast food, restaurant, or you can view our cookbook by typing cookbook\n")
    
    if meal != "cheap meal at home" and meal != "healthy meal at home" and meal != "quick meal at home" and meal!= "fast food" and meal != "restaurant" and meal != "cookbook":
        print("\nError. Please choose a correct option\n")
        continue
    elif meal == "cheap meal at home":
        cheapMeal()
        option = input("Do you want to choose another meal? yes or no\n")
        if option == 'no':
            print("\nHave a nice meal")
            break
    elif meal == "healthy meal at home":
        healthyMeal()
        option = input("Do you want to choose another meal? yes or no\n")
        if option == 'no':
            print("\nHave a nice meal")
            break
    elif meal == "quick meal at home":
        quickMeal()
        option = input("Do you want to choose another meal? yes or no\n")
        if option == 'no':
            print("\nHave a nice meal")
            break
    elif meal == "fast food":
        fastFood()
        option = input("Do you want to choose another meal? yes or no\n")
        if option == 'no':
            print("\nHave a nice meal")
            break
    elif meal == "restaurant":
        restaurant()
        option = input("Do you want to choose another meal? yes or no\n")
        if option == 'no':
            print("\nHave a nice meal")
            break
    elif meal == "cookbook":
        cookBook()
        option = input("Do you want to choose another meal? yes or no\n")
        if option == 'no':
            print("\nHave a nice meal")
            break
        

























    

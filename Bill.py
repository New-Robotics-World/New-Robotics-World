from os import terminal_size
import shutil
from datetime import datetime

# Get the terminal width
width = shutil.get_terminal_size().columns

#this is our data base for print the menu
vegetables = {'Carrot': 40, 'Potato': 59, 'Broccoli': 35, 'Spinach': 50}
fruits = {'Apple': 2, 'Banana': 1.5, 'Orange': 3, 'Grapes': 4}
cereals = {'Milk': 5, 'Cheese': 8, 'Yogurt': 3, 'Butter': 6}
dairy = {'Rice': 1.5, 'Oats': 2, 'Wheat': 1, 'Barley': 1.8}

#this data base for calculate the total price
allthings = {
    'Carrot': 40,
    'Potato': 59,
    'Broccoli': 35,
    'Spinach': 50,
    'Apple': 2,
    'Banana': 1.5,
    'Orange': 3,
    'Grapes': 4,
    'Milk': 5,
    'Cheese': 8,
    'Yogurt': 3,
    'Butter': 6,
    'Rice': 1.5,
    'Oats': 2,
    'Wheat': 1,
    'Barley': 1.8
}

#these are some required data for this program 
title = "welcome to Grosary shop!"
contact = "Contact us: +91 9029420021"
address = "Opp to Annamalai University, Annamalai Nagarm, Chidambaram"

#this list stoes the things and quantity that they ordered
buyed = []
quanti = []

#This function definition is to calculate the total price of the purchased things
i=0
def total():
  global i
  m=0
  for a in buyed:
      d= allthings[a]*quanti[i]
      sum=d+m
      m=sum
      i+=1
  return str(m)

#This function definition is for finding the purchasing date and time 
def buy_time():
  # Get current date and time
  current_datetime = datetime.now()
  # Format and print the date in "Month name date, year" format
  formatted_date = current_datetime.strftime("%B %d, %Y")
  print("Date:", formatted_date)
  current_time = current_datetime.strftime("%H:%M:%S")
  print("Time:", current_time)

#this function definition is for alining the top part contant
def header():
  lenth = len(title)
  t = int((width - lenth) / 2)
  centered_contact = contact.center(width)
  centered_add = address.center(width)

  print("_" * width)
  print("-" * t + title + "-" * t)
  print(centered_contact)
  print(centered_add)
  print("-" * width)
  print("_" * width)

choice = ["vegetable", "Fruit", "Cereals", "Dairy"]
choose=1
things = dairy
#this function definition is for give the instruction
def option():
  global choose
  global things
  print("\n\nPress 1 for Vegetable database and purchase")
  print("Press 2 for Fruits database and purchase")
  print("Press 3 for Cereals database and purchase")
  print("Press 4 for Dairy database and purchase\n\n")

  choose = int(input("Enter your Option : "))

  if choose==1:
    things=vegetables
  elif choose==2:
    things=fruits
  elif choose==3:
    things=cereals
  else:
    things=dairy

#this function definition is to print the Menu
def layout(heading1=f"{choice[choose-1]} Name", heading2="cost per kg"):

  l_h1 = len(heading1)
  l_h2 = len(heading2)

  width = l_h1 + l_h2 + 7

  print("\n\n\n"+"-" * width)
  print(f"| {heading1} | {heading2} |")

  for key, value in things.items():
    key_space = l_h1 - len(key)
    value_space = l_h2 - len(str(value))
    print("-" * width)
    print(f"| {key}{' '*key_space} | {value}{' '*value_space} |")
    print("-" * width)

#this function is for purchasing things
def order_things(whish = True):
  while (whish):
    item = input(f"\nEnter the name of the {choice[choose-1]} : ")
    if item in things:
      quantity = int(
          input(f"Enter the quantity in kg of the {choice[choose-1]} : "))
      buyed.append(item)
      quanti.append(quantity)
    else:
      print(f"\n*** we do not have that {choice[choose-1]} ***!\n")

    purchase = input(f"\n\nDo you want any other {choice[choose-1]} Y/N : ").lower()
    if purchase == "n":
      whish = False

#this function definition is to print the lower part content
def lower_part():
    print("_"*width)
    buy_time()
    print("Thank you for purchasing. Your bill is processing !".center(width))
    print("-"*width)
    print("Total Amount".center(int(width/2)-1)+":"+total().center(int(width/2)))
    print("-"*width)
    print("!!! Please visit again !!!".center(width))
    print("_"*width)

#Program starts here 
#I call the header function first
header()

shopping=True
while(shopping):

  #here I call the option function to print the instructions
  option()
  #next I call the layout function to print the menu
  layout()
  #then I call the ordre_things function to purchase things
  order_things()

  wish=input("\nDo you want continue shopping Y/N : ").lower()
  if wish=="n":
    shopping=False
lower_part()
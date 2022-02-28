from tip_calculation_functions import *
print("***TIP CALCULATOR***")

#Takes user input to enage with the calculator
Run= input("Enter 'Yes' if you'd like to use the Tip Calculator \nEnter 'No' if you don't \n ")
#Run loop through calculator in case of multiple uses
while Run == "Yes":
    cost_of_food= (float(input("What is the total cost of the food bill ?\n$")))
   
    # Takes input Number of people splitting the bill 
    num_of_people=(int(input("How many people are paying the food bill ?(Don't enter 0)\nPeople: ")))

    # Takes input of percentage of the tip and uses the input to find the tip amount
    tip_percentage=(input("What percentage would you like to tip ?\n"))
    tip_percentage=float(f"0.{tip_percentage}")
    tip_amount = float(tip_percentage * cost_of_food)
    
    #Takes the total bill and calculates the sales tax
    sales_tax = ((float(cost_of_food * .10)))

    #Calculates the total cost and bill
    total_bill=float((cost_of_food + sales_tax + tip_amount))
    split_cost= float(total_bill / num_of_people)

    # Print total bill and how much each person pays or if one person pays
    if num_of_people ==1:
        print(f"\nTotal Bill: {total_bill:.2f}".format())
    elif num_of_people > 1:
        print(f"Total Bill: {total_bill:.2f}".format())
        print(f"\nEach Person Pays: {split_cost:.2f}".format())
    Run= input("\nEnter 'Yes' if you'd like to try another Tip calculation \nEnter 'No' if you're done\n ")

if Run == "No":
    print("\nGive it another try next time\n")


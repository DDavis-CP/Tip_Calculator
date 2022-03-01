from tip_calculation_functions import *
print("***TIP CALCULATOR***")

#Takes user input to enage with the calculator
Run= input("Enter 'Yes' if you'd like to use the Tip Calculator \nEnter 'No' if you don't \n ")

#Run loop through calculator in case of multiple uses
while Run == "Yes":
    #Takes user input for calculations
    info =take_info()
    # Calls calculation function to use user input values to return solutions
    bill_calcv=bill_calc(*info)

    # Print total bill and how much each person pays or if one person pays
    print_calculations(*bill_calcv)
    
    Run=input("\nEnter 'Yes' if you'd like to try another Tip calculation \nEnter 'No' if you're done\n ")
    if Run == "No":
     print("\nGive it another try next time\n")


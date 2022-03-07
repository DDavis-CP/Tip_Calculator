def  take_info():
    validate_cost_of_food=False
    while validate_cost_of_food == False:
      try:
        #Take cost of food
        cost_of_food= (float(input("What is the total cost of the food bill ?\n$")))
        if cost_of_food>0:
          validate_cost_of_food=True
        else:
          print("Invalid Entry")
      except ValueError:
        print("Invalid Value Entry")
   
    #In case user enters an invalid number of people
    #Loop until valid number of people is entered
    validate_num_of_people=False
    while validate_num_of_people==False:
      try:
          # Takes input Number of people splitting the bill 
          num_of_people=(int(input("How many people are paying the food bill ?\nPeople: ")))
          if num_of_people>0:
           validate_num_of_people=True
          else:
            print("Enter number > 0")
          # In case user enters an invalid number of people
      except ValueError:
        print("Invalid Value Entry")
    # Takes input of percentage of the tip and uses the input to find the tip amount
    validate_tip_percentage=False
    while validate_tip_percentage==False:
      try:
         tip_percentage=(int(input("What percentage would you like to tip ?\n")))
         if tip_percentage>0:
          validate_tip_percentage=True
         else:
          print("Invalid Entry")
      except ValueError:
        print("Invalid value entry")



    tip_percentage=float(f"0.{tip_percentage}")
    tip_amount = float(tip_percentage * cost_of_food)

    return cost_of_food,num_of_people,tip_amount
#Function that calculates the solutions using the users input from the take info function
def bill_calc(cost_of_food,num_of_people,tip_amount):
         #Takes the total bill and calculates the sales tax
          sales_tax = ((float(cost_of_food * .10)))

         #Calculates the total cost and bill
          total_bill=float((cost_of_food + sales_tax + tip_amount))
        
          split_cost= float(total_bill / num_of_people)
           
          return num_of_people,total_bill,split_cost
#Function that prints the calculations of the calculator
def print_calculations(num_of_people,total_bill,split_cost):
        if num_of_people ==1:
          print(f"\nTotal Bill: {total_bill:.2f}".format())
        elif num_of_people > 1:
          print(f"Total Bill: {total_bill:.2f}".format())
          print(f"\nEach Person Pays: {split_cost:.2f}".format())

          
def  take_info():
    cost_of_food= (float(input("What is the total cost of the food bill ?\n$")))
   
    # Takes input Number of people splitting the bill 
    num_of_people=(float(input("How many people are paying the food bill ?(Don't enter 0)\nPeople: ")))

    # Takes input of percentage of the tip and uses the input to find the tip amount
    tip_percentage=(input("What percentage would you like to tip ?\n"))
    tip_percentage=float(f"0.{tip_percentage}")
    tip_amount = float(tip_percentage * cost_of_food)

    return cost_of_food,num_of_people,tip_amount

def bill_calc(cost_of_food,num_of_people,tip_amount):
         #Takes the total bill and calculates the sales tax
         sales_tax = ((float(cost_of_food * .10)))

         #Calculates the total cost and bill
         total_bill=float((cost_of_food + sales_tax + tip_amount))
         split_cost= float(total_bill / num_of_people)

         return num_of_people,total_bill,split_cost

def print_calculations(num_of_people,total_bill,split_cost):
        if num_of_people ==1:
          print(f"\nTotal Bill: {total_bill:.2f}".format())
        elif num_of_people > 1:
          print(f"Total Bill: {total_bill:.2f}".format())
          print(f"\nEach Person Pays: {split_cost:.2f}".format())

          
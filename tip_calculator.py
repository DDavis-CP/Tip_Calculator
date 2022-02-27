# Takes input on cost of food 
cost_of_food= (float(input("What is the total cost of the food bill ?\n$")))

# Takes input Number of people splitting the bill 
num_of_people=(int(input("How many people are paying the food bill ?\n")))

# Takes input of percentage of the tip and uses the input to find the tip amount
tip_percentage=(input("What percentage would you like to tip ?\n"))
tip_percentage=float(f"0.{tip_percentage}")
tip_amount = tip_percentage * cost_of_food

#Takes the total bill and calculates the sales tax
sales_tax=float(cost_of_food * .10)
#Calculates the total cost
total_cost= float(((cost_of_food + sales_tax + tip_amount)/ num_of_people))


print(f"The total cost is {total_cost} ")
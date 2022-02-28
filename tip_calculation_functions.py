def  take_info():
    cost_of_food= (float(input("What is the total cost of the food bill ?\n$")))
   
    # Takes input Number of people splitting the bill 
    num_of_people=(int(input("How many people are paying the food bill ?(Don't enter 0)\nPeople: ")))

    # Takes input of percentage of the tip and uses the input to find the tip amount
    tip_percentage=(input("What percentage would you like to tip ?\n"))
    tip_percentage=float(f"0.{tip_percentage}")
    tip_amount = float(tip_percentage * cost_of_food)
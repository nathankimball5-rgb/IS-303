#The following is asking the user information to be able to make 
# the needed calculations. It is all input statements.
print("Welcome to the Trip Cost Calculator!\n".upper())
first_name=input("Enter your first name:")
destination=input("Enter your destination: ")
distance=int(input("Enter the one way distance in miles: "))
miles_per_gallon=int(input("Enter your car's miles per gallon: "))
gas_price=float(input("Enter the price of gas per gallon in US dollars: "))
number_of_travelers=int(input("Enter the number of people traveling:"))
print("\n")

#The following is calculating the total miles, 
# total gallons, estimated cost of gas, and estimated cost per person. 
# It is all calculations.

total_miles=(distance*2)
total_gallons=(total_miles/miles_per_gallon)
estimated_cost_gal=(total_gallons*gas_price)
estimated_cost_person=(estimated_cost_gal/number_of_travelers)

#The following is printing the information that was inputted and calculated.
print("Trip Summary:".upper(), )
print("\n")
print(f"Name: {first_name.upper()} \nDestination: {destination}")
print("Total gallons of gas needed: ", total_gallons)
print("Estimated Total Cost: $", estimated_cost_gal)
print("Estimated Cost Per Person: $", estimated_cost_person)
print("\n" + "Have a great trip!".upper())










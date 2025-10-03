import json
try:
    with open("meals.json", "r") as file:
        meals = json.load(file)
except FileNotFoundError:
    meals = []
selection = input("Would you like to a - Add a meal, b - Edit a meal, c - Sort meals by _____, or d - Terminate the program? ")
while selection != 'd':
    if selection == 'a':
        name = input("Enter a meal name: ")
        rating = int(input("Rate it (1-10): "))
        prep_time = int(input("Prep time in minutes: "))
        meal = {"name": name, "rating": rating, "prep_time": prep_time}
        meals.append(meal)
        with open("meals.json", "w") as file:
            json.dump(meals, file, indent=4)
        selection = input("Would you like to a - Add a meal, b - Edit a meal, c - Sort meals by _____, or d - Terminate the program? ")
    elif selection == 'b':
        search = input("What meal would you like to edit? ")
        updating = input("Would you like to update r - rating, or p - prep time? ")
        updated = input("What would you like the updated value to be? ")
        for meal in meals:
            if meal["name"] == search: 
                if updating == 'r':
                    meal["rating"] = int(updated)
                elif updating == 'p':
                    meal["prep_time"] = int(updated)
                else: 
                    print("Not a valid option. Please go through the menu again.")
        with open("meals.json", "w") as file:
            json.dump(meals, file, indent=4)
        print("Meal rating, if valid, has been updated.")
        selection = input("Would you like to a - Add a meal, b - Edit a meal, c - Sort meals by _____, or d - Terminate the program? ")
    elif selection == 'c':
        sort = input("What would you like to sort by? (rating, prep_time, name) ")
        if sort == "rating" or "prep_time" or "name":
            sorted_meals = sorted(meals, key= lambda m: m[sort], reverse= True ) #lambda saves us from writing a full function
            print(f"Meals sorted by {sort}:")
            for meal in sorted_meals:
                print(f"{meal['name']} - {meal['rating']}/10 ({meal['prep_time']} min)")
        else: 
            print("Not a valid comparator.")
        selection = input("Would you like to a - Add a meal, b - Edit a meal, c - Sort meals by _____, or d - Terminate the program? ")
    else:
        print("Not a valid option!")
        selection = input("Would you like to a - Add a meal, b - Edit a meal, c - Sort meals by _____, or d - Terminate the program? ")



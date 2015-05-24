# deny enter or other types

strength = 0
health = 0
wisdom = 0
dexterity = 0
points = 30
choise = None

print("Welcome to your character editor!\n")

while choise != "0":
	if choise == None:
		print("\t 1 - Add skills to your character")
		print("\t 2 - Remove skills to your character")
		print("\t 3 - View the available points")
		print("\t 0 - Exit")
		choise = input("Select your option: ")

	if choise == "1":
		print("Which skill do you want to add points?")
		print("\t 1 - Strength")
		print("\t 2 - Health")
		print("\t 3 - Wisdom")
		print("\t 4 - Dexterity")
		print("\t 0 - Exit")
		add_option = input("Select your option: ")
		if add_option == "1":
			print("Curent available points:", points)
			add_value = abs(int(input("Amount of points to add: ")))
			if points - add_value < 0:
				print("Not enough points.")
			else:
				strength += add_value
				points -= add_value
				print("The new strength is:", strength)
		elif add_option == "2":
			print("Curent available points:", points)
			add_value = abs(int(input("Amount of points to add: ")))
			if points - add_value < 0:
				print("Not enough points.")
			else:
				health += add_value
				points -= add_value
				print("The new health is:", health)
		elif add_option == "3":
			print("Curent available points:", points)
			add_value = abs(int(input("Amount of points to add: ")))
			if points - add_value < 0:
				print("Not enough points.")
			else:
				wisdom += add_value
				points -= add_value
				print("The new wisdom is:", wisdom)
		elif add_option == "4":
			print("Curent available points:", points)
			add_value = abs(int(input("Amount of points to add: ")))
			if points - add_value < 0:
				print("Not enough points.")
			else:
				dexterity += add_value
				points -= add_value
				print("The new dexterity is:", dexterity)
		elif add_option == "0":
			choise = None
		else:
			print("Invalid option.")

	if choise == "2":
		print("Which skill do you want to remove points?")
		print("\t 1 - Strength")
		print("\t 2 - Health")
		print("\t 3 - Wisdom")
		print("\t 4 - Dexterity")
		print("\t 0 - Exit")
		add_option = input("Select your option: ")
		if add_option == "1":
			print("Curent available points:", points)
			add_value = abs(int(input("Amount of points to remove: ")))
			if points - add_value < 0:
				print("Not enough points.")
			else:
				strength += add_value
				points -= add_value
				print("The new strength is:", strength)
		elif add_option == "2":
			print("Curent available points:", points)
			add_value = abs(int(input("Amount of points to remove: ")))
			if points - add_value < 0:
				print("Not enough points.")
			else:
				health += add_value
				points -= add_value
				print("The new health is:", health)
		elif add_option == "3":
			print("Curent available points:", points)
			add_value = abs(int(input("Amount of points to remove: ")))
			if points - add_value < 0:
				print("Not enough points.")
			else:
				wisdom += add_value
				points -= add_value
				print("The new wisdom is:", wisdom)
		elif add_option == "4":
			print("Curent available points:", points)
			add_value = abs(int(input("Amount of points to remove: ")))
			if points - add_value < 0:
				print("Not enough points.")
			else:
				dexterity += add_value
				points -= add_value
				print("The new dexterity is:", dexterity)
		elif add_option == "0":
			choise = None
		else:
			print("Invalid option.")

	if choise == "3":
		print("Which skill do you want to see the points?")
		print("\t 1 - Strength")
		print("\t 2 - Health")
		print("\t 3 - Wisdom")
		print("\t 4 - Dexterity")
		print("\t 5 - All skills")
		print("\t 0 - Exit")
		add_option = input("Select your option: ")
		if add_option == "1":
			print("The Strength is:", strength)
		elif add_option == "2":
			print("The Health is:", health)
		elif add_option == "3":
			print("The Wisdom is:", wisdom)
		elif add_option == "4":
			print("The Dexterity is:", dexterity)
		elif add_option == "5":
			print("The Strength is:", strength)
			print("The Health is:", health)
			print("The Wisdom is:", wisdom)
			print("The Dexterity is:", dexterity)
		elif add_option == "0":
			choise = None
		else:
			print("Invalid option.")

input("\n\nPress the enter key to exit.")
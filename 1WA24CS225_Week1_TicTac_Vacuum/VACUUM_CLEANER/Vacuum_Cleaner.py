# Vacuum Cleaner Agent
# Simple Reflex + Goal Based Agent

location = input("Enter Vacuum Location (A/B): ").upper()

roomA = input("Enter Room A state (Clean/Dirty): ").capitalize()
roomB = input("Enter Room B state (Clean/Dirty): ").capitalize()

print("\nInitial State")
print("Location:", location)
print("Room A:", roomA)
print("Room B:", roomB)

while roomA == "Dirty" or roomB == "Dirty":

    if location == "A":

        if roomA == "Dirty":
            print("\nRoom A is Dirty")
            print("Suck Dirt in Room A")
            roomA = "Clean"

        else:
            print("\nRoom A is Clean")
            print("Move Right to Room B")
            location = "B"

    elif location == "B":

        if roomB == "Dirty":
            print("\nRoom B is Dirty")
            print("Suck Dirt in Room B")
            roomB = "Clean"

        else:
            print("\nRoom B is Clean")
            print("Move Left to Room A")
            location = "A"

    else:
        print("Invalid location!")
        break

print("\nGoal Achieved!")
print("Room A:", roomA)
print("Room B:", roomB)
print("Both Rooms are Clean")

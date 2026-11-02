
# Simple Reflex Agent - Vacuum Cleaner

# Take room conditions from the user
roomA = input("Enter condition of Room A (Dirty/Clean): ")
roomB = input("Enter condition of Room B (Dirty/Clean): ")

# Vacuum cleaner starts in Room A
current_room = "A"

print("\nVacuum Cleaner Started")

# Check Room A
if current_room == "A":

    if roomA.lower() == "dirty":
        print("Room A is Dirty. Cleaning Room A.")
        roomA = "Clean"
    else:
        print("Room A is already Clean.")

    # Move to Room B
    print("Moving to Room B.")
    current_room = "B"

# Check Room B
if current_room == "B":

    if roomB.lower() == "dirty":
        print("Room B is Dirty. Cleaning Room B.")
        roomB = "Clean"
    else:
        print("Room B is already Clean.")

# Display final room conditions
print("\nFinal Room Conditions:")
print("Room A:", roomA)
print("Room B:", roomB)

print("Cleaning Completed.")

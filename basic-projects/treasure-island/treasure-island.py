print("Welcome to Treasure Island!\nYour mission is to find the treasure.")
direction = input(
    """You're at a corss road. Where do u want to go?\nType "left" or "right"\n"""
)
if direction == "right":
    print("You've fallen into a hole.\nGame over!")
else:

    print("Yoy've come to a lake.There is an island in the middle of the lake.")
    wait_or_swim = input(
        """Type "wait" to wait for boat or type "swim" to swim across.\n"""
    )
    if wait_or_swim == "swim":
        print("You've been attacked by a trout.\nGame over!")
    else:

        print(
            "You arrived at the island unharmed.There is a house with three doors.\none red , one yellow and one blue."
        )
        doors = input("Which one do you chosse?\n")
        if doors == "red":
            print("You've been burned by fire.\nGame over!")
        elif doors == "blue":
            print("You've been eaten by beasts.\nGame over!")
        else:
            print("You found the treasure.\nYou Win!")

import random 



# Define ASCII art representations of dice faces using brackets and zeros
dice_faces = [
    ["[-------] ",
     "[       ]",
     "[   0   ]",
     "[       ]",
     "[-------]"],

     ["[-------] ",
     "[       ]",
     "[   0   ]",
     "[       ]",
     "[-------]"],

    [" ------- ",
     "| 0     |",
     "|   0   |",
     "|     0 |",
     " ------- "],

    [" ------- ",
     "| 0   0 |",
     "|       |",
     "| 0   0 |",
     " ------- "],

    [" ------- ",
     "| 0   0 |",
     "|   0   |",
     "| 0   0 |",
     " ------- "],

    [" ------- ",
     "| 0   0 |",
     "| 0   0 |",
     "| 0   0 |",
     " ------- "]
]

def display_dice_face(number):
    if number >= 1 and number <= 6:
        for line in dice_faces[number - 1]:
            print(line)
    else:
        print("Invalid dice number")

def main():
    try:
        # Ask the user for the number to display on the dice
        user_input = int(input("Enter a number to display on the dice (1-6): "))
        
        # Display the dice face corresponding to the user's input
        display_dice_face(user_input)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
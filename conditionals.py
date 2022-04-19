age = int(input("How old are you? "))
legal_age = 18

if age >= legal_age:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

user_favorite_color = input("What is your favorite color? ")
favorites_colors = ["red", "blue", "green", "yellow"]
disliked_colors = ["black", "white", "brown"]

if user_favorite_color in favorites_colors:
    print("I like " + user_favorite_color + " too!")
elif user_favorite_color in disliked_colors:
    print("I don't like " + user_favorite_color + ".")
else:
    print("I don't know what " + user_favorite_color + " is.")
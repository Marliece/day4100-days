print("=== Your Adventure Simulator ===")
print()
print("""Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with YOU as the star!""")
print()
name = input("What is your name? ")
enemy = input("What is your worst enemy's name? ")
superpower = input("What is your superpower? ")
live = input("Where do you live? ")
food = input("What is your favorite food? ")
print()
print("Hello \033[35m", name, "\033[37m! Your ability to\033[36m", superpower, "\033[37m will make sure you never have to look at \033[33m", enemy, "\033[37m again. Go eat your \033[30m", food, "\033[37m as you walk down the streets of \033[34m", live, "\033[37m and use \033[0m", superpower, "\033[37m for \033[32m good \033[37m and not \033[31m evil \033[37m!")
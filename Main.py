# Start with your program from Exercise 4 - 1 (page 56).
# Make a copy of the list of pizzas, and call it
# "frined_pizzas." Then, do the following:

favorite_fruits = ["blueberries", "cherries", "peaches"]

for fruit in favorite_fruits:
    print(f"I like {fruit.title()}.")
print(f"I like {favorite_fruits[0].title()},"
      f"\nI like {favorite_fruits[1].title()},"
      f"\nbut nothing compares to {favorite_fruits[2].title()},"
      f"\nI really love {favorite_fruits[2].title()}!")

friends_fruits = favorite_fruits[:]

# Add a new pizza (fruit) to the original list.

favorite_fruits.append("bananas")

# Add a different pizza (fruit) to the list "frined_pizzas."

friends_fruits.append("apples")

# Print the message "My favorite pizzas are: ", and then
# use a for loop to print the first list. Print the message
# "My friend's favorite pizzas are: ", and then use a for
# loop to print the second list. Make sure each new
# pizza is stored in the appropriate list.

my_favorite_fruits = f"My favorite fruits are: "

for fruits in favorite_fruits:
    print(f"{my_favorite_fruits} {fruits.title()}")

my_friends_favorite_fruits = f"My friends favorite fruits " \
                             f"are: "

for friend_fruits in friends_fruits:
    print(f"{my_friends_favorite_fruits} {friend_fruits}")

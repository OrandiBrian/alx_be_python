"""
Python scrip that asks the user about the current weather conditions and provide clothing recommendations based on the input
"""

# prompting the user
whether = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# clothing conditions
if whether == "sunny":
    print("wear a t-shirt and sunglasses.")
elif whether == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif whether == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

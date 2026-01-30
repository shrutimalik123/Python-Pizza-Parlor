import random

def pizza_parlor():
    # 1. Game Setup
    menu_toppings = ["pepperoni", "mushrooms", "onions", "peppers", "sausage"]
    score = 0
    rounds = 3

    print("--- 🍕 Python Pizza Parlor 🍕 ---")
    print(f"Toppings available: {', '.join(menu_toppings)}")
    print("Match the customer's order exactly to win points!")

    # 2. Game Loop
    for r in range(1, rounds + 1):
        # Generate a random order of 2 or 3 toppings
        order_size = random.randint(2, 3)
        customer_order = random.sample(menu_toppings, order_size)
        
        print(f"\nRound {r}: A customer wants a pizza with: {', '.join(customer_order)}")
        
        # 3. Player Input
        user_pizza = []
        print("Type your toppings one by one (type 'done' when finished):")
        
        while True:
            topping = input("> ").lower().strip()
            if topping == 'done':
                break
            elif topping in menu_toppings:
                user_pizza.append(topping)
                print(f"Added {topping}!")
            else:
                print("❌ We don't have that topping!")

        # 4. Comparison Logic
        # Sort both lists so the order they were typed in doesn't matter
        if sorted(user_pizza) == sorted(customer_order):
            print("✅ Perfect Pizza! +100 points.")
            score += 100
        else:
            print(f"📉 Wrong toppings! The customer is unhappy. (They wanted: {', '.join(customer_order)})")

    print(f"\n🏁 Shift over! Your final score: {score}")

# Start the game
pizza_parlor()

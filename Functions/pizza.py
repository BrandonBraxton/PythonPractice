def mk_pizza(size, *toppings):
    print("\nMaking your " + str(size) + "-inch pizza with the following topping(s): ")
    for topping in toppings:
        print("- " + topping)

shopping_list = []
shopping = input("What do you want in your shopping list?")
shopping_list.append(shopping) 
print(shopping_list) 
want2 = "R"
while want2 == "R" or want2 == "A":    
    want2 = input("Would you like to remove(R), add(A), or end(E)?")
    if want2 == "A":
        shop = input("What else do you want in your shopping list?")
        shopping_list.append(shop)
        print(shopping_list)
    elif want2 == "R":
        remove = input("What would you like to remove?") 
        shopping_list.remove(remove) 
        print(shopping_list)
    else:
        print(shopping_list)
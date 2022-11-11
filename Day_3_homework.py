# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list


shopping_list = []

def stored_data(name, item, price):
    shopping_list.append({
        'name' : name,
        'item' : item,
        'price' : price,

})

def delete_item(shopping_list, name):
    if name in shopping_list:
        del shopping_list[name]

def main():

    while True:
        name = input(f"What is Your Name?: ")
        item = input(f"What would you like to add to your cart?: ")
        price = input(f"What is the pirce of this item?: $")
        stored_data(name, item, price)
        delete = input(f"Do you want to delete an item?: ")
        
      
        while True:
            keep_going = input(f"Do you want to add more items?: ")

            if keep_going == "yes" or "Yes":
                print(shopping_list)    
                break           

            elif keep_going == "no" or "No":
                break      

            else:
                print(f'Not a valid response. Please enter a yes or no response')

            if delete == 'yes':
                name = input(f"Do you want to delete an item?: ")
                delete(shopping_list, name)


            elif delete== "no" or "No":
                    print(shopping_list)    
                    break      
    


main()


    # need functions for input / show / add / delete / quit



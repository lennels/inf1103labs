inventory = 0

rejectedEntries = 0

while True:
    inputInventory = input("Enter stock quantity or 'quit' to exit: ")
    if inputInventory == 'quit':
        break
    try:
        inventoryFloat = float(inputInventory)
        
        if inventoryFloat != int(inventoryFloat):
            print("Invalid input. Please enter a whole number or a number ending in .0.")
            rejectedEntries += 1
            continue
        if inventory + inventoryFloat > 500:
            rejectedEntries += 1
            print("Overstock alert! You cannot add 500 items. Maximum capacity is 500.")
            break
        elif inventoryFloat < 0:
            rejectedEntries += 1
            print("Invalid input please enter a non-negative stock quantity")
            continue
        else:
            inventory += inventoryFloat
            print(f"Added {inventoryFloat:g} items to inventory. Total inventory: {inventory:g}")
    except ValueError:
        print("Invalid input. Please enter a valid stock quantity or 'quit' to exit")
        rejectedEntries +=1
        continue
    
    
print(f"Total Units Processed: {inventory:g}")
print(f"Total rejected entries: {rejectedEntries}")
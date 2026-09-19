#  Global Constant
MAX_CAPACITY = 500
TAX_RATE = 0.1 # 10% tax rate

def get_valid_input(user_input):
    if user_input == "quit":
        return "quit"
    try:
        user_inputFloat = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid stock quantity or 'quit' to exit") 
        return False
    return user_inputFloat

def process_delivery(current_total, new_value):
    new_value+=current_total
    return new_value

def calculate_tax(amount):
    tax = amount * TAX_RATE
    return tax

def generate_report(total_units, failed_entries):
    print(f"Total Units Processed: {total_units:g}")
    print(f"Total rejected entries: {failed_entries}")
    
def main():
    inventory = 0
    rejectedEntries = 0
    tax = 0
    exit_program = False
    
    while not exit_program:
        user_input = input("Enter stock quantity or 'quit' to exit: ")
        validated_user_input = get_valid_input(user_input)
        if validated_user_input is 'quit':
            exit_program = True
        elif validated_user_input is not False:
            if validated_user_input != int(validated_user_input):
                print("Invalid input. Please enter a whole number or a number ending in .0.")
                rejectedEntries += 1
                continue
            if inventory + validated_user_input > MAX_CAPACITY:
                rejectedEntries += 1
                print("Overstock alert! You cannot add 500 items. Maximum capacity is 500.")
                return "quit"
            elif validated_user_input < 0:
                rejectedEntries += 1
                print("Invalid input please enter a non-negative stock quantity")
                continue
            else:
                inventory = process_delivery(inventory,validated_user_input)
                tax += calculate_tax(validated_user_input)
                print(f"Added {validated_user_input:g} items to inventory. Total inventory: {inventory:g}")
        else:
            rejectedEntries +=1
    generate_report(inventory, rejectedEntries)

if __name__ == "__main__":
    main()
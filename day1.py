from inventory import inventory

# Function to convert the string of the whole inventory to a list 
# of which each item is the inventory of one elf
def parse_inventory(inventory):
    new_inventory = inventory.split('\n\n')
    for value in new_inventory:
        if '\n' in value:
            new_value = value.split('\n')
            i = new_inventory.index(value)
            new_inventory[i] = new_value
    return new_inventory
    
# Function to convert each string in a list to integer
def convert_to_int(inventory_list):
  for value in inventory_list:
    if isinstance(value, list):
      for item in value:
        i = value.index(item)
        value[i] = int(item)
    else:
      i = inventory_list.index(value)
      inventory_list[i] = int(value)
  return inventory_list

# Function to have a list of elves with their total calories
def create_elf_list(number_list):
  elf_list = []
  for value in number_list:
    if isinstance(value, list):
      elf_list.append(sum(value))
    else:
      elf_list.append(value)
  
  return elf_list

# Converting the original inventory string to a list 
new_inventory = parse_inventory(inventory)

# Converting the invetory list  from strings to integers
new_int_inventory = convert_to_int(new_inventory)

# Creating an elf object list where values are the total calories
elves = create_elf_list(new_int_inventory)

# Finding the elf with largest calorie count 
max_calories = max(elves)

# Second part of the quiz.
# To retrieve the second and third largest values, sorting the list.
elves.sort()

# Sum of the last 3 elements of the list 
sum_top_three = elves[len(elves)-1] + elves[len(elves)-2] + elves[len(elves)-3]

print(sum_top_three)
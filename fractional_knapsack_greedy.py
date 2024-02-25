# Fractional Knapsack problem

# This model will assume it can take whole items and
# fractions other items that can be carried in the knapsack

# In this dictionary:
#
# Keys ('item1', 'item2', etc.) represent the items.
# Values are tuples where the first element represents the weight,
# and the second element represents the value.

# Define a total capacity for the knapsack. It is the total allowable weight.
W = 100

knapsack_items = {
    'item1': (30, 66),  # weight 30, value 66
    'item2': (10, 20),  # weight 10, value 20
    'item3': (20, 30),  # weight 20, value 30
    'item4': (50, 60),  # weight 50, value 60
    'item5': (40, 40)  # weight 40, value 40
}

# Sort objects in decreasing order of value-to-weight ratio
sorted_items = sorted(knapsack_items.items(), key=lambda x: x[1][1] / x[1][0], reverse=True)

# Initialize variables
load = 0
value = 0
i = 0
xi = 0

print(sorted_items)

# Main loop
while load < W and i < len(sorted_items):
    weight, val = sorted_items[i][1]

    # Check capacity
    if weight <= W - load:
        xi = 1
    else:
        xi = (W - load) / weight

    # Update load and value
    load += xi * weight
    value += xi * val

    # Print current selection
    print(f"Selected {xi} of {sorted_items[i][0]}")

    # Move to the next item
    i += 1

print("Total value in knapsack:", value)

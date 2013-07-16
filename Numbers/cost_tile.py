# Find Cost of Tile to Cover W x H Floor
# Calculate the total cost of tile it would take to cover a floor plan of width and height,
# using a cost entered by the user.

height = int(raw_input("Height: "))
width = int(raw_input("Width: "))
cost = int(raw_input("Cost: "))

print "Total cost is " + str(width * height * cost) + "€"

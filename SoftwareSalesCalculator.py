# Author: Weijia Fang
# Title: Software Sales Calculator
# Completion Date: Jan 2019

package = int(input("Enter the number of packages ordered: "))

cost = 0
discount = 0
if package >= 100:
    costbeforediscount = 100 * package
    discount = costbeforediscount * 0.4
    cost = costbeforediscount - discount
    print ("The total cost of your purchase was $%.2f"%(cost),"with a discount of $%.2f."%(discount))
elif package >= 50:
    costbeforediscount = 100 * package
    discount = costbeforediscount * 0.3
    cost = costbeforediscount - discount
    print ("The total cost of your purchase was $%.2f"%(cost),"with a discount of $%.2f."%(discount))
elif package >= 20:
    costbeforediscount = 100 * package
    discount = costbeforediscount * 0.2
    cost = costbeforediscount - discount
    print ("The total cost of your purchase was $%.2f"%(cost),"with a discount of $%.2f."%(discount))
elif package >= 10:
    costbeforediscount = 100 * package
    discount = costbeforediscount * 0.1
    cost = costbeforediscount - discount
    print ("The total cost of your purchase was $%.2f"%(cost),"with a discount of $%.2f."%(discount))
else:
    cost = 100 * package
    print ("The total cost of your purchase was $%.2f"%(cost),"with a discount of $0.00.")

# Author: Weijia Fang
# Title: Popular Names With Functions
# Completion Date: March 2019

#A function to get the names, and return as a list
def get_names_list(filename):
    f = open(filename,'r')
    name_list = []
    for line in f.readlines():
        line = line.strip()
        name_list.append(line)
    f.close()
    return name_list

#A function to check the rank of the name the user enter
def check_name(name,name_list):
    if name in name_list:
        rank = name_list.index(name)+1
        return rank
    else:
        return 0

#Main Program
#Use the 2 functions above
girlnames_list = get_names_list('GirlNames.txt')
boynames_list = get_names_list('BoyNames.txt')

print("Enter a name to see if it is a popular girls or boys name.")
name = input('Enter a name to check, or "stop" to stop: ')

#A while loop to get the result and output
while name != 'stop':
    #Girl
    if check_name(name,girlnames_list) != 0:
        print(name,"is a popular girl's name and is ranked:",check_name(name,girlnames_list))
    else:
        print(name,"is not a popular girl's name.")
    #Boy
    if check_name(name,boynames_list) != 0:
        print(name,"is a popular boy's name and is ranked:",check_name(name,boynames_list))
    else:
        print(name,"is not a popular boy's name.")
    #Ask for new input
    name = input('\nEnter a name to check, or "stop" to stop:')

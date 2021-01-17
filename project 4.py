#Gillian Line-Luttrell

print('This program keeps track of rowers on a team.')
rower_one=input("Enter the name of rower 1: ")
print(rower_one)
rower_one_weight=float(input("Enter the weight of rower 1 (in pounds): "))
print(rower_one_weight)

rower_two=input("Enter the name of rower 2: ")
print(rower_two)
rower_two_weight=float(input("Enter the weight of rower 2 (in pounds): "))
print(rower_two_weight)

rower_three=input("Enter the name of rower 3: ")
print(rower_three)
rower_three_weight=float(input("Enter the weight of rower 3 (in pounds): "))
print(rower_three_weight)

rower_four=input("Enter the name of rower 4: ")
print(rower_four)
rower_four_weight=float(input("Enter the weight of rower 4 (in pounds): "))
print(rower_four_weight)

average_weight=float((rower_one_weight+rower_two_weight+rower_three_weight+rower_four_weight)/4)
print('\nAverage weight: {:.1f}'.format(average_weight))

list_one=[rower_one, rower_two, rower_three, rower_four]
list_two=[rower_one_weight, rower_two_weight, rower_three_weight, rower_four_weight]
location=int(input('\nEnter a list location (1-4): '))
print(location)
if location==1:
    print('Name: ',list_one[0])
    print('Weight in pounds: ',list_two[0])
elif location==2:
    print('Name: ',list_one[1])
    print('Weight in pounds: ',list_two[1])
elif location==3:
    print('Name: ',list_one[2])
    print('Weight in pounds: ',list_two[2])
elif location==4:
    print('Name: ',list_one[3])
    print('Weight in pounds: ',list_two[3])

remove=int(input('\nEnter a rower to remove (1-4): '))
print(remove)
if remove==1:
    print(list_one.pop(0))
    (list_two.pop(0))
elif remove==2:
    print(list_one.pop(1))
    (list_two.pop(1))
elif remove==3:
    print(list_one.pop(2))
    (list_two.pop(2))
elif remove==4:
    print(list_one.pop(3))
    (list_two.pop(3))

print('\nAverage weight: {:.1f}'.format(sum(list_two)/3))

location_two=int(input('\nEnter a list location (1 - 3): '))
print(location_two)
if location_two==1:
    print('Name: ',list_one[0])
    print('Weight in pounds: ',list_two[0])
elif location_two==2:
    print('Name: ',list_one[1])
    print('Weight in pounds: ',list_two[1])
elif location_two==3:
    print('Name: ',list_one[2])
    print('Weight in pounds: ',list_two[2])




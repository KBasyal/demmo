# I am trying to learn for loop in detail
print('hello world')
# Starting for loop from here

fruits=["Apple","Banana","Orange","Pineapple"]
for fruit in fruits:
    print(fruit)


# givng another eample of for loop

Subjects= ["Maths","Science","Social","Account","English"]
for subject in Subjects:
    print(subject)

# for loop for range
for i in range(5):
    print(i)

# another eample of range in for loop
for l in range(15):
    print(l)

# for loop in list of lists

list1=[["kamal","Basyal"],["anita","basyal"],["kabita","basyal"]]

#Casting list into dictonary
dict1= dict(list1)
print(dict1)

# for items in list1:
#     print(items)

for items, surname in list1:
    print("Surname of",items, "is",surname)
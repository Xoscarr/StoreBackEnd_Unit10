about_me = {
    "name": "Oscar",
    "last": "Rodriguez", 
    "age": 26,
    "hobbies":[],
    "address": {
        "street":"42 evergreen",
        "city":"Springfield"
    }

}
print(about_me["name"])

# using string formatting, print the full name (first last)
print(f"{about_me['name']} {about_me['last']}")

# street ands city
# print(about_me["address"]["street"])
address = about_me["address"]
print(address["street"])
print(address["city"])

#modify
about_me["age"] = 35 

# create new key
about_me["phone"]= "123 3232 3444"

print(about_me)

# how to test the type of code
#print(type(about_me["address"])

# List 
print("-" * 40)

names = []
names.append("Angel")
names.append("Oscar")

print(names)

print(names[0])
print(names[1])

# for loop 
print("using loops" * 4)
for name in names:
    print(name)


nums = [1,2,3,4,5,6,7,5,4,4,7,2,54,6,2,768,89,345,5467,908,2,4,78,678,123,435]
# exe 1: print all nunbers

for num in nums:
    if num !=4:
        print(num)

# exe 2: count how many 4s there are in the list 
# start a counter on 0
# travel the lis tand get each number inside
#if the number is a four increase the counter 
# print eh counter 
counter = 0 
for num in nums:
    if num == 4:
        counter = counter + 1 

print(counter)
# using list count
# print(nums.count(4))

# exe 3: Sum all the nums 
# start with a sum of 0
# travel the list and get each number inside
# add the number to the running sum
# print the sum
my_sum = 0 
for num in nums:
    # sum = sum + num 
    my_sum += num
print(my_sum)

print(sum(nums))

students = [ 
    {
        "name": "Kvon",
        "age": 36
    },
   {
        "name": "Gary",
        "age": 37
    },
    {
        "name": "Oscar",
        "age": 33
    },
    {
        "name": "Angel",
        "age": 35
    },
]

# exe 4: Sum the ages (141)
total = 0 
for student in students:
    age = student["age"]
    total += age
print(total)





# Find the minium algorithm

ages = [ 62,34,21,78,23,88,20, 65,32, 17, 94, 17, 16, 65,21,89
]
min = ages[0]
for num in ages:
    if num < min:
        min = num 
print(f"the youngest person's age is {min}")

from mock_data import catalog
def get_unique_categories():
    print("-" * 30)

    categories = []
    for prod in catalog:
        if prod["category"] not in categories:
            categories.append(prod["category"])
    
    print(categories)


        #print(prod["category"])

get_unique_categories()


colors = ["red", "blue", "orange", "orange", "Blue", "Green", "Red", "blue", "Black", "gray", "GrAY", "oRanGE"]
def get_unique_colors():
    print("*" * 30 )
    result = []
    for uColor in colors:
        if uColor.lower() not in result:
            result.append(uColor.lower())
    print(result)
              

get_unique_colors()
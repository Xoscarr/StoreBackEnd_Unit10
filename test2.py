def numbers():
    print("--- numbers test ----")
    nums = [10,345,34,12,345,567,45,567,789,6345,12354,5231,5678,789,645,23145,34567,589,341,3]
    
    sum=0
    for element in nums:
        sum += element
    
    print(f"the Result is:{sum}" )
    

    print("*" * 30)

    car ={
        "color": "red",
        "brand": "vw",
        "year": 1975,
        
    }
    print(car)

    print(f"My car is {car['color']}")

    print("*" * 30)
    
    test_list = [{'Name' : 'Apple', 'Price' : 18, 'Color' : 'Red'},
             {'Name' : 'Mango', 'Price' : 20, 'Color' : 'Yellow'},
             {'Name' : 'Orange', 'Price' : 24, 'Color' : 'Orange'},
             {'Name' : 'Plum', 'Price' : 28, 'Color' : 'Red'}]

    total=0
    for fruit in test_list:
         price = fruit["Price"]
         total += price
    print(total)



    cheapest = test_list[0]
    for fruit in test_list:
        if fruit["Price"] < cheapest["Price"]: 
            cheapest = fruit
    print(cheapest["Name"])
numbers()

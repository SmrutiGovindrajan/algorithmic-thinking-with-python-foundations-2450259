for i in range(1, 101):
    if (i%15)==0:
        print("fizzbuz", end=", ")
    elif (i%3)==0:
        print("fizz", end=", ")
    elif(i%5)==0:
        print("buzz", end=", ")

    else:
        print(i, end=", ")
num = int(input("Enter a number: "))
result = find_factors(num)
print("Factors of num are:"result)
except ValueError:
    print("Please enter a valid integer.")

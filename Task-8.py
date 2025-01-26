string = str(input("Enter a String: "))
vowels = 'aeiouAEIOU'
count = 0
for char in string:
    if char in vowels:
        count += 1
        
print("Number of Vowels = ", count)
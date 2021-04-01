# 1. Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as 
# the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    result = []
    for i in range(num, -1, -1):
        result.append(num)
        num-=1
    print(result)
countdown(7)

# 2. Print and Return - Create a function that will receive a list with 
# two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([8,9]))

# 3. First Plus Length - Create a function that accepts a list and returns 
# the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 
# 1 + length: 5)
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([5, 67, 23, 90, 34, 6]))

# 4. Values Greater than Second - Write a function that accepts a list and 
# creates a new list containing only the values from the original list that 
# are greater than its 2nd value. Print how many values this is and then 
# return the new list. If the list has less than 2 elements, have the 
# function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and 
# return [5,3,4]

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    else:
        val = list[1]
        count = 0
        result = []
        for i in range(len(list)-1):
            if list[i] > val:
                count+=1
                result.append(list[i])
        print(count)
        return result

print(values_greater_than_second([8,5,4,2,0,6,10,4]))

# 5. This Length, That Value - Write a function that accepts two integers as 
# parameters: size and value. The function should create and return a list 
# whose length is equal to the given size, and whose values are all the given 
# value.
# Example: length_and_value(4,7) should return [7,7,7,7]

def length_and_value(size, val):
    result = []
    for i in range(size):
        result.append(val)
    return result

print(length_and_value(6,6))
        
        
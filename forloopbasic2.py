# 1. Biggie Size - Given a list, write a function that changes all positive 
# numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose 
# values are now [-1, "big", "big", -5]
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

print(biggie_size([0,2,8,-5,-2,9,-19,3]))

# 2. Count Positives - Given a list of numbers, create a function to replace 
# the last value with the number of positive values. (Note that zero is not 
# considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] 
# and returns it
def count_positives(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count+=1
    list[len(list)-1] = count
    return list
print(count_positives([-1,8,-6,9,3,5,-4, 2]))

# 3. Sum Total - Create a function that takes a list and returns the sum of 
# all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
def sum_total(list):
    sum = 0
    for i in list:
        sum+=i
    return sum
print(sum_total([3,4,5]))

# 4. Average - Create a function that takes a list and returns the average 
# of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(list):
    sum = 0
    for i in list:
        sum+=i
    avg = sum / len(list)
    return avg

print(average([1,2,3,4,5]))

# 5. Length - Create a function that takes a list and returns the length 
# of the list.
# Example: length([37,2,1,-9]) should return 4
def length(list):
    return len(list)
print(length([1,2,3,4]))

# 6. Minimum - Create a function that takes a list of numbers and returns 
# the minimum value in the list. If the list is empty, have the function 
# return False.
# Example: minimum([37,2,1,-9]) should return -9
def minimum(list):
    if len(list) < 1:
        return False
    else:
        min = list[0]
        for i in list:
            if i < min:
                min = i
        return min
print(minimum([-8,9,30,-2,3,10,-33,-4]))

# 7. Maximum - Create a function that takes a list and returns the maximum 
# value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
def maximum(list):
    if len(list) < 1:
        return False
    else:
        max = list[0]
        for i in list:
            if i > max:
                max = i
        return max
print(maximum([-20,78,-2,-8,2,4,5,8,23]))

# 8. Ultimate Analysis - Create a function that takes a list and returns a 
# dictionary that has the sumTotal, average, minimum, maximum and length of 
# the list.
# Example: ultimate_analysis([37,2,1,-9]) should return 
# {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(list):
    sum = 0
    min = list[0]
    max = list[0]
    for i in list:
        sum+=i
        if min > i:
            min = i
        if max < i:
            max = i
    res = {'sumTotal': sum, 'average': sum/len(list), 'minimum': min, 'maximum': max, 'length': len(list)}
    return res
print(ultimate_analysis([3,9,2,10,4,6]))

# 9. Reverse List - Create a function that takes a list and return that list 
# with values reversed. Do this without creating a second list. (This 
# challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse(arr):
    for i in range(len(arr)/2):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr
print(reverse([1,2,3,4,5]))
        
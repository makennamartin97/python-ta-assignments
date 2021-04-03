b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

	



def countdown(num):
    nums_list = []
    for val in range(num, -1, -1):
        nums_list.append(val)
    return nums_list
print(countdown(8))
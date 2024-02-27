#1
characters = input("Enter a list of numbers separated by commas: ").split(',')
characters = [num for num in characters]
print("The list is:", characters)

list1 = ["m","na","i","ke"]
list2 = ["y","me","s","lly"]
print([x+y for x,y in zip(list1,list2)])
#2
numbers = [1,2,3,4,5,6,7]
print([i**2 for i in numbers])

list1 = ["hello","take"]
list2 = ["dear","sir"]
result = []
for x in list1:
    for y in list2:
        result.append(x+' '+y)
print(result)
#3
dict1 = {'Ten': 10,'Twenty': 20,'Thirty': 30}
dict2 = {'Thirty': 30,'Fourty': 40,'Fifty': 50}
print({**dict1, **dict2})

sampleDict = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])
#4
tuple1 = ("Orange", [10,20,30], (5,15,25))
list_element = tuple1[1]
value = list_element[1]
print(value)

tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)
#5
input_line = input("Enter a line of text: ")
letter_counts = {}
for char in input_line:
    if char.isalpha():
        char = char.lower()
        if char not in letter_counts:
            letter_counts[char] = 1
        else:
            letter_counts[char] += 1
print("Letter counts:")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")
#6
n = int(input("Enter a number (1-100): "))
import random
numbers = [random.randint(1, 100) for _ in range(n)]
for i in range(len(numbers)):
    min_index = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = numbers.index(j)
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
search_key = int(input("Enter a search key: "))
found = False
while not found and search_key >= numbers[0]:
    if search_key == numbers[0]:
        found = True
    else:
        numbers = numbers[1:]
if found:
    print(f"Found key {search_key} at position {numbers.index(search_key)+1} in list")
else:
    print("Not Found!")
def recursive_binary_search(numbers, low, high, search_key):
    if low > high:
        return False
    mid = (low + high) // 2
    if numbers[mid] == search_key:
        return True
    elif numbers[mid] < search_key:
        return recursive_binary_search(numbers, mid+1, high, search_key)
    else:
        return recursive_binary_search(numbers, low, high-1, search_key)

found = recursive_binary_search(numbers, 0, len(numbers)-1, search_key)
if found:
    print(f"Found key {search_key} at position {numbers.index(search_key)} in list")
else:
    print("Not Found!")
def iterative_binary_search(numbers, search_key):
    low = 0
    high = len(numbers)-1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == search_key:
            return True
        elif numbers[mid] < search_key:
            low = mid + 1
        else:
            high = mid - 1
    return False
found = iterative_binary_search(numbers, search_key)
if found:
    print(f"Found key {search_key} at position {numbers.index(search_key)} in list")
else:
    print("Not Found!")
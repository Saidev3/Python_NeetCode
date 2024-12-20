arr = [1, 2, 3, 4, 5]

print("READ")
# READING FROM AN ARRAY --> O(1)

index = 3
print(arr[index])

print("------------------------------------------------------------------------------")

print("TRAVERSE")
# TRAVERSING THROUGH AN ARRAY --> O(n)

print("Using For Loop")
for i in range(len(arr)):
    print(arr[i], end="->")
print()

print("Using While Loop")
index = 0
while index < len(arr):
    print(arr[index], end="->")
    index += 1
print()

print("------------------------------------------------------------------------------")

print("DELETE")
# DELETING FROM AN ARRAY --> O(n)

print("From the end of Array --> O(1)")
print(f"Before Delete: {arr}")
del arr[len(arr)-1]
print(f"After Delete: {arr}")

arr = [1, 2, 3, 4, 5]
print("In the middle of Array --> O(n)")
print(f"Before Delete: {arr}")
index_to_be_deleted = 1
for index in range(index_to_be_deleted, len(arr)-1):
    arr[index] = arr[index+1]
del arr[len(arr)-1]
print(f"After Delete: {arr}")

print("------------------------------------------------------------------------------")

print("INSERT")
# INSERTING IN AN ARRAY --> O(n)

arr = [1, 2, 3, 4, 5]
print("Inserting at an end --> O(1)")
print(f"Before Delete: {arr}")
arr.append(6)
print(f"After Delete: {arr}")

arr = [1, 2, 3, 4, 5]
print("Inserting in the middle --> O(n)")
index_to_be_inserted_at = 2
element_to_be_inserted = 8
print(f"Before Delete: {arr}")
arr.append("place_holder_for_new_element")
for i in range(len(arr)-1, index_to_be_inserted_at-1, -1):
    arr[i] = arr[i-1]
arr[index_to_be_inserted_at] = element_to_be_inserted
print(f"After Delete: {arr}")
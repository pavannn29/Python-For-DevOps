'''
List Methods
Let's look at different list methods in Python:

copy(): Returns a shallow copy of the list.
clear(): Removes all elements from the list.
count(): Returns the number of times a specified element appears in the list.
extend(): Adds elements from another list to the end of the current list.
index(): Returns the index of the first occurrence of a specified element.
remove(): Removes the first occurrence of a specified element.
'''
# Example remove(): Removes the first occurrence of a specified element.

servers = ["web-01", "web-02", "web-03", "db-01", "cache-01"]

servers.remove("web-01")
print("List after removing: ", servers)

# Example append(): Adds an element to the end of the list.

servers = ["web-01", "web-02", "web-03", "db-01", "cache-01"]

servers.append("cache-02")
print("list after appending: ",servers)

# Example sort(): Sorts the list in ascending order (by default).
l1 = [1, 24, 64, 48, 98, 55]

l1.sort()
print("Sort list: ", l1)

# Example reverse(): Reverses the order of the elements in the list.

l1 = [1, 24, 64, 48, 98, 55]

l1.reverse()
print("Reverse list: ", l1)

# Example insert(): Inserts an element at a specified position.

l1 = [1, 24, 64, 48, 98, 55]

l1.insert(7, 29) # this will add 29 at 7th index 
print("List after inserting: ", l1)

# Example pop(): Removes and returns the element at the specified position (or the last element if no index is specified).

l1 = [1, 24, 64, 48, 98, 55]

l1.pop(2) # will delete element at the index 2 and return its value
print("List after popping: ",l1)
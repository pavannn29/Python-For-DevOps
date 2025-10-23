l = [24, 29, 68, 76]

'''
index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1
'''

# This can be simplified usinf enumarate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")
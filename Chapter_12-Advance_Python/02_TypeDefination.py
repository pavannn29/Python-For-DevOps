'''
Type hits are added using the colon (:) syntax for variables and the -> syntax for function return type.

'''

# Variable type hint 
age: int = 19

# Function type hint 
def greeting(name: str) -> str:
    return f"Hello, {name}!"

# Usage 
print(greeting("Pavan"))


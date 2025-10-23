'''
The basic syntax of the match statement involves matching a variable against several cases
using the case keyword. Match case is likely to be switch case in another language.
'''

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not found"
        case 500:
            return "Internal server error"
        case _:
            return "Unknown status"
        
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(403))
        
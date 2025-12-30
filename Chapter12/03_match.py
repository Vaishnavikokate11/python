# match statement example
def http_error(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 400:
            return "Bad Request"
        case _:
            return "Unknown status"
        
print(http_error(200)) 
print(http_error(500))
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
 

custom_exception = CustomError("This is a custom error message")
 

try:
    raise custom_exception
except CustomError as ce:
    print(f"Caught a custom exception: {ce}")
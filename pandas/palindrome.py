def is_palindrome(s):
    s = s.lower()  # Convert to lowercase
    s = ''.join(c for c in s if c.isalnum())  # Remove non-alphanumeric characters
    return s == s[::-1]

input_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome")
else:
    print(f"{input_string} is not a palindrome")

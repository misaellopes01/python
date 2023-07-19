name = input("Whats your name? ").strip().title()
# Remove whitespace from a string on the left or right
# print(name.strip())
# Capitalize cases
# print(name.capitalize())
# Split user's name into first name and last name
first, last = name.split(' ')
print(f"First name: {first}, Last name: {last}")
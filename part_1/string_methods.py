# Examples of string methods
text = "Hello World"
 
print(text.lower())
print(text.upper())

text_with_whitespace = "  Hello World  "
print(text_with_whitespace.strip())
print(text.replace("Hello", "Hi"))

text_with_spaces = "Hello World"
print(text_with_spaces.split())

list_of_strings = ["Hello", "World"]
print(" ".join(list_of_strings))
print(text.find("World"))
print(text.startswith("Hello"))
print(text.endswith("World"))

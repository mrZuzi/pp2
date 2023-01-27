print("Hello")
print('Hello')

#Assign String to a Variable
a = "Hello"
print(a)

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Strings are Arrays
a = "Hello, World!"
print(a[1]) #Answer=> e

#Looping Through a String
for x in "banana":
    print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String 1
txt = "The best things in life are free!"
print("free" in txt)

#Check String 2 by if
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#Check if NOT 1
txt = "The best things in life are free!"
print("expensive" not in txt)

#Check if NOT 2 by if
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")




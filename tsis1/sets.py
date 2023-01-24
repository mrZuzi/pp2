fruits = {"apple", "banana", "cherry"}
if 'apple' in fruits:
    print("Yes, apple is a fruit")
    
fruits = {"apple", "banana", "cherry"}
fruits.add('orange')
print(fruits)

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove('banana')
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.discard('banana')
print(fruits)

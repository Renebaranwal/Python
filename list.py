# data=["apple","mango",23,4,5]
# print(data)
# print(len(data))
# print(type(data))

# fruits=list(("apple","mango","kiwi","cherry"))
# print(fruits)

# data=list() #empty list
# print(data)


# fruits=list(("apple","mango","kiwi","cherry","orange"))
# fruits[2]="mango"
# print(fruits)

# fruits[1:3]=["apple","cranberry"]
# print(fruits)

# fruits=list(("apple","mango","kiwi","cherry","orange"))
# print(fruits)
# fruits[1:4]=["apple","cranberry"]
# print(fruits)

# fruits=list(("apple","mango","kiwi","cherry","orange"))
# quantity=(10,20,30,40)
# print(fruits)
# print(quantity)
# fruits.extend(quantity) # we can extend our list with tuples, set,dic etc.
# print(fruits)

# fruits.insert(1,"cherry")
# print(fruits)

# fruits.append("cherry") # it will add at the last of the element
# print(fruits)

#remove an element
# fruits=list(("apple","mango","kiwi","cherry","orange"))
# print(fruits)

# fruits.remove("kiwi") #remove always takes a value it does not take index 
# print(fruits)

# fruits.pop(2) #pop cannot take value , it will take index
# print(fruits)

# fruits.pop() # it will remove last element
# print(fruits)

# fruits.clear() # it will clear the entire list and show as empty
# print(fruits)

#del fruits

# to sort the list
# fruits=list(("apple","mango","kiwi","cherry","orange"))
# print(fruits)

#fruits.sort(reverse=True)
# fruits.sort()
# print(fruits)

# fruits.reverse()
# print(fruits)

#copy the list
# fruits=list(("apple","mango","kiwi","cherry","orange"))
# print(fruits)

# newfruits=fruits.copy()
# print(newfruits)

# newfruits=list(fruits)
# print(newfruits)

# quantity=[10,20,30]
# data=fruits+quantity
# print(data)

# data=fruits.count("apple") # count the number of apple
# print(data)


# fruits=list(("apple","mango","kiwi","cherry","orange"))
#print(fruits)
# for i in fruits:
#     print(i)
# 

#list comprehance
fruits=list(("apple","mango","kiwi","cherry","orange"))
data=[i for i in fruits if i!="kiwi"]
print(data)
# List basics

list = [2,3,4,4,56,1]

list.append(5)
print(list)
x = list.pop()
print(x)
print(list[1:4])
print(list[::-1])

# List comprehension

squarelist = [x*x for x in range(5)] 
print(squarelist) #list of square 

squareevenlist = [x*x for x in range(20) if x%2 == 0]
print(squareevenlist)

users = [("Amit", 25), ("Ravi", 20), ("Zoya", 30)]
users.sort(key=lambda x: x[1])
print(users)
users.sort(key=lambda x:x[0], reverse = True)
print(users)

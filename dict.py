    # students is dictionary which will store 
    # name and marks of a student 
students = {} 
# No. of inputs by the user 
n = int(input('No of inputs: ')) 
    
while n != 0: 
    name, marks = input().split() 
    students[name] = int(marks) 
    n -= 1 
print(students) 
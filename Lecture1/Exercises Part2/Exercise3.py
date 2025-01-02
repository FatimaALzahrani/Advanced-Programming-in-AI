# Assume that we execute the following assignment statements:
#  width = 17
#  height = 12.0
'''
 For each of the following expressions, write the value of the expression and the
 type (of the value of the expression).
 1. width//2
 2. width/2.0
 3. height/3
 4. 1 + 2 * 5
'''
width = int(input("Enter width: "))
height = float(input("Enter height: "))
# width = 17
# height = 12.0

print(f"1. width//2 = {width//2}, Type: {type(width//2)}")
print(f"2. width/2.0 = {width/2.0}, Type: {type(width/2.0)}")
print(f"3. height/3 = {height/3}, Type: {type(height/3)}")
print(f"4. 1 + 2 * 5 = {1 + 2 * 5}, Type: {type(1 + 2 * 5)}")
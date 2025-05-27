# String
str1 = "Python"
str2 = 'Python'
str3 = '''Python'''
str4 = """Python"""

# Number
int1 = 1
float1 = 1.1

# Boolean
t = True
f = False

# List
# Mutable: Can edit → For dynamic data (slower than tuple)
list1 = [str1, 'String', int1, 2, float1, 2.2, t]
print(list1)

# Tuple
# Immutable: Cannot edit individual elements (can overwrite entire variable) → For static data (faster than list)
tuple1 = (str1, 'String', int1, 2, float1, 2.2, f)
print(tuple1)

# Dictionary
dict1 = { "Name": "Man", "Age": 22, "Skill": ['AWS', "Python",'''Jenkins'''], "Job": f, "Passion": t }
print(dict1)

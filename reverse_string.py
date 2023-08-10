import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack() # making an object of the stack

for char in string:
    s.push(char) # this will push on to the stack which first letter would be g at the bottom 

while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)


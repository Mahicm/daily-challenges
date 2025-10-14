#----------------------------------Method 1
#Reverse a string with a built in function
def reverse_string_builtin(s):
    return s[::-1]

string = reverse_string_builtin("Hello, World!")
print("reverse with slice method",string)  # Output: !dlroW ,olleH     

#--------------------------------Method 2 List method to string-------------------------- 
def reverse_string_method(s):
    s.reverse()
    # s="".join(reversed(s)) #reveresed() is a built-in function that returns an iterator that accesses the given sequence in the reverse order.
    return "".join(s)
#list.reverse() #reverses the elements of the list in place.only for list
string = list("Hello, World!")
reversed_string = reverse_string_method(string)
print("reverse with list method",reversed_string)  # Output: !dlroW ,olleH


#--------------------------Method 3 Using loop-----------------------------------
def reverse_string_loop(s):
    reversed_str = ""
    for i in range(len(s)-1,-1,-1):
        reversed_str += s[i]
    return reversed_str

string = reverse_string_loop("Hello, World!")
print("reverse with loop",string)  # Output: !dlroW ,olleH  


#--------------------------Method 4 Using recursion-----------------------------------
def reverse_string_recursion(s):
    if(len(s)==0):
        return s
    return reverse_string_recursion(s[1:]) + s[0]
string = reverse_string_recursion("Hello, World!")
print("reverse with recursion",string)  # Output: !dlroW ,olleH 
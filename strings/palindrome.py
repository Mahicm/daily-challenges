# ------Method 1 Using Slice method and comparison-----
def palindrome(s):
    nw_string = s[::-1]
    if(s==nw_string):
        return "panlindrome"
    else:
        return "Not a Panlindrome"

s = "car"
print(palindrome(s))

# ------Method 2 Using 2 pointer Method-----
def palindromeLoop(s):
    left,right = 0, len(s)-1
    while left<right:
        if(s[left]==s[right]):
            left+=1
            right-=1
        else:
            return False
    return True

s = input("Enter a string: ").lower().replace(" ","") # to ignore case and spaces if asked
print(palindromeLoop(s))

# ------Method 3 Given a string and checking palindrome without converting to a string-----
def isPalindrome(x):
    if(x<0):
        return False
    if(x>0 and x%10==0):
        return False
    if(x<10):
        return True
    else:
        reversed_half=0
        while(x>reversed_half):
            reversed_half = (reversed_half*10)+(x%10)
            x=x//10
        if(len(str(x))==len(str(reversed_half))):
            if(x==reversed_half):
                return True
            else:
                return False
        else:
            if(x==(reversed_half//10)):
                return True
            else:
                return False
    
x = 121
print(isPalindrome(x))

'''Step 1: 
Handle Special Cases
If the number is negative, it’s not a palindrome (e.g., -121).
If the number ends with 0 (but isn’t 0 itself), it can’t be a palindrome (e.g., 10).

Step 2: 
Reverse Half the Number
Initialize a variable, say reversed_half = 0.
While the original number is greater than reversed_half:
Pop the last digit from the original number and push it onto reversed_half.
Example: For 1221,
First iteration: original = 122, reversed_half = 1
Second: original = 12, reversed_half = 12

Step 3: 
Check for Palindrome
For even length numbers: If original == reversed_half, it’s a palindrome.
For odd length numbers: If original == reversed_half // 10, it’s a palindrome (middle digit doesn’t matter).'''
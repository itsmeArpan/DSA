#!/usr/bin/env python3
# Reverse positive integer.
def intreverse(n):
    n = str(n)
    reverse_num = ''
    for i in range(0,len(n)):
        reverse_num = n[i] + reverse_num
    return reverse_num


# Check "(" and ")" balance and validation in a string.
def matched(s):
    result = 0
    count = 0
    pair = 0
    while result > -1 and count < len(s):
        if s[count] == '(':
            result = result + 1 
            count = count + 1
            pair = pair + 1
        
        elif s[count] == ')':
            result = result - 1
            count = count + 1
        else :
            count = count + 1

    if result != 0:
        return False
    else :
        return True
        
              
# sum of prime numbers of a list values.
def prime_number(num):
    if num%2==0 and num != 2:
        return False
    elif num%3==0 and num != 3:
        return False
    elif num%5==0 and num != 5:
        return False
    elif num%7==0 and num != 7:
        return False
    else:
        return num

def sumprimes(list_of_number):
    result = 0
    for i in list_of_number:
        if i > 1:
            result = result + prime_number(i)
    return result

print(intreverse(242789))

print(matched("a)*(?"))

print(sumprimes([4,6,15,27]))

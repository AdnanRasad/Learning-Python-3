
#In Java we had to write public class { public static void main(String args[])}} ...for every file...but this is not required in Python...
#To Priny something we had to write: System.out.println("Hey Tukun")...but in Python we write:


print("Hey Tukun")

#No semicolon is required also....but be careful 'print' has all lower case letters...
#Here, we are using Python 3 & in python 3, print() is a function...and thats why there's  brackets & thisbracket is mandatory
# after 'print'..but in python 2 it is not...so if we are using
#python 2 we must be careful while we use print with brackets..
#The print statement has been replaced with a print() function, with keyword arguments to replace most of the special syntax of the old print statement
'''
Python 2:
>>> print "Hello User"
Hello User
>>> answer = 42
>>> print "The answer is: " + str(answer)
The answer is: 42
>>>
It's possible to put the arguments inside of parentheses:
>>> print("Hallo")
Hallo
>>> print("Hallo","Python")
('Hallo', 'Python')
>>> print "Hallo","Python"
Hallo Python
>>>
We can see that the output behaviour changes as well. But more importantly: The output behaviour of version 2.x and version 3.x is different as well, as we can see in the following:
$ python3
Python 3.2.3 (default, Apr 10 2013, 05:03:36)
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello")
Hello
>>> print("Hello","Python")
Hello Python
>>>
'''
#Source: https://www.python-course.eu/print.php


print("Adnan" "Tukun") #Didnot print the space,Same as python 2
print("Adnan", "Tukun")#in python 2 this line printed with the parenthesis and the comma, but here we see python 3 did not print the parenthesis and comma


#So Python 3 puts a space when it sees a comma.(Python 2 does this too)..and for a normal print it would create a newline after it finishes...
print("Adnan", end=" ") #normally python 3 would put a space by seeing comma, so it did it and then it would end and goes to new line but now it wont bcz we use end=" "
print("There are <", 2**32, "> possibilities!", sep=" ")
print("There are <", 2**32, "> possibilities!", sep="")

#INCOMPLETE COULD NOT LEARN NICEYLY
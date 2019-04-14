## Overview of Arrays & Lists

While there is no implementation of Arrays in Python, it is a common in built data structure found in other programming languages, such as C# and Java.  

![image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6NpwpwU0xvTRgGStyLglHSqC731Lk-xfudGBeZhPgDHstqA1T)  
(Credit to https://techspirited.com/types-of-data-structures-in-computer-science-their-applications)  

Arrays are like a line of numbered buckets chained to each other side by side. A big difference between arrays and lists are that while the length of arrays are immutable (cannot change), the length of lists are mutable (can change over time). Since there are no arrays in python, we will focus on lists instead.  

**Lists**

- Assignment: my_list = `['a','b',1,2,True]`  
Just like strings, the index of the first element is 0 and both have similar indexing and slicing properties. 

- Interesting methods:  
  - When you want to initialize an N amount of something in a list (i.e. an array of 6 instances of None)
    Syntax: `[ None for x in range(6) ]`  
    General Syntax: [ something **for** dummy_variable in range(N)]  
    OK technically NOT a method, but its something cool to show off + dont waste time and space writing dumb looking for loops
      
  - When you want to add some items into the end of the list
    Syntax: my_list.append('Pikachu')
    
  - Pretty much every other method is interesting! You can find out more about them by typing "list." in IDLE and pressing tab (hopefully a list of methods will appear). I think Cambridge does not encourage using in-built methods of the in build data structures (e.g. `.sort()` , `.remove()`, `.index()` etc) so I will not go into detail! These are more 'good to know' methods that you **should** use in daily life to make life simpler for yourself but **should not** use in A Levels.

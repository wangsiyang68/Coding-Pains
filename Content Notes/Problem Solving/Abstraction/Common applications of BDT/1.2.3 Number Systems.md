## Overview of Number Systems

Common number systems include binary (base-2), octal (base-8), decimal (base-8) and hexadecimal (base-16).

Sometimes, we will need to convert the same number from a base to a different base. They can be broadly categorized into two scenarios, each with their own method:

*From base 10 to base x*

Given a number n, in base 10:

Steps:
1. While n is not 0,
2. Divide n by x
3. Store the remainder
4. Replace n with the quotient

In order to see why this works, imagine that you are converting a number from decimal to decimal. While in real life you would never need to do so, you would realize that everytime you divide by 10, you are moving from the ones slot of the number to the tens slot of the number, and so on until you have reached zero, which means that your number can be stored using the amount of slots that you have found so far.

*From base x to base 10*

Given a number n, in base x, where x is any integer:

Steps:
1. For each integer in the number, starting from the left:
2. Multiply the integer with base to the power of n (base ** n), where n = 0
3. Add the result to a total sum that is initially 0
4. Increase n by 1

Unanswered Questions:
Why do we need to learn about each representation? Whats so important about them

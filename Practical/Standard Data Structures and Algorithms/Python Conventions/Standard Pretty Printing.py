##Standard Pretty Printing

test = 'Manchester United'
num = 3.14159
##left align
print('{:<40}'.format(test))

##center align
print('{:^40}'.format(test))

##right align
print('{:>40}'.format(test))

##padding with different character
print('{:*^40}'.format(test))

##rounding values up only if it is a floatz
print('{:.3f}'.format(num))
print(round(num,3))

##enter variable in the string
print('{0:{1}<{2}}'.format('a','b',10))

##enter commas every three ints, also the f specifies the extent to which the float is shown
print('${0:,.2f}'.format(123456))

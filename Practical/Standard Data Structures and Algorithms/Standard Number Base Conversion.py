##NOTE: remember to account for negative and larger than base 10 values

#denary to unknown form
def den2unk(den,base):
    num = '0123456789abcdef'
    if den == 0:
        return '0'
    else:
        if den//base == 0:
            return num[den%base]
        else:
            return den2unk(den//base, base) + num[den%base]
        
print('Denary Number 102 in binary is ' + str(den2unk(102,2)))
print('Denary Number 3544 in hexadecimal is ' + str(den2unk(3544,16)))

#unknown to denary form
def unk2den(num,base): #recursive version but super unreadable
    if num == 0:
        return 0
    return unk2den(num%(10**(len(str(num))-1)),base) + num//(10**(len(str(num))-1))*(base**(len(str(num))-1))

print('Octal Number 12341234 in denary form is ' + str(unk2den(12341234,8)))

def iterative(num,base): #iterative version, more readable and intuitive
    power = 0
    total = 0
    for i in str(num)[::-1]:
        total += int(i)*base**power
        power += 1
    return total

print('Octal number 1451 in denary form is ' + str(iterative(1451,8)))

#unknown to unknown form
def unk2unk(num,base,new_base):
    return den2unk(unk2den(num,base),new_base)

print('Binary Number 1010011100101101 (42797) in hexadecimal is ' + str(unk2unk(1010011100101101,2,16)))

def converter(DenaryNumber, binary = ''):
    if DenaryNumber == 0 or DenaryNumber == 1:
        return str(DenaryNumber) + binary
    else:
        binary = str(DenaryNumber%2) + binary
        return converter(DenaryNumber//2,binary)

print(converter(56))

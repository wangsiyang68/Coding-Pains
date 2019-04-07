while True:
    try:
        answer = int(input("What is : " + \
                           str(9) + ' - ' + str(1) + ' = '\
                           " equal to? "))
        break
    except ValueError:
        print('Illegal value; please enter a number!')
    except:
        print('lmao')

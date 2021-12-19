# FMC_2 ver 1.5

# MULTI VARIABLE SUPPORT STILL TO BE IMPLEMENTED

# VARIABLE IN PLACE OF DIVISOR SOLVED MANY TIMES GIVES WRONG ANSWERS

# author Murtuza Attarwala


INTEGERS = list('1234567890')
OPERATORS = list('+-*/=')
toFind = list('ZXCVBNMLKJHGFDSAPOIUYTREWQqwertyuiopasdfghjklzxcvbnm')

def main():
    string = input('>')
    if string == '-i':
        manual()
    else:
        parser(string)

def manual():
    m = open('FMC2_MANUAL.fmc','r')
    print(m.read())
    m.close
def spaceRemover(string):
    lstring = list(string)
    stringSize = len(string)
    fstring = []
    i = 0
    while i < stringSize:
        if lstring[i] == ' ':
            i = i + 1
        else:
            fstring.append(lstring[i])
            i = i + 1
    return ''.join(fstring)

def process(num, result):
    lnum = list(num)
    sign = num[0]
    numSize = len(num)
    num = float(''.join(lnum[1:numSize]))
    if sign == '+':
        result = result - num
    elif sign == '-':
        result = result + num
    elif sign == '*':
        result = result / num
    elif sign == '/':
        result = result * num
    return result

def Result(result):
    res = list(str(result))
    if res[-1] == '0':
        result = int(result)
        return result
    else:
        return result

def parser(string):
    lstring = list(spaceRemover(string))
    stringSize = len(lstring)
    if lstring[0] not in OPERATORS:
        lstring.insert(0, '+')
    stringSize = len(lstring)
    startPoint = 0
    endPoint = 0
    middle = 0
    varDivide = 0
    fstring = []
    var = ''
    result = 0.0
    i = 0
    while i < stringSize:
        if i == 0 and lstring[1] not in toFind:
            startPoint = 0
        if lstring[i] == '=':
            middle = i
            break
        elif lstring[i] in OPERATORS and (lstring[i-1] in INTEGERS or lstring[i-1] in toFind) and lstring[i+1] not in toFind:
            startPoint = i
        if lstring[i] in INTEGERS and lstring[i+1] in OPERATORS:
            endPoint = i
            fstring.append(''.join(lstring[startPoint:endPoint+1]))
        if lstring[i] in toFind:
            var = lstring[i]
            varSign = lstring[i-1]
            if varSign == '*':
                num = list(fstring[-1])
                num[0] = '*'
                fstring[-1] = ''.join(num)
            elif varSign == '/':
                varDivide = 1
                numerator = fstring[-1]
                lnum = list(numerator)
                lnum.pop(1)
                numerator == ''.join(lnum)
                fstring[-1] = '!'
        i = i + 1
    fstring.reverse()
    #if varDivide == 1:
        #result = float(numerator)/float(''.join(lstring[middle+1:stringSize]))
    #else:
    rhs = ''.join(lstring[middle+1:stringSize])
    result = float(rhs)
    i = 0
    if len(fstring) != 0:
        while i < len(fstring):
            if varDivide == 1 and fstring[i] == '!':
                result = float(numerator)/float(result)
            else:
                result = process(fstring[i], result)
            i += 1
    if varSign == '-':
        result = -(result)
    result = Result(result)
    print(var + ' = ' + str(result))
    return 0

infinity = 0
print('Fission Model Calculator 2 -Alpha ver 1.5')
print('_Developed and Implemented by Murtuza Attarwala')
print('i)\'-i\' for instructions')
print('')
while infinity == 0:
    main()
    print('')
        

def sumAll(*Values):
    return sum(Values)


def timesAll(*Values):
    answer = 1
    for i in Values:
        answer *= i
    return answer

'''
x = sumAll(3,4,2)
y = timesAll(2,3,4)
print(f'The value of x= {x} and y= {y}')
'''
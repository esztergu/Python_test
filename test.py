def Task_4(n):
    def my_func(n):
        print "original n: ", n
        last_digit = n % 10
        print "last digit: ", last_digit
        n = n + (10 - last_digit)
        print "new n:", n
        return n

    my_func(n)

def solution_4(N):
    print "Task 4"
    Task_4(N)
    pass



def string_to_number(string):
    switcher = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        }
    return switcher.get(string)

def solution_5(D,S):
    print "Task 5"

    if D >= 1 and D <= 5:
        print D * string_to_number(S)
    else:
        print('D is out of range')
        pass
    pass



def Task_6(N):
    print "Task 6"

    def my_func(n):
        my_array = []
        i = 1
        while i <= n // 2:
            my_array.append(i)
            my_array.append(-i)
            i += 1
        if n % 2:
            my_array.append(0)
        print "n: ", n
        print "length: ", len(my_array)
        print "sum: ", sum(my_array)
        print my_array
        return my_array

    my_func(N)

def Task_6_extra(N):
    # sum is N not zero
    print "Task 6 extra"

    def my_func(n):
        my_array = []
        i = 1
        if n % 2:
            print "odd number"
            while i <= n // 2:
                my_array.append(i)
                my_array.append(-i)
                i += 1
        else:
            print "even number"
            while i <= n // 2 - 1:
                my_array.append(i)
                my_array.append(-i)
                i += 1
            my_array.append(0)
        my_array.append(n)
        print "n: ", n
        print "length: ", len(my_array)
        print "sum: ", sum(my_array)
        print my_array
        return my_array

    my_func(N)

def solution_6(N):
    Task_6(N)
    Task_6_extra(N)
    pass



solution_4(169775)
solution_4(999999999)
# solution_5(4, "two")
# solution_5(3, "six")
# solution_6(76)


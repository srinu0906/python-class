# def add(a,b):
#     res = a+b
#     return res

# def add1(a,b):
#     res = a+b
#     print(res)

# def add2():
#     res = 1+2
#     return res

# def say_hi():
#     print("hi")

# c = add(1,2)

# types of functions
# 1. with arg and with return


def is_eligible_to_vote(age):
    if(age >= 18):
        return True
    else:
        return False

age = int(input("enter age"))

print(is_eligible_to_vote(age))
import  os

def reverse_int(num):
    remainder = 0
    revers_int=0

    while num>0:
        remainder = num %10

        num = num //10

        revers_int= revers_int *10 + remainder


    return revers_int

if __name__ == '__main__':
    print(reverse_int(1234))
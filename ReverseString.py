import os, sys


def reverse(data):
    print(data[::-1])


def is_palindrome(data):
    reversed_string = reverse_manually(data)
    print(f"reverse string is {reversed_string}")
    if data == reversed_string:
        return True
    else:
        return False


def reverse_manually(data):
    print(list(data))
    lst_string = list(data)
    start_item = 0
    end_item = len(data) - 1
    while end_item > start_item:
        lst_string[start_item], lst_string[end_item] = (
            lst_string[end_item],
            lst_string[start_item],
        )

        # print(f"end_item {end_item} ,start item {start_item}")
        end_item = end_item - 1
        start_item = start_item + 1

    return "".join(lst_string)


if __name__ == "__main__":
    reverse("calculator")
    print(is_palindrome("hello"))
    print(is_palindrome("madam"))

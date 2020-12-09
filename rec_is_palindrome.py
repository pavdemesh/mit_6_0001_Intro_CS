def strip_but_letters(text):
    """Function takes a string as argument and returns
    the same string in lowercase without spaces and punctuation"""
    res = ""
    for char in text.lower():
        if char.isalpha():
            res += char
    return res


def is_palindrome(text):
    """Function takes as input a lowercase string consisting only of letters
    Returns True if the string is a palindrome and False otherwise"""
    if len(text) == 1 or len(text) == 0:
        return True
    else:
        return text[0] == text[-1] and is_palindrome(text[1:-1])


test = 'AtbbArraBBta'
print(is_palindrome(strip_but_letters(test)))

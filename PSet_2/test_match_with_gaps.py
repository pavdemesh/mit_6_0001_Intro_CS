def match_with_gaps(my_word, other_word):
    i = 0
    res = ''

    while i < len(my_word):
        if my_word[i].isalpha():
            res += my_word[i]
            i += 1
        else:
            res += '*'
            i += 2

    return res


print(match_with_gaps("pom_ dor_ ", 'kasa'))

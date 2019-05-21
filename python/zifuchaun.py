def is_reverse(word1, word2) :
    if len(word1) != len(word2) :
        return False

    i = 0
    j = len(word2)

    while j > 0 :
        print(i, j-1)
        if word1[i] != word2[j - 1] :
            return False
        i = i + 1
        j = j - 1

    return True


def count(str, char) :
    count = 0
    i = 0
    while i < len(str) :
        if str[i] == char :
            count = count + 1
        i = i + 1
    print(count)
             

count('banbana', 'a')
is_reverse('pots', 'stop')


def duplicate_encode(word):
    dic= {}
    for char in word:
        if char.lower() not in dic:
            dic[char.lower()] = 1
        else:
            dic[char.lower()] +=1
    for char in word:
        if dic[char.lower()] == 1:
            new += '('
        else:
            new += ')'
        return new

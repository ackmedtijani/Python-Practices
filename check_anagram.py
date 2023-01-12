def anagram(s1 , s2):
    check = 0
    for i in s1:
        for j in s2:
            if i in [" ",",","'","\"","\n","\t"]:
                continue
            if i == j:
                check = 1
        if check == False:
            return False
    return True


    
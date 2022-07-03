



def nestedlists(name, score):
    dic = {}
    s = list()
    if score in dic:
        dic[score].append(name)
    else:
        dic[score] = [name]

    s.append(score)
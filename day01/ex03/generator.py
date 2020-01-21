from secrets import randbelow
import datetime

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    tmp = ""
    lst = []
    modlist = []

    for letter in text:
        if letter != sep:
            tmp += letter
        else:
            lst.append(tmp)
            tmp = ""
    lst.append(tmp)

    if option == "shuffle":
        while len(lst) > 0:
            rand = datetime.datetime.now().microsecond % len(lst)
            modlist.append(lst[rand])
            lst.pop(rand)
        return modlist
    elif option == "ordered":
        lst.sort(reverse=True)
        return lst
    else:
        return lst

for ele in generator("Le Lorem Ipsum est simplement du faux texte.", sep=" ", option="shuffle"):
    print(ele)

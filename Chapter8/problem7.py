# write a program to remove a given list word and strip it at the same time

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
        return n
    

l = ["Vaishu", "Rohan", "Harry"]

print(rem(l, "an"))
#!/usr/bin/pytjon3
def search_replace(my_list, search, replace):
    rep = my_list[:]
    for idx, n in enumerate(rep):
        if n == search:
            rep[idx] = replace
    return rep

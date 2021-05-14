def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """

    if len(arrivals) % 2:
        if name in arrivals[len(arrivals) // 2:] and name != arrivals[-1]:
            return True
        else:
            return False
    else:
        if name in arrivals[len(arrivals)//2-1:] and name != arrivals[-1]:
            return True
        else:
            return False


first = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
second = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford', 'Alex']

print(fashionably_late(second, 'Adela'))
print(fashionably_late(second, 'Fleda'))
print(fashionably_late(second, 'Owen'))
print(fashionably_late(second, 'May'))
print(fashionably_late(second, 'Mona'))
print(fashionably_late(second, 'Gilbert'))
print(fashionably_late(second, 'Ford'))
print(fashionably_late(second, 'Alex'))

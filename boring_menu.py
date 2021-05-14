def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """

    for meal in range(len(meals) - 1, 0, -1):
        if meals[meal] == meals[meal - 1]:
            return True


    return False


stuff = ['Spam', 'Spam']

print(menu_is_boring(stuff))


def set_initial(name):
    if len(name) >= 5:
        initials = name[0].upper() + '. '
        return initials
    else:
        return name


def get_initials(name):
    return name


print("Working with Name Attributor!")
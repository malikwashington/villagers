from collection import defauldict
"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    
    species = set()
    
    file = open(filename)
    
    for line in file:
        words = line.strip().split("|")
        species.add(words[1])

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []


    file = open(filename)
    for line in file:
        words = line.strip().split("|")
        if search_string.lower() == 'all':
          villagers.append(words[0])
        elif search_string == words[1]:
          villagers.append(words[0])
          

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    hobbies = defauldict(list)
    file = open(filename)
    order = ['Fitness', 'Nature', 'Education', 'Music', 'Fashion', 'Play']
    for line in file:
        words = line.strip().split("|")
        hobbies[words[-2]] = words[0]
    return [sorted(hobbies[hobby]) for hobby in order]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    
    file = open(filename)
    all_data = []

    for line in file:
        words = line.strip().split("|")
        all_data.append(tuple(words)) 

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    file = open(filename)
    
    for line in file:
        words = line.strip().split("|")
        if words[0] == villager_name:
          return words[-1]
    return None


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    file = open(filename)
    personality = ''
    personality_set = set()

    # find personailty of villager:
    #   for loop name return personality variable that matches the villager name
    for line in file:
        words = line.strip().split("|")
        if villager_name in words:
            personality = words[2]
            break
    # find all lines that match personality:
    #   for loop  set.add names who match personality and are not the villager
    for line in file:
        words = line.strip().split("|")
        if personality in words and villager_name not in words:
            personality_set.add(words[0])


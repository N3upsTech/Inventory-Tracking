""" Database module for Inventory Track project. """


DATA = {}
DATABASE_NAME = None

def initialise(database_name):
    global DATABASE_NAME
    DATABASE_NAME = database_name 


def add(category, value):
    """ Add stuff to database. """
    global DATA
    DATA[category] = value


def save():
    """ Write the value of the category to the database. """
    global DATABASE_NAME
    global DATA

    database = open(DATABASE_NAME + ".database", 'w')
    for key in DATA.keys():
        # For every key in dictionary
        database.write(key + "=" + str(DATA[key]) + "\n")
    database.close()


def read(category):
    """ Read the value of category from the database. """
    global DATABASE_NAME
    global DATA
    
    # Read from file
    database = open(DATABASE_NAME + ".database")
    lines = database.readlines()
    # Rest the DATA
    DATA = {}
    for line in lines:
        key, value = line.split("=") # split on '=' sign
        DATA[key] = int(value)
    # Get the value and return
    if category in DATA.keys():
        return DATA[category]
    else:
        # Did not found
        return 0


def update(category, value):
    """ Update the value in the database. """
    global DATA
    if category in DATA.keys():
        # If the category exists in database
        DATA[category] = value
    else:
        print("[-] Failed to update database.")
        print(f"[-] Can not find '{category}'")
#lab 7-7

rows = [
    ["Darick", "Eugene", "Kyle", "Azaan"],
    ["Ryan", "Phil", "Eman", "Alex", "Nicholas"],
    ["Christian", "Josh", "Matt", "Francesco"],
    ["Patrick", "Nico", "Trevayne"]
]

def print_possessive_names(rows):
    """
    Function to print each person's name in possessive form.
    If a name ends with 's', add only an apostrophe.
    Otherwise, add "'s".
    """
    for row in rows:  
        for name in row: 
            
            if name.endswith('s'):
                print(f"{name}'")
            else:
                print(f"{name}'s")


print_possessive_names(rows)

from fuzzywuzzy import fuzz

n1 = ['SmithJohnson', 'WilliamsBrown', 'GarciaJones']
n2 = ['GarciaJones', 'WilliamsBrown', 'SmithJohnson']

def fuzzy_wuzzy(lst1, lst2):
    """If the names are equal but in different order in the lists."""
    print('')
    for x in lst1:
        for y in lst2:
            if fuzz.ratio(x, y) == 100:
                print(f'Match - {x} = {y} = {fuzz.ratio(x,y)}')


fuzzy_wuzzy(n1, n2)
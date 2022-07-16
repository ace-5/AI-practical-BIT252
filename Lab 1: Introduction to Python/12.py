# WAP to find the sum of all items in a dictionary

def get_items_sum(dict):
    print('Input:', dict)
    print('Output:', sum(dict.values()))

input1 = {
    'a': 100, 
    'b':200, 
    'c':300
    }
input2 = {
    'x': 25, 
    'y':18, 
    'z':45
    }

get_items_sum(input1)
get_items_sum(input2)
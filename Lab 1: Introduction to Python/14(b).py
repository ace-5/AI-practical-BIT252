# WAP to represent the following graphs using a dictionary
# Biratnagar -> (Itahari, 22), (Biratchowk, 30), (Rangeli, 25)
# Itahari -> (Biratnagar, 22), (Dharan, 20), (Biratchowk, 11)
# Biratchowk -> (Biratnagar, 30), (Itahari, 11), (Kanepokhari, 10)
# Rangeli -> (Biratnagar, 25), (Kanepokhari, 25), (Urlabari, 40)
# Kanepokhari -> (Rangeli, 25), (Urlabari, 22), (Biratchowk, 10)
# Urlabari -> (Kanepokhari, 12), (Damak, 6), (Rangeli, 40)

routes_with_distance_in_kms = {
    'Biratnagar': {
        'Itahari': 22,
        'Biratchowk': 30,
        'Rangeli': 25
    },
    'Itahari': {
        'Biratnagar': 22,
        'Dharan': 20,
        'Biratchowk': 11
    },
    'Biratchowk': {
        'Biratnagar': 30,
        'Itahari': 11,
        'Kanepokhari': 10
    },
    'Rangeli': {
        'Biratnagar': 25,
        'Kanepokhari': 25,
        'Urlabari': 40
    },
    'Kanepokhari':{
        'Rangeli': 25,
        'Urlabari': 22,
        'Biratchowk': 10
    },
    'Urlabari': {
        'Kanepokhari': 12,
        'Damak': 6,
        'Rangeli': 40
    }
}


trees = {

    'brzoza': {
        'symbol': 'B',
        'probability': 30
        }, 

    'dab': {
        'symbol': 'D',
        'probability': 20
        }, 

    'swierk': {
        'symbol': 'S',
        'probability': 10
        },
    }


mushrooms = {

    'maslak': {
        'symbol': 'm',
        'probability': 30,
        'type': 'amanita',
        'poisonous': 'no',
        'color': 'light brown',
        'shape': 'cap',
        'stipe': 'plain',
        'tastiness': 5,
        'favorite_tree': 'brzoza'
        }, 

    'pieprznik': {
        'symbol': 'p',
        'probability': 15,
        'type': 'cantharellaceae',
        'poisonous': 'no',
        'color': 'yellow',
        'shape': 'cone',
        'stipe': 'rugged',
        'tastiness': 10,
        'favorite_tree': 'brzoza'
        },

    'muchomor czerwony': {
        'symbol': 'h',
        'probability': 15,
        'type': 'amanita',
        'poisonous': 'yes',
        'color': 'red',
        'shape': 'cap',
        'stipe': 'dotted',
        'tastiness': 0,
        'favorite_tree': 'swierk'
        },

    'czubajka kania': {
        'symbol': 'c',
        'probability': 10,
        'type': 'macrolepiota',
        'poisonous': 'no',
        'color': 'white',
        'shape': 'cap',
        'stipe': 'dotted',
        'tastiness': 20,
        'favorite_tree': 'brzoza'
        },

    'lysiczka lancetowata': {
        'symbol': 'l',
        'probability': 5,
        'type': 'psilocybe',
        'poisonous': 'no',
        'color': 'brown',
        'shape': 'cone',
        'stipe': 'plain',
        'tastiness': 50,
        'favorite_tree': 'dab'
        },

    'muchomor sromotnikowy': {
        'symbol': 's',
        'probability': 15,
        'type': 'amanita',
        'poisonous': 'yes',
        'color': 'yellow',
        'shape': 'cap',
        'stipe': 'plain',
        'tastiness': 0,
        'favorite_tree': 'swierk'
        },

    'uszak gestowlosy': {
        'symbol': 'u',
        'probability': 10,
        'type': 'amanita',
        'poisonous': 'no',
        'color': 'brown',
        'shape': 'cap',
        'stipe': 'plain',
        'tastiness': 40,
        'favorite_tree': 'dab'
        },
    }


ground = {

    'trawa': {
        'symbol': '.', 
        },

    'mech': {
        'symbol': '+',
        'probability': 60
        }
    }
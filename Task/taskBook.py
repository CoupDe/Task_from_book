import json

mydiscription = {
    'name': {'firstname': 'Artem',
             'lastname': 'Troychenko',
             'patronymic': 'Sergeevich'
             },
    'age': {'birthday': '14/11/1985',
            'age': 35
            },
    'family': {
        'wife': {
            'firstname': 'Daria',
            'lastname': 'Alekseeva',
            'patronymic': 'Sergeevna'
        },
        'age': {'birthday': '21/12/1991',
                'age': 29
                },
        'child': {
            'firstname': 'Eva',
            'lastname': 'Troychenko',
            'patronymic': 'Artemovna'
        },
        'child_age': {'birthday': '12/07/2019',
                      'age': 1
                      },
    }
}

with open('mydb.json', 'w') as write_json:
    json.dump(mydiscription, write_json, indent=4)

with open('mydb.json', 'r') as read_json:
    dt = json.load(read_json)

print('Name-{0}, Lastname {1}\nWife-{2} {3}\nChildren-{4} {5} Birthday {6}' .format(dt['name']['firstname'], dt['name']['lastname'],
                                                dt['family']['wife']['firstname'],dt['family']['wife']['lastname'],
                                                dt['family']['child']['firstname'],
                                                dt['family']['child']['lastname'], dt['family']['child_age']['birthday']))

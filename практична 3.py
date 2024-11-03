dictionary = { 'name': 'Danilo',
            'age': 16,
            'dict': {'1': 'nxdannik',
                    '2': 'nx',
                    '3': 5.18,
                    '4': "papu",
                    '5': "pupu"},
            'true': 'false',
            }
print(dictionary)

type_dict = {}
for key, value in dictionary.items():
    if type(value) == dict:
        for k1, v1 in value.items():
            type_dict[k1] = type(v1)
    else:
        type_dict[key] = type(value)
print(type_dict)
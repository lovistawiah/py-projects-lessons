people = [
    {"name": "Lovis", "house": "Tano"},
    {"name": "Sandra", "house": "Volta"},
    {"name": "Ron", "house": "Nkrumah"}
]

# use to compare and return value in alphabetical descending order

# def f(person):
#     return person["house"]


people.sort(key=lambda person: person["name"])

print(people)

# Dictionary method

dict = {
    45: 68,
    46: 86
}

print(dict)

dict[45] = 89

print(dict)

del dict

print(dict)

dict2 = {}

print(dict2)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f"What is your {q}? It is {a}")

dict2[1] = 48
dict2[2] = 65

del dict2[2]

print(dict2)
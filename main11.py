import pprint

cook_book = {}
some_list = []
with open('recept.txt', 'r', encoding='UTF-8') as f:
    data = f.read().split('\n\n')
    for food in data:
        some_list = []
        key = food.split('\n')[0]
        ingridients = food.split('\n')[2:]
        for ingridient in ingridients:
            ingridient_1 = ingridient.split('|')
            ingrigients_dict = {'ingredient_name':ingridient_1[0], 'quantity':ingridient_1[1], 'meansure':ingridient_1[2]}
            some_list.append(ingrigients_dict)    
        cook_book[key] = some_list

pprint.pprint(cook_book, width=100)
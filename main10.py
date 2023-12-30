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
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['meansure']))




def get_cook_book_with_quantity(path):
    cook_book = {}
    with open(path, encoding='utf-8') as f:
        while True:
            name = f.readline().strip()
            if not name:
                break
            count = int(f.readline().strip())
            cook_book[name] = []
            line = f.readline().strip()
            while line:
                ingredients = line.split(" | ")
                ingredients_dict = {"ingredient_name": ingredients[0],
                                    "quantity": int(ingredients[1]),
                                    "meansure": ingredients[2]}
                cook_book[name].append(ingredients_dict)
                line = f.readline().strip()

    return cook_book


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    cook_book = get_cook_book_with_quantity("recept.txt")
    shop_list = get_shop_list_by_dishes(cook_book, person_count)
    print_shop_list(shop_list)


create_shop_list()


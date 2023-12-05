  
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
 
def split_text(text):
    return [i.splitlines() for i in text.split('\n\n')]
 
def split_ingredients_data(lst):
    return lst[:1] + [i.replace(' ', '').split('|') for i in lst[2:]]
 
def lst_to_dict(lst):
    return {lst[0]: [{'ingredient_name': i[0], 'quantity': int(i[1]), 'measure': i[2]} for i in lst[1:]]}
 
def data_loads(file_path):
    out = {}
    text = read_file(file_path)
    dish_list = split_text(text)
    format_dish_list = [split_ingredients_data(i) for i in dish_list]
    for i in format_dish_list:
        out.update(lst_to_dict(i))
    return out
 
res = data_loads('recept.txt')
 
print(res)
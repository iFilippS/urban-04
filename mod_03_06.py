
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(structure):

    score = 0
    
    # если список, кортеж, словарь или множество
    if isinstance(structure, list | tuple | set | dict):
        
        # перобразуем словарь в список
        if isinstance(structure, dict):
            structure = list(structure.items())

        # перебираем список, кортеж или множество
        for item in structure:
            # используем рекурсию
            score += calculate_structure_sum(item)
    
    # если строка
    if isinstance(structure, str):
        score = len(structure)
    
    # если число
    if isinstance(structure, int):
        score = structure

    return score

print(data_structure)
result = calculate_structure_sum(data_structure)
print(result)

def index_r(p1, p2, p3):                    #индекс
    return (4 * (int(p1) + int(p2) + int(p3)) - 200) / 10

def low_coast(age):          
    a = (min(int(age), 15) - 7) // 2             #в каком столбце (4, 3, 2, 1, 0)
    low = 21 - 1.5 * a
    return low

def strokes(index, low):
    if index >= low:
        return 0
    if index >= low - 4:
        return 1
    if index >= low - 5:
        return 2
    if index >= low - 5.5:
        return 3
    return 4

def compare(p1, p2, p3, age):
    if int(age) < 7:
        return 'не найден', 'невозможно расчитать'
    index = index_r(p1, p2, p3)
    low = low_coast(age)
    stroke = strokes(index, low)
    return index, txt_res[stroke]

txt_res = []
txt_res.append('''низкая.
Срочно обратитесь к врачу!''')
txt_res.append('''удовлетворительная.
Обратитесь к врачу!''')
txt_res.append('''средняя.
Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''
выше среднего''')
txt_res.append('''
высокая''')
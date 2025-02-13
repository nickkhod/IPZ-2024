def process_string():
    s = input("Введіть текст: ")
    v = "аоуеиіАОУЕІИaeiouAEIOU"
    c = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгґджзклмнпрстфхцчшщБВГҐДЖЗКЛМНПРОТФХЦЧШЩ"
    vowels = "".join(sorted([ch for ch in s if ch in v], reverse=True))
    consonants = "".join(sorted([ch for ch in s if ch in c], reverse=True))
    more_consonants = len(consonants) > 3
    return (vowels, more_consonants, consonants)

result = process_string()
print(result)

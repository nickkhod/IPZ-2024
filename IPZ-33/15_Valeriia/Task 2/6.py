def number(n):  # create lists for verbal representations of ones, tens, and hundreds
    ones = ["", "один", "два", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять", "десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п'ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять", "дев'ятнадцять"]
    tens = ["", "", "двадцять", "тридцять", "сорок", "п'ятдесят", "шістдесят", "сімдесят", "вісімдесят", "дев'яносто"]
    hundreds = ["", "сто", "двісті", "триста", "чотириста", "п'ятсот", "шістсот", "сімсот", "вісімсот", "дев'ятсот"]
    
    if n == 1000:
        return "тисяча"
    
    result = []
    
    result.append(hundreds[n // 100])  # Process the hundreds
    n %= 100
    
    if n < 20:  # Process tens and ones
        result.append(ones[n])
    else:
        result.append(tens[n // 10])
        result.append(ones[n % 10])
    
    return ' '.join([word for word in result if word])  # Filter out empty elements and join

n = int(input("Число: "))
print("Слово:", number(n))

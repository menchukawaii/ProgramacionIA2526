## numeros primos

def es_primo(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False     
    else:
        return False

    return True

print(es_primo(19500))

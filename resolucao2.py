mainString = print(input('Digite seu texto:'))

def replaceMultiple(string_principal, substituir, newString):
    for elem in substituir:
        if elem in string_principal:
            string_principal = string_principal.replace(elem, newString)

    return string_principal

print(string_principal)



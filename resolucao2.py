mainString = print(input('Digite seu texto:'))

def replaceMultiple(string_principal, substituir, nova_string):
    for elemento in substituir:
        if elemento in string_principal:
            string_principal = string_principal.replace(elemento, nova_string)

    return string_principal

print(string_principal)



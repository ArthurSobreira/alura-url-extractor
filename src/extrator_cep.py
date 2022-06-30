import re  # Regular Expression -- RegEx

endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'

# 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile('[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]')
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)

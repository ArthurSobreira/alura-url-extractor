url = 'https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

# Separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

# Busca o valor de um parâmetros
url_parametros = url[(indice_interrogacao+1):]
print(url_parametros)

parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + (len(parametro_busca) + 1)
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)

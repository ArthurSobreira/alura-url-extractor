from re import compile


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'{self.url}\nParâmetros: {self.get_url_parametros()}\nURL Base: {self.get_url_base()}'

    def __eq__(self, other):
        return self.url == other.url

    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao_url = compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é válida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[(indice_interrogacao + 1):]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + (len(parametro_busca) + 1)
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def converter_moeda(self):
        valor_dolar = 5.2
        valor_convertido = int(self.get_valor_parametro('quantia')) / valor_dolar
        return round(valor_convertido, 2)


if __name__ == '__main__':
    extrator_url = ExtratorURL('https://bytebank.com/cambio?quantia=100&moedaDestino=dolar&moedaOrigem=real')
    valor_quantidade = extrator_url.get_valor_parametro('quantia')
    print(valor_quantidade)
    print(extrator_url)
    print(len(extrator_url))
    print(extrator_url.converter_moeda())

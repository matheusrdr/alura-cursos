import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.limpa_url(url)
        self.valida_url()

    def limpa_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL informada é vazia.")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        index_interrogacao = self.url.find('?')
        url_base = self.url[:index_interrogacao]
        return url_base

    def get_url_parametros(self):
        index_interrogacao = self.url.find('?')
        url_parametros = self.url[index_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro):
        index_parametro = self.get_url_parametros().find(parametro)
        index_valor = index_parametro + len(parametro) + 1
        indice_e_comercial = self.get_url_parametros().find('&', index_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[index_valor:]
        else:
            valor = self.get_url_parametros()[index_valor:indice_e_comercial]
        return valor

    # Métodos especiais:
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
#url = "matheus"
extrair_url = ExtratorURL(url)
valor_parametro = extrair_url.get_valor_parametro("moedaDestino")
print(valor_parametro)

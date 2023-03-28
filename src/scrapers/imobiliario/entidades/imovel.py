class Imovel:

    def __init__(self, 
                 descricao, 
                 preco, area, quartos, link, site, id_site="", nome="", 
                 valor_condominio="", valor_iptu="", banheiros="", 
                 vagas_garagem="", endereco="", edificio=""):

        # Atributos obrigatórios
        if not descricao or not preco or not area or not quartos or not link or not site:
            raise ValueError(
                'Todos os atributos obrigatórios devem ser fornecidos')

        self.descricao = descricao
        self.preco = preco
        self.area = area
        self.quartos = quartos
        self.link = link
        self.site = site

        # Atributos opcionais
        self.id_site = id_site
        self.nome = nome
        self.valor_condominio = valor_condominio
        self.valor_iptu = valor_iptu
        self.banheiros = banheiros
        self.vagas_garagem = vagas_garagem
        self.endereco = endereco
        self.edificio = edificio

    def __str__(self) -> str:
        print("Detalhes do imovel: ")
        print(f"Id Zap Imoveis: {self.id_site}")
        print(f"Descricao: {self.descricao}")
        print(f"Preço: {self.preco}")
        print(f"Área: {self.area}")
        print(f"Quartos: {self.quartos}")
        print(f"Link: {self.link}")        
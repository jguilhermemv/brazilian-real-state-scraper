from enum import Enum

class ImovelXPaths(Enum):
    STATUS = '//*[@class="color-white text-small text-small__bolder label__container background-color-progress-2"]//strong'
    ENDERECO = '//span[@class="link"]'
    PRECO = '//*[contains(@class, "price__item--main")]//strong'
    AREA = '//span[@itemprop="floorSize"]'
    QUARTOS = '//span[@itemprop="numberOfRooms"]'
    VAGAS = '//*[@class="feature__item text-regular js-parking-spaces"]/span[2]'
    BANHEIROS = '//span[@itemprop="numberOfBathroomsTotal"]'
    DESCRICAO = '//div[contains(@class, "amenities__description")]'
    EDIFICIO = '//ul[@class="subinfo"]/li/'
    CONDOMINIO = '//li[@class="price__item condominium color-dark text-regular"]/span'
    IPTU = '//li[@class="price__item iptu color-dark text-regular"]/span'
    ANDAR = '//span[@itemprop="floorLevel"]'

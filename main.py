import time
import re
from src.util.arquivos import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from src.scrapers.imobiliario.entidades.imovel import Imovel
from src.scrapers.imobiliario.constantes.atributos_imovel_xpaths import ImovelXPaths
from src.util.logging_util import get_logger

logger = get_logger()
inicio = time.time()
# Define as opções do navegador
chrome_options = Options()
chrome_options.add_argument("--headless")  # Inicia em formato headless

# Inicia o navegador
driver = webdriver.Chrome(options=chrome_options)

# Acessa a página do Zap Imóveis
url = "https://www.zapimoveis.com.br/venda/apartamentos/pe+recife++poco/?pagina2000&?tipos=apartamento_residencial&transacao=vendal&onde=,Pernambuco,Recife,,Poço,,,,BR>Pernambuco>NULL>Recife>Barrios>Poco"
driver.get(url)


# Verifica se houve um erro ao acessar a página
if "404" in driver.title:
    print("Erro 404: Página não encontrada")
    logger.error(f"Erro 404: Página inicial {url} não encontrada")
    raise RuntimeError("Erro 404: Página inicial {url} não encontrada")    
else:
    time.sleep(2)  # Espera 2 segundos para carregar a página completamente
    
    url_janela_inicial = driver.current_url
    print(f"Pagina Inicial: {url_janela_inicial}\n")
    # Remove o elemento com a classe "cookie-notifier"
    driver.execute_script("document.getElementsByClassName('cookie-notifier')[0].style.display = 'none';")
    
    # Localiza os elementos div com as classes "card-container js-listing-card" e "card-listing simple-card"
    lista_imoveis = driver.find_elements(By.XPATH, "//div[@class='card-container js-listing-card']//div[@class='card-listing simple-card']")

    #Itera sobre a linhas de imóveis encontradas para o bairro especificado
    for i, imovel in enumerate(lista_imoveis):       
       
        #Clica no imóvel da vez, que vai abrir uma nova aba/janela       
        driver.execute_script("arguments[0].click();", imovel)
        
        time.sleep(1)  # Espera 3 segundos para carregar a página completamente
        
        # Muda o controle para a nova janela/aba do imovel clicado
        driver.switch_to.window(driver.window_handles[-1])
        
        # Pega a URL da nova janela
        url_nova_janela = driver.current_url       
        
        # Verifica se realmente mudou de janela
        if url_nova_janela == url_janela_inicial:
            raise RuntimeError("Não foi possível mudar de janela.") 
        else:
            
            print(f"{i+1} - {url_nova_janela}")
            try:         
                #close-button-1545222288830       
                ## Processa aqui a pagina do imovel e coleta informacoes        
                data_id = re.search(r"id-(\d+)/", url_nova_janela).group(1)
                descricao = driver.find_element(By.XPATH, ImovelXPaths.DESCRICAO.value)
                descricao = descricao.text
                descricao = descricao.replace("\n", "")
                preco = driver.find_element(By.XPATH, ImovelXPaths.PRECO.value).text
                preco = re.search(r'R\$ (\d+)\.(\d+)', preco).group(1) + re.search(r'R\$ (\d+)\.(\d+)', preco).group(2)
                area = driver.find_element(By.XPATH, ImovelXPaths.AREA.value).text.replace(" m²", "").strip()
                quartos = driver.find_element(By.XPATH, ImovelXPaths.QUARTOS.value).text.replace(" quartos", "").strip()
                link = url_nova_janela
                imovel_entidade = Imovel(descricao=descricao, preco=preco, area=area, quartos=quartos, link=link, site="Zap Imoveis", id_site=data_id)
                adicionar_objeto_a_arquivo_csv(imovel_entidade, "imoveis")
                print(imovel)
            except Exception as e:
                html = imovel.get_attribute("outerHTML")
                escrever_html(html, f"html/{data_id}-error.html")
                logger.error(e)
            
            # print("Detalhes do imovel: ")
            # print(f"Id Zap Imoveis: {data_id}")
            # print(f"Descricao: {descricao}")
            # print(f"Preço: {preco}")
            # print(f"Área: {area}")
            # print(f"Quartos: {quartos}")
            # print(f"Link: {link}")
            
            # Fecha a nova janela
            driver.close()
            
            # Volta para a guia anterior
            driver.switch_to.window(driver.window_handles[0])            
            # print(f"Aba alterada para: {driver.current_url}")
            #break    

# Fecha o navegador
driver.quit()
fim = time.time()
# Calcula o tempo decorrido
tempo_decorrido = fim - inicio

# Converte o tempo decorrido em dias, horas, minutos, segundos e centésimos de segundo
tempo_decorrido = time.gmtime(tempo_decorrido)
tempo_decorrido_str = time.strftime("%jd %H:%M:%S.%02d", tempo_decorrido)

# Imprime o tempo decorrido
print(f"Tempo decorrido: {tempo_decorrido_str}")
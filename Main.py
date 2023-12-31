# Antes de rodar o código, copie e cole o seguinte comnado no seu terminal, para instalar os pacotes necessários:
# pip install selenium pyperclip webdriver_manager
# Antes de rodar o código, defina a mensagem que deseja enviar na linha 21 e coloque os nomes dos contatos na linha 25


# Essa parte do código que vai fazer com que abra o whatsapp web no seu navegador. Assim que abrir, conecte o seu whatsapp através do QR Code
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")


# Essa parte do código é onde você vai definir a mensagem que quer escrever e os nomes dos contatos para qual deseja enviar a mensagem
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

mensagem = """ Digite a mensagem que deseja enviar nessa linha!

"""

lista_contatos = [ "Aqui você deve colocar os nomes dos contatos para qual deseja enviar a mensagem."
"Certifique-se de colocas os nomes dentro do colchetes, os nomes devem estar entre aspas e separados por vírgula"]



nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys("Meu Numero")
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(1)


pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + "v")
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)





from selenium.webdriver.common.action_chains import ActionChains


qtde_contatos = len(lista_contatos)

if qtde_contatos % 5 == 0:
    qtde_blocos = qtde_contatos / 5
else:
    qtde_blocos = int(qtde_contatos / 5) + 1

for i in range(qtde_blocos):
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

  
    lista_elementos = nav.find_elements('class name', '_2AOIt') 
    for item in lista_elementos:
        mensagem = mensagem.replace("\n", "")
        texto = item.text.replace("\n", "")
        if mensagem in texto:
            elemento = item
        
    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element('class name', '_3u9t-').click()
    time.sleep(0.5)
    nav.find_element('xpath', '//*[@id="app"]/div/span[4]/div/ul/div/li[4]/div').click()
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()
    time.sleep(1)

    for nome in lista_enviar:
 
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(nome)
        time.sleep(1)
        # dar enter
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        time.sleep(1)
        # apagar o nome do contato
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
        time.sleep(1)

    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(3)


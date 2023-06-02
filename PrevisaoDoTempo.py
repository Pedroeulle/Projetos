# PROJETO 3: PREVISAO DO TEMPO:
# Introdução:
# Neste projeto, você irá utilizar uma API de previsão do tempo para criar um programa que exiba as condições climáticas atuais e a previsão para os próximos dias em uma determinada cidade.

# OQUE FAZER: 

import requests  # Importa a biblioteca requests, utilizada para fazer requisições HTTP
import json  # Importa a biblioteca json, utilizada para trabalhar com dados no formato JSON
from time import sleep  # Importa a função sleep da biblioteca time, utilizada para pausar a execução do programa

while True:  # Inicia um loop infinito
    sleep(5)  # Pausa a execução do programa por 5 segundos

    cidade = input("Digite uma cidade: ")  # Solicita ao usuário que digite o nome de uma cidade

# Escolha uma API de previsão do tempo: Pesquise e escolha uma API de previsão do tempo que forneça os dados necessários para o seu programa.
    try:  # Inicia um bloco de tratamento de exceções
        clima = requests.get("https://api.hgbrasil.com/weather", params={"city_name": cidade})  # Faz uma requisição GET à API de previsão do tempo

        if clima.status_code == 200:  # Verifica se a requisição foi bem-sucedida (código de status 200)

#Trate a resposta da API: Receba a resposta da API e processe os dados retornados. Geralmente, as informações são fornecidas em formato JSON. Utilize as funções e métodos adequados para extrair as informações relevantes, como a temperatura atual, as condições climáticas e a previsão para os próximos dias.
            clima = clima.json()  # Converte a resposta da requisição para JSON
            print("\nCLIMA ATUAL:\n")  # Imprime uma mensagem indicando que serão exibidas as informações do clima atual
            print(cidade)  # Imprime o nome da cidade digitada pelo usuário

# Exiba as informações: Organize as informações obtidas da API e exiba-as de forma clara e legível para o usuário. Você pode mostrar a temperatura atual, as condições climáticas, a umidade, a velocidade do vento e qualquer outra informação que seja relevante.
            climaAgoraD = clima['results']['description']  # Obtém a descrição do clima atual
            print("Tempo:", climaAgoraD)  # Imprime a descrição do clima atual

            climaAgoraHUM = clima['results']['max']  # Obtém a umidade atual
            print("Humidade:", climaAgoraHUM)  # Imprime a umidade atual

            climaAgoraDA = clima['results']['date']  # Obtém a data atual
            print("Data:", climaAgoraDA)  # Imprime a data atual

            climaAgoraT = clima['results']['temp']  # Obtém a temperatura atual

            climaAgoraTM = clima['results']['time']  # Obtém a hora atual
            print("Hora:", climaAgoraTM)  # Imprime a hora atual

            climaAgoraHO = clima['results']['currently']  # Obtém o período do dia
            print("Periodo do dia:", climaAgoraHO)  # Imprime o período do dia

# Tratamento de erros: Adicione tratamento de erros para lidar com possíveis falhas na requisição à API ou erros de conexão. Certifique-se de que o programa seja capaz de lidar com situações em que a cidade não seja encontrada ou a API retorne dados inconsistentes.
        else:
            print("Erro na requisição. Código de status:", clima.status_code)  # Imprime uma mensagem de erro caso a requisição não tenha sido bem-sucedida

    except requests.exceptions.RequestException as e:  # Trata exceções relacionadas a erros de conexão
        print("Erro de conexão. Verifique sua conexão com a internet.")

    except KeyError:  # Trata exceções relacionadas a chaves não encontradas no JSON
        print("Cidade não encontrada. Verifique o nome da cidade digitado.")





# import requests

# #JSON é um formato bom para trocar informações entre um local e outro
# import json
# from time import sleep

# while True: # foi implementa uma repetição para ficar sendo feita a leitura constantemente
#   sleep(5) #Utilizei a função sleep para o programa ter uma pausa entre as mensagens do clima

# # Escolha uma API de previsão do tempo: Pesquise e escolha uma API de previsão do tempo que forneça os dados necessários para o seu programa.
#   cidade = input("Digite uma cidade: ")
#   clima = requests.get("https://api.hgbrasil.com/weather", params={"city_name": cidade})#Atravez deste trecho tempos acesso a uma API de clima
   
#   clima = clima.json()
#   #print(clima) ##esta função extraia toda a informação(tudo contido nas listas) da variavel clima
#   print("\nCLIMA ATUAL: \n") #Aqui é impresso a imagem mensagem do clima atula
#   print(cidade)
#   climaAgoraD = clima ['results'] ['description'] #Estraido a descrição do clima
#   print("Tempo: ", climaAgoraD) #Os dados antes coletados agora são expostos
  
#   climaAgoraHUM = clima ['results'] ['max'] #Estraido a humidade
#   print("Humidade: " , climaAgoraHUM) #Os dados antes coletados agora são expostos
  
#   climaAgoraDA = clima ['results'] ['date'] #Estraido a data
#   print("Data: ", climaAgoraDA) #Os dados antes coletados agora são expostos
  
#   climaAgoraT = clima ['results'] ['temp'] #Estraido a temperatura
  
#   climaAgoraTM = clima ['results'] ['time'] #estraido a hora
#   print("Hora: " , climaAgoraTM) #Os dados antes coletados agora são expostos
#   climaAgoraHO = clima ['results'] ['currently'] #Estraido a 
#   print("Periodo do dia: ", climaAgoraHO) #Os dados antes coletados agora são expostos  


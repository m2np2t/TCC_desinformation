import time


teste = {

                            "Probabilidade": "0.6680631", 
                            "themes": "{'T02': 0.2065798, 'T09': 0.08085475, 'T06': 0.04985724}", 
                            "TOP5": 
                            [
                                [
                                    "Alegação verificada: ", "Na missa de ontem o papa Francisco chorou após rezar e pedir a Deus o fim da pandemia do novo coronavírus", "\n(Score: 0.5883)\n Link: https://checamos.afp.com/foto-do-papa-chorando-e-de-outubro-de-2019-meses-antes-da-identificacao-do-novo-coronavirus\n Veredito: Falso"

                                    

                                ], 
                                [
                                    "Alegação verificada: ", "Circula pelas redes sociais uma imagem do Papa Francisco com o rosto entre as mãos, cobrindo os olhos com um lenço. Uma legenda diz: \"O Papa chora pedindo a misericórdia de Deus para o fim do coronavírus\". A mensagem é #FAKE.", "\n(Score: 0.5202)\n Link: https://g1.globo.com/fato-ou-fake/noticia/2020/07/01/e-fake-que-foto-mostre-papa-francisco-chorando-pedindo-o-fim-da-pandemia-do-coronavirus.ghtml\n Veredito: Falso"

                                ], 
                                [
                                    "Alegação verificada: ", "Ouçam o Monsenhor Viganò, do Vaticano. Ele está certo ao apontar que a pandemia é uma farsa, condenar o lockdown, vacinação e anunciar o Grande Reset que está por vir.", "\n(Score: 0.4847)\n Link: https://www.boatos.org/mundo/monsenhor-vigano-vaticano-esta-certo-falar-sobre-pandemia-vacinas-grande-reset.html\n Veredito: Falso"
                                ], 
                                [
                                    "Alegação verificada: ", "O Santo Papa Francisco pediu a todos que repitam esta oração na mente: Estou vacinado com o Sangue de Cristo: nenhum vírus pode tocar-me!", "\n(Score: 0.4841)\n Link: https://checamos.afp.com/o-papa-francisco-nao-pediu-que-repetissem-oracao-estou-vacinado-com-o-sangue-de-cristo-nenhum-virus\n Veredito: Falso"
                                ], 
                                [
                                    "Alegação verificada: ", "Circula pelas redes sociais uma mensagem que diz que o governador de Pernambuco, Paulo Câmara, proibiu missas virtuais no estado durante a pandemia do novo coronavírus. \"Ele decretou que não pode mais haver transmissão online de missas e cultos, mesmo com as igrejas e os templos fechados\", diz o texto. É #FAKE.", "\n(Score: 0.4764)\n Link: https://g1.globo.com/fato-ou-fake/coronavirus/noticia/2020/05/15/e-fake-que-governador-de-pernambuco-proibiu-missas-online-durante-a-pandemia-do-coronavirus.ghtml\n Veredito: Falso"
                                ]
                            ]
                        }

def machine(text, choice):
    inicio = time.time()

    json = {
                "Probabilidade": "0.6680631", 
                "themes": {"T02": 0.2065798, 
                           "T09": 0.08085475, 
                           "T06": 0.04985724}, 
                "TOP5": 
                    [
                        [
                            "Alegação verificada: ", 
                            "Na missa de ontem o papa Francisco chorou após rezar e pedir a Deus o fim da pandemia do novo coronavírus", 
                            "\n(Score: 0.5883)\n Link: https://checamos.afp.com/foto-do-papa-chorando-e-de-outubro-de-2019-meses-antes-da-identificacao-do-novo-coronavirus\n Veredito: Falso"
                        ], 
                        [
                            "Alegação verificada: ", "Circula pelas redes sociais uma imagem do Papa Francisco com o rosto entre as mãos, cobrindo os olhos com um lenço. Uma legenda diz: \"O Papa chora pedindo a misericórdia de Deus para o fim do coronavírus\". A mensagem é #FAKE.", "\n(Score: 0.5202)\n Link: https://g1.globo.com/fato-ou-fake/noticia/2020/07/01/e-fake-que-foto-mostre-papa-francisco-chorando-pedindo-o-fim-da-pandemia-do-coronavirus.ghtml\n Veredito: Falso"
                        ], 
                        [
                            "Alegação verificada: ", "Ouçam o Monsenhor Viganò, do Vaticano. Ele está certo ao apontar que a pandemia é uma farsa, condenar o lockdown, vacinação e anunciar o Grande Reset que está por vir.", "\n(Score: 0.4847)\n Link: https://www.boatos.org/mundo/monsenhor-vigano-vaticano-esta-certo-falar-sobre-pandemia-vacinas-grande-reset.html\n Veredito: Falso"
                        ], 
                        [
                            "Alegação verificada: ", "O Santo Papa Francisco pediu a todos que repitam esta oração na mente: Estou vacinado com o Sangue de Cristo: nenhum vírus pode tocar-me!", "\n(Score: 0.4841)\n Link: https://checamos.afp.com/o-papa-francisco-nao-pediu-que-repetissem-oracao-estou-vacinado-com-o-sangue-de-cristo-nenhum-virus\n Veredito: Falso"
                        ], 
                        [
                            "Alegação verificada: ", "Circula pelas redes sociais uma mensagem que diz que o governador de Pernambuco, Paulo Câmara, proibiu missas virtuais no estado durante a pandemia do novo coronavírus. \"Ele decretou que não pode mais haver transmissão online de missas e cultos, mesmo com as igrejas e os templos fechados\", diz o texto. É #FAKE.", "\n(Score: 0.4764)\n Link: https://g1.globo.com/fato-ou-fake/coronavirus/noticia/2020/05/15/e-fake-que-governador-de-pernambuco-proibiu-missas-online-durante-a-pandemia-do-coronavirus.ghtml\n Veredito: Falso"
                        ]
                    ]
            }
    fim = time.time()
    
    themes = json["themes"]
    top = json["TOP5"]
    
    #Construção da tabela analisy 
    classification = json["Probabilidade"]
    result = fim - inicio
    #disinformation - Encontrar uma forma de capturar a chave estrangeira de disinformation, neste ponto ela ainda não existe 

    #Construção da tabela themes
    x = 0
    cont = "T0"
    while(x >= 7):
        cont = "T0"

    return result

print(machine('teste', 'teste'))


from operator import itemgetter
from pprint import pprint
import requests

print('Taxa média anual do crescimento da população (BRIKS)')
print()

#77826
response = requests.get("https://servicodados.ibge.gov.br/api/v1/paises/BR|RU|IN|CN|ZA/indicadores/77826")

if response.status_code == 200:
    data_paises = response.json()
    series = data_paises[0]['series']
    lista_valores = []
    for dados in series:
        nome = dados['pais']['nome']
        for serie in dados['serie']:            
            for periodos in serie.keys():
                periodo = periodos
                for valores in serie.values():
                    valor = valores
                    valor_att = str(valor)
                    dict_serie = {"Pais": nome, "Periodo": periodo, "Valor": valor_att}
                    lista_valores.append(dict_serie)           

    lista_ordenada = sorted(lista_valores, key=itemgetter('Valor'), reverse=False)
    pprint(lista_ordenada[slice(10)])    
else:
    print("Erro ao obter dados dos países:", response.status_code)
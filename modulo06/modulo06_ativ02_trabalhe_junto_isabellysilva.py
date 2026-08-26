'''
Javascript object notation(JSON) e um formato leve de troca de dados, facil para humanos lerem e escreverem, e fácil para máqquinas 
analisarem e gerarem. Ele e baseado em um subconjunto da linguagem de programacao Javascript, mas é independente de linguagem com muitos
idiomas de programacao incluindo codigo para gerar e analisar JSON
'''



import json

with open('arquivo_leitura_em_json_isabellycastelo.json', 'r') as arquivo:
    dados_arquivo = json.load(arquivo)

dados_formatados = []

for item in dados_arquivo :
    aluno_formatado = {
        "Nome Completo": item.get("nome") or item.get("Nome Completo"), 
        "idade": item.get("idade"),
        "CEP": item.get("CEP") or item.get ("CEP"),
        "Resgmatr": item.get("Resgmatr") or item.get("Resgmatr"),
        "E-mail": item.get("E-mail") or item.get("e-mail")
    }
    dados_formatados.append(aluno_formatado)

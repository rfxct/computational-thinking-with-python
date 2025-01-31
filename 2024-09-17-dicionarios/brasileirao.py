import json
from pprint import pprint
'''
Nessa atividade, vamos usar dados do campeonato brasileiro 2018
(brasileirao) para estudar como acessar listas,
dicionarios,
e estruturas encadeadas (listas dentro de dicionários
dentro de listas)

Os dados estão fornecidos em um arquivo (ano2018.json) que você 
pode abrir no firefox, para tentar entender melhor (aperte alt para aparecer o menu,
depois, no canto superior esquerdo, arquivo > "abrir arquivo")

Vale a pena instalar o firefox, porque o leitor de arquivo json dele é muito melhor,
mas também existem extensões pro chrome que fazem a mesma coisa.
'''

'''
DICA VSCODE: para poder executar o arquivo py a partir do VSCODE,
é importante ter aberto a pasta certa

Se voce tem a seguinte estrutura de diretorios
distribuidos > brasileirao > brasileirao.py
                             ano2018.json

Deve selecionar no VSCODE File > Open folder
e escolher a pasta brasileirao.
Se escolher distribuidos, o python nao vai achar o arquivo ano2018.json
'''

'''
Se quiser ver os dados dentro do python,
pode chamar a funcao
pega_dados

Nao se preocupe com como ela foi definida, ela só está 
lendo o arquivo json pra voce
'''

def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)
    return dados

'''
não dá muito certo imprimir todos os dados, porque o python 
dá pau ao imprimir uma quantidade tao grande de informações, 
mas podemos ver algumas coisas.

Descomente cada um dos exemplos abaixo para ver o que ele faz.
Verifique a correspondencia do que está sendo impresso pelo
python com o que aparece no firefox

Repare que além do print, você também verá o resultado dos testes. 
No caso, você não passou nenhum teste ainda. 
As primeiras linhas no cmd tem o seu print, as outras tem o resultado dos testes.
'''
dados2018 = pega_dados()
print("\n\n\n") #apenas uns espaços pra te ajudar a ler. Deixe descomentado

#print('todas as chaves do dicionario principal', dados2018.keys())

#print('dados do time corinthians')
#pprint(dados2018['equipes']['6'])

#pprint(dados2018['equipes'])
#print('esses foram os dados de todos os times')
#print('repare que cada time tem uma id. A id do corintians é 6')

#print('faixas de classificacao e rebaixamento')
#pprint(dados2018['fases']['2700']['faixas-classificacao'])

# print('classificacao dos times no fim do campeonato')
# print(dados2018['fases']['2700']['classificacao']['grupo']['Único'])


print("\n\n\n") #apenas uns espaços pra te ajudar a ler
'''
Como você viu nos prints acima, cada time tem uma id numérica,
e pode ser acessado em dados['equipes'][id_numerica]

A primeira funcao a fazer
recebe a id_numerica de um time e deve retornar 
seu 'nome-comum'

Observe que essa funcao (e todas as demais!) recebem os dados dos
jogos numa variavel dados. Essa variavel 
contem todas as informacoes do arquivo
json que acompanha essa atividade 
'''
def nome_do_time(dados,id_numerica):
   return dados['equipes'][id_numerica]['nome-comum']

'''
A proxima funcao recebe somente o dicionario dos dados do brasileirao

Ela retorna a id do time que foi campeao.

Lembre-se de usar a variavel dados, que foi passada para a funcao. 
Nao use dados2018, a variavel global que tinha sido definida antes
'''
def id_campeao(dados):
    return dados['fases']['2700']['classificacao']['grupo']['Único'][0]

'''
A proxima funcao recebe somente o dicionario dos dados do brasileirao

Ela retorna o nome-comum do time que foi campeao.
'''
def nome_campeao(dados):
    id = id_campeao(dados)
    return nome_do_time(dados, id)

'''
A proxima funcao recebe apenas o dicionario dos dados do brasileirao

Ela retorna o nro de times que o brasileirao qualifica para a libertadores

Note. Esse numero está nos dados que eu forneci. Voce deve pegar dos
dados. Nao basta retornar o valor correto, tem que acessar os dados
fornecidos.

Dica: voce vai pegar uma string do tipo "1-5" do dicionário.
Pode ser util quebrar ela em duas usando string.split, e converter
as strings "1" e "5" em números inteiros
>>> string = '1-5'
>>> string.split('-')
['1', '5']
>>> string.split('-')[1]
'5'

'''

def qtos_libertadores(dados):
    return int(
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa'].split('-')[-1]
    )

'''
A proxima funcao recebe um tamanho, e retorna uma lista
das ids dos times melhor classificados.

O tamanho da lista que deve ser retornada é o argumento "numero_de_times"
'''
def ids_dos_melhor_classificados(dados,numero_de_times):
    return dados['fases']['2700']['classificacao']['grupo']['Único'][:numero_de_times]

'''
A proxima funcao usa as duas anteriores para retornar uma 
lista de todos os times classificados para a libertadores em
virtude do campeonato brasileiro

Lembre-se de consultar a estrutura, tanto para obter a classificacao, quanto
para obter o nro correto de times a retornar

A funcao so recebe o dicionario de dados do brasileirao

'''
def classificados_libertadores(dados):
    qtd_libertadores = qtos_libertadores(dados)
    return ids_dos_melhor_classificados(dados, qtd_libertadores)


'''
Usando as duas funcoes anteriores, podemos fazer uma que retorna os nomes dos classificados
'''

def nomes_classificados_libertadores(dados):
    return [
        nome_do_time(dados, id)
        for id in classificados_libertadores(dados)
    ]

'''
Nos nossos dados, cada time tem um id, uma identificacao numerica.
(voce pode consultar as identificacoes numericas em dados['equipes'])

Essas id também aparecem nos jogos 
para ver o jogo 192094, experimente

pprint(dados2018['fases']['2700']['jogos']['id']['102094'])

A proxima função recebe a id numerica de um jogo, e devolve as
ids numéricas dos dois times envolvidos

vou deixar um codigo pra vc lembrar como retornar duas ids em
um unico return

def ids_dos_times_de_um_jogo(dados,id_jogo):
    time1 = 12
    time2 = 13
    return time1,time2 #assim a gente retorna as duas respostas em um unico return
'''
def ids_dos_times_de_um_jogo(dados,id_jogo):
    jogo = dados['fases']['2700']['jogos']['id'][id_jogo]
    return jogo['time1'],jogo['time2']

'''
A proxima funcao "cruza" a anterior com a funcao que pega nomes. 
Recebe uma id de um jogo
e retorna os "nome-comum" dos dois times

(você provavelmente vai querer testar sua funcao no braço e nao
somente fazer os meus testes. Para isso, note que muitos numeros
nesse arquivo estao representados nao como números, mas como strings)
'''
def nomes_dos_times_de_um_jogo(dados,id_jogo):
    time1, time2 = ids_dos_times_de_um_jogo(dados, id_jogo)
    return nome_do_time(dados, time1), nome_do_time(dados, time2)

'''
Façamos agora a busca "ao contrário". Conhecendo
o nome-comum de um time, queremos saber sua id.

Se o nome comum nao existir, retorne 'nao encontrado'
'''
def id_do_time(dados,nome_time):
    for equipe in dados['equipes'].values():
        if equipe['nome-comum'] == nome_time:
            return equipe['id']
    return 'nao encontrado'

'''
Crie uma funcao datas_de_jogo, que procura nos dados do brasileirao 
e devolve uma lista de todas as datas em que houve jogo.

As datas devem ter o mesmo formato que tinham nos dados do brasileirao

dica: busque em dados['fases']

'''
def datas_de_jogo(dados):
    return [data for data in dados['fases']['2700']['jogos']['data']]

'''
Crie uma funcao data_de_um_jogo, que recebe a id numérica de um jogo
e devolve a data em que ele ocorreu. 

Se essa nao é uma id valida, voce deve devolver a string 'nao encontrado'.
Cuidado! Se você devolver uma string ligeiramente diferente, o teste
vai falhar

'''
def data_de_um_jogo(dados,id_jogo):
    jogos = dados['fases']['2700']['jogos']['id']
    if id_jogo in jogos:
         return jogos[id_jogo]['data']
    return 'nao encontrado'

'''
A proxima funcao recebe apenas o dicionario dos dados do brasileirao

ela devolve um dicionário. Esse dicionário conta, para cada estádio,
quantas vezes ocorreu um jogo nele.

Ou seja, as chaves sao ids de estádios e os valores associados,
o número de vezes que um jogo ocorreu no estádio
'''
def dicionario_id_estadio_e_nro_jogos(dados):
    jogos = dados['fases']['2700']['jogos']['id']
    estadios = {}

    for jogo in jogos.values():
        id_estadio = jogo['estadio_id']
        if id_estadio not in estadios:
            estadios[id_estadio] = 0
        estadios[id_estadio] += 1
    return estadios


'''
Agora, façamos uma busca "fuzzy". Queremos procurar por 'Fla'
e achar o flamengo. Ou por 'Paulo' e achar o são paulo.

Nessa busca, você recebe um nome, e verifica os campos
        'nome-comum', 'nome-slug', 'sigla' e 'nome',
        tomando o cuidado de aceitar times se a string
        buscada aparece dentro do nome (A string "Paulo"
        aparece dentro de 'Sao Paulo')

Sua resposta deve ser uma lista de ids de times que "batem"
com a pesquisa (e pode ser vazia, se não achar ninguém)
'''

def busca_imprecisa_por_nome_de_time(dados,nome_time):
    times = []
    for id_time, equipe in dados['equipes'].items():
        possiveis_nomes = [equipe['nome'], equipe['nome-comum'], equipe['nome-slug'], equipe['sigla']]
        for pnome in possiveis_nomes:
            if nome_time.lower() in pnome.lower():
                times.append(id_time)
                break
    return times

#ids dos jogos de um time

'''
Agora, a idéia é receber a id de um time
e retornar as ids de todos os jogos em que ele participou
'''
def ids_de_jogos_de_um_time(dados,time_id):
    ids = []
    for id_jogo in dados['fases']['2700']['jogos']['id']:
        if time_id in ids_dos_times_de_um_jogo(dados, id_jogo):
            ids.append(id_jogo)
    return ids

'''
Usando as ids dos jogos em que um time participou, podemos descobrir
em que dias ele jogou.

Note que essa função recebe o nome-comum do time, nao sua id.

Ela retorna uma lista das datas em que o time jogou
'''
def datas_de_jogos_de_um_time(dados,nome_time):
    id_time = id_do_time(dados, nome_time)
    ids_jogos = ids_de_jogos_de_um_time(dados, id_time)
    datas_jogo = []

    for id_jogo in ids_jogos:
        data_jogo = data_de_um_jogo(dados, id_jogo)
        datas_jogo.append(data_jogo)
    return datas_jogo

'''
A proxima funcao recebe apenas o dicionario dos dados do brasileirao

Ela devolve um dicionário, com quantos gols cada time fez

Ou seja, um dicionario d que tem a chave '17' (correspondendo ao palmeiras)
e o valor associado ao '17' é o numero de gols total que o palmeiras fez.
'''

def dicionario_de_gols(dados):
    gols = {}
    for id_jogo, jogo in dados['fases']['2700']['jogos']['id'].items():
        time1, time2 = ids_dos_times_de_um_jogo(dados, id_jogo)

        if time1 not in gols:
            gols[time1] = 0
        if time2 not in gols:
            gols[time2] = 0

        gols[time1] += int(jogo['placar1'])
        gols[time2] += int(jogo['placar2'])
    return gols
'''
A proxima funcao recebe apenas o dicionario dos dados do brasileirao

Ela devolve a id do time que fez mais gols no campeonato
'''
def time_que_fez_mais_gols(dados):
    gols = dicionario_de_gols(dados)
    id_artilheiro = id_campeao(dados)

    for id_time in gols:
        if gols[id_time] > gols[id_artilheiro]:
            id_artilheiro = id_time
    return id_artilheiro

'''
Da mesma forma que podemos obter a informacao dos times classificados
para a libertadores, também podemos obter os times na zona de rebaixamento

A proxima funcao recebe apenas o dicionário de dados do brasileirao,
e retorna uma lista com as ids dos times rebaixados.

Consulte a zona de rebaixamento do dicionário de dados, nao deixe
ela chumbada da função
'''
def rebaixados(dados):
    min_rebaixamento, max_rebaixamento = (
        dados['fases']['2700']['faixas-classificacao']['classifica3']['faixa'].split('-')
    )

    classificacao = dados['fases']['2700']['classificacao']['grupo']['Único']
    return classificacao[int(min_rebaixamento) - 1:int(max_rebaixamento)]

'''
A proxima função recebe (alem do dicionario de dados do brasileirao) uma id de time

Ela retorna a classificacao desse time no campeonato.

Se a id nao for valida, ela retorna a string 'nao encontrado'
'''
def classificacao_do_time_por_id(dados,time_id):
    classificacao = dados['fases']['2700']['classificacao']['grupo']['Único']
    for posicao, id_time_cl in enumerate(classificacao):
        if time_id == id_time_cl:
            return posicao + 1
    return 'nao encontrado'


import unittest
try:
    from brasileirao_gabarito import *
except:
    pass
class TestStringMethods(unittest.TestCase):
    
    def test_000_nome_do_time(self):
        dados = pega_dados()
        global dados2018
        dados2018 = pega_dados()

        self.assertEqual(nome_do_time(dados,'1'),'Flamengo')
        self.assertEqual(nome_do_time(dados,'695'),'Chapecoense')
    
    def test_001_id_campeao(self):     
        dados = pega_dados()
        try:
            self.assertEqual(id_campeao(dados),'17')
        except NameError as e:
            if 'dados2018' in str(e):
                self.fail("lembre-se de não usar a variavel dados2018, mas sim a variavel dados que a função recebeu")
            else:
                raise e
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['classificacao']['grupo']['Único'].pop(0)
        self.assertEqual(id_campeao(dados),'1')
 

    def test_002_nome_campeao(self):
        dados = pega_dados()
        self.assertEqual(nome_campeao(dados),'Palmeiras')
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['classificacao']['grupo']['Único'].pop(0)
        self.assertEqual(nome_campeao(dados),'Flamengo')
    
    def test_003_qtos_libertadores(self):
        dados = pega_dados()
        self.assertEqual(qtos_libertadores(dados),6)
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']='1-8'
        self.assertEqual(qtos_libertadores(dados),8)

    
    def test_004_ids_dos_melhor_classificados(self):
        dados = pega_dados()
        self.assertEqual(ids_dos_melhor_classificados(dados,10),["17","1","15","13","24","4","3","9","5","22"])
        self.assertEqual(ids_dos_melhor_classificados(dados,5),["17","1","15","13","24"])
        self.assertEqual(ids_dos_melhor_classificados(dados,3),["17","1","15"])
    
    def test_005_classificados_libertadores(self):
        dados = pega_dados()
        self.assertEqual(classificados_libertadores(dados),["17","1","15","13","24","4"])
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']='1-8'
        self.assertEqual(classificados_libertadores(dados),["17","1","15","13","24","4","3","9"])
    
    def test_006_nomes_classificados_libertadores(self):
        dados = pega_dados()
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']='1-3'
        self.assertEqual(nomes_classificados_libertadores(dados),["Palmeiras","Flamengo","Internacional"])
    
    def test_007_ids_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1,t2 = ids_dos_times_de_um_jogo(dados,'102099')
        self.assertTrue(t1 in ['5','17'])
        self.assertTrue(t2 in ['5','17'])
        t1,t2 = ids_dos_times_de_um_jogo(dados,'102109')
        self.assertTrue(t1 in ['1','26'])
        self.assertTrue(t2 in ['1','26'])
    
    def test_008_nomes_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1,t2 = nomes_dos_times_de_um_jogo(dados,'102099')
        self.assertTrue(t1 in ['Botafogo','Palmeiras'])
        self.assertTrue(t2 in ['Botafogo','Palmeiras'])
        t1,t2 = nomes_dos_times_de_um_jogo(dados,'102106')
        self.assertTrue(t1 in ['Chapecoense','Vasco'])
        self.assertTrue(t2 in ['Chapecoense','Vasco'])
    
    def test_009_id_do_time(self):
        dados = pega_dados()
        self.assertEqual(id_do_time(dados,'Cruzeiro'),'9')
        self.assertEqual(id_do_time(dados,'Athletico'),'3')
    
    

    def test_010_datas_de_jogo(self):
        dados = pega_dados()
        datas = datas_de_jogo(dados)
        self.assertEqual(len(datas), 107)
        self.assertTrue('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_011_datas_de_jogo_teste_2(self):
        dados = pega_dados()
        #deleto a data '14 de abril'
        del dados['fases']['2700']['jogos']['data']['2018-04-14']
        #e todos os jogos que ocorreram nela
        del dados['fases']['2700']['jogos']['id']['102094']
        del dados['fases']['2700']['jogos']['id']['102097']
        del dados['fases']['2700']['jogos']['id']['102101']
        datas = datas_de_jogo(dados)
        self.assertEqual(len(datas), 106)
        self.assertFalse('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_012_data_de_um_jogo(self):
        dados = pega_dados()
        self.assertEqual(data_de_um_jogo(dados,'102132'),'2018-05-06')
        self.assertEqual(data_de_um_jogo(dados,'102187'),'2018-06-06')
        self.assertEqual(data_de_um_jogo(dados,'102540'),'nao encontrado')

    def test_013_dicionario_id_estadio_e_nro_jogos(self):
        dados = pega_dados()
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'],16)
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102097']['estadio_id']='72'
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'],17)
    
    def test_014_busca_imprecisa_por_nome_de_time(self):
        dados = pega_dados()
        ids_times = busca_imprecisa_por_nome_de_time(dados,'Paulo')
        self.assertTrue('24' in ids_times)
        ids_times = busca_imprecisa_por_nome_de_time(dados,'SPA')
        self.assertTrue('24' in ids_times)
        ids_times = busca_imprecisa_por_nome_de_time(dados,'anto')
        self.assertTrue('22' in ids_times)
    
    def test_015_ids_de_jogos_de_um_time(self):
        dados = pega_dados()
        jogos_chapeco = ids_de_jogos_de_um_time(dados,'695')
        self.assertEqual(len(jogos_chapeco),38)
        self.assertTrue('102330' in jogos_chapeco)
        self.assertTrue('102422' in jogos_chapeco)
        jogos_santos = ids_de_jogos_de_um_time(dados,'22')
        self.assertEqual(len(jogos_santos),38)
        self.assertTrue('102208' in jogos_santos)
        self.assertTrue('102259' in jogos_santos)
    
    def test_016_datas_de_jogos_de_um_time(self):
        dados = pega_dados()
        datas_santos = datas_de_jogos_de_um_time(dados,'Santos')
        self.assertEqual(len(datas_santos),38)
        self.assertTrue('2018-04-21' in datas_santos)
        self.assertTrue('2018-10-13' in datas_santos)
        datas_chapeco = datas_de_jogos_de_um_time(dados,'Chapecoense')
        self.assertEqual(len(datas_chapeco),38)
        self.assertTrue('2018-11-25' in datas_chapeco)
        self.assertTrue('2018-12-02' in datas_chapeco)
    
    def test_017_dicionario_de_gols(self):
        dados = pega_dados()
        dic_gols = dicionario_de_gols(dados)

        self.assertEqual(dic_gols['695'],34)
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102330']['placar2']=1
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'],35)
        dados['fases']['2700']['jogos']['id']['102422']['placar2']=2
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'],36)
        dados['fases']['2700']['jogos']['id']['102422']['placar2']=12
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'],46)
    
    def test_018_time_que_fez_mais_gols(self):
        dados = pega_dados()
        time = time_que_fez_mais_gols(dados)
        self.assertEqual(time,'17')
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102422']['placar2']=120
        time = time_que_fez_mais_gols(dados)
        self.assertEqual(time,'695')


    def test_019_rebaixados(self):
        dados = pega_dados()
        self.assertEqual(rebaixados(dados),['76', '26', '21', '18'])
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica3']['faixa']='15-20'
        self.assertEqual(rebaixados(dados),['33','25','76', '26', '21', '18'])

    def test_020_classificacao_do_time_por_id(self):
        dados = pega_dados()
        self.assertEqual(classificacao_do_time_por_id(dados,'17'),1)
        self.assertEqual(classificacao_do_time_por_id(dados,'30'),11)
        self.assertEqual(classificacao_do_time_por_id(dados,'695'),14)
        self.assertEqual(classificacao_do_time_por_id(dados,'1313'),'nao encontrado')

    # as proximas funcoes nao sao testes
    def setUp(self):
        global dados2018
        del dados2018
        return super().setUp()

    def tearDown(self):
        global dados2018
        dados2018 = pega_dados()
        return super().tearDown()

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)
    return dados

dados2018 = pega_dados()

if __name__ == '__main__':
    runTests()

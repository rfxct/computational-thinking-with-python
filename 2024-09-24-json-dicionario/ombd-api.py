import requests

'''
A primeira coisa a fazer é ir ao site http://www.omdbapi.com/
e clicar no link API key.

Cadastre-se, abra o e-mail e valide sua chave. Depois, você
poderá acessar o OMDb.
'''

'coloque aqui a sua chave de acesso à api'
api_key = '7a9c0fe5'

'''
Antes de fazer qualquer função, vamos experimentar
consultar o OMDb pelo navegador.

Digite, por exemplo, a seguinte URL no Firefox:
    http://www.omdbapi.com/?s=star%20wars&apikey={SUA-CHAVE-VEM-AQUI}

Observe que vemos uma lista de 10 filmes, mas há mais resultados.

Para ver a página 2, acesse
    http://www.omdbapi.com/?s=star%20wars&page=2&apikey={SUA-CHAVE-VEM-AQUI}
'''


'''
Observe que nas URLs acima, estamos passando parâmetros.
Na URL http://www.omdbapi.com/?s=star%20wars&page=2&apikey={SUA-CHAVE-VEM-AQUI}
definimos 3 parâmetros:
 * s=star wars
 * page=2
 * apikey={SUA-CHAVE-VEM-AQUI}
'''

'''
QUESTÃO 1
Olhando para os resultados da consulta
http://www.omdbapi.com/?s=star%20wars&apikey=7a9c0fe5,
quantos filmes foram encontrados para o termo "star wars"?
(dica: é bem mais do que 100, e você não precisa acessar outra pagina)

Resposta: 896 filmes

QUESTÃO 2
Consultando a documentação em www.omdbapi.com, você
pode aprender a filtrar os resultados da sua busca,
ficando apenas com filmes, eliminando jogos e séries.

Como fazer isso?

Se você fizer essa consulta, quantos filmes
existem para a busca star wars?

Resposta: 627 filmes, com o filtro "type=movie"

QUESTÃO 3:
E se ao invés de filmes você quiser só jogos,
quantos existem?

Resposta: 110 jogos, com o filtro "type=game"

'''




'''
Vou te deixar dois exemplos de como acessar a URL. Nesse exemplo,
eu estou retornando o dicionário inteiro.

Observe a linha
r = requests.get(url)

Estamos chamando a função .get da biblioteca requests,
passando a url como parâmetro, e guardando o retorno na variável r


Para poder usar a biblioteca requests, precisamos fazer duas coisas:
* Instalar a biblioteca requests, usando o comando
`python -m pip install requests` no cmd do windows
* Importar a biblioteca requests (avisar pro programa omdb.py 
que queremos usar essa biblioteca)
 -> isso foi feito na primeira linha do arquivo omdb.py
`import requests` 
'''

def busca_por_id(film_id):
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={film_id}"
    r = requests.get(url)
    return r.json()

def busca_por_texto(texto_buscar, type = None):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}"
    if type != None:
        url += f'&type={type}'
    r = requests.get(url)
    return r.json()

'''
Experimente! chame d1=busca_por_texto('star wars') e examine o
dicionário d1 retornado.
'''

'''
Agora, faça uma função busca_qtd_total que retorna quantos
itens (pode ser filme, jogo, série ou o que for) batem com
uma determinada busca.
'''
def busca_qtd_total(texto_buscar):
    resultado = busca_por_texto(texto_buscar)
    return resultado['totalResults']

'''
Faça uma função busca_qtd_filmes que retorna quantos
filmes batem com uma determinada busca.
'''
def busca_qtd_filmes(texto_buscar):
    resultado = busca_por_texto(texto_buscar, "movie")
    return resultado['totalResults']

'''
Faça uma função busca_qtd_jogos que retorna quantos
jogos batem com uma determinada busca.
'''
def busca_qtd_jogos(texto_buscar):
    resultado = busca_por_texto(texto_buscar, "game")
    return resultado['totalResults']

'''
Agora, vamos aprender a ver os detalhes de um filme.

Por exemplo, na lista de filmes podemos ver que o filme
star wars original (de 1977) tem id 'tt0076759'

Acessando a URL
http://www.omdbapi.com/?i=tt0076759&apikey={SUA-CHAVE-VEM-AQUI}
podemos ver mais detalhes.

Observe que agora não temos mais o parâmetro 's=star%20wars'
mas sim i=tt0076759. Mudou o nome da "variável", não só
o valor.
'''

'''
Faça uma função nome_do_filme_por_id que recebe a id de
um filme e retorna o seu nome.
'''
def nome_do_filme_por_id(id_filme):
   filme = busca_por_id(id_filme)
   return filme['Title']

'''
Faça uma função ano_do_filme_por_id que recebe a id de
um filme e retorna o seu ano de lançamento.
'''
def ano_do_filme_por_id(id_filme):
   filme = busca_por_id(id_filme)
   return filme['Year']

'''
Peguemos vários dados de um filme de uma vez.

A ideia é receber uma id e retornar 
um dicionário com diversos dados do filme.

O dicionário deve ter as seguintes chaves:
 * ano
 * nome
 * diretor
 * genero

E os dados devem ser preenchidos baseado nos dados do site.
'''
def dicionario_do_filme_por_id(id_filme):
    filme = busca_por_id(id_filme)

    if filme["Response"] == "False":
        raise IdInvalida('O id fornecido é inválido')
    dict = {
        "id": id_filme,
        "ano": filme['Year'],
        "nome": filme['Title'],
        "diretor": filme['Director'],
        "genero": filme['Genre'],
        "poster": filme['Poster'],
    }
    for rating in filme['Ratings']:
        if rating['Source'] == 'Metacritic':
            dict['nota_metacritic'] = int(rating['Value'].split('/')[0]) / 100
        if rating['Source'] == 'Rotten Tomatoes':
            dict['nota_rotten_tomatoes'] = int(rating['Value'][0:-1]) / 100
        if rating['Source'] == 'Internet Movie Database':
            dict['nota_imdb'] = float(rating['Value'].split('/')[0]) / 10


    dict['nota_media'] = (
        dict['nota_metacritic'] +
        dict['nota_rotten_tomatoes'] +
        dict['nota_imdb']
    ) / 3

    return dict

'''
Voltando para a busca...

Faça uma função busca_filmes que, dada uma busca, retorna
os dez primeiros items (filmes, series, jogos ou o que for)
que batem com a busca.

A sua resposta deve ser uma lista, cada filme representado por 
um dicionário. cada dicionario deve conter os campos
'nome' (valor Title da resposta) e 'ano' (valor Year da resposta).
'''
def busca_filmes(texto_buscar, type = None):
    resultado = busca_por_texto(texto_buscar, type)['Search']
    return [
        { "nome": d['Title'], "ano": d['Year'] }
        for d in resultado
    ]

'''
Faça uma função busca_filmes_grande que, dada uma busca, retorna
os VINTE primeiros filmes que batem com a busca.
'''
def busca_filmes_grande(texto_buscar):
    return [
        *busca_filmes(texto_buscar, 'movie'),
        *busca_filmes(f'{texto_buscar}&page=2', 'movie')
    ]

'''
Agora, considere novamente a sua função dicionario_do_filme_por_id.

1) Um dos campos que o servidor retorna para nós tem
a URL de um poster. Adicione o campo poster no dicionário retornado.

2) Quando usamos uma id que não existe, temos um erro.
Nesse caso, a função deverá lançar a exceção IdInvalida.
Verifique primeiro no Firefox uma consulta 'zoada'
para ter uma ideia do que fazer.

3) O servidor nos retorna várias notas diferentes.
Adicione o campo nota_rotten_tomatoes no dicionario retornado
A nota deve ser normalizada, passando a ser um valor de 0 a 1,
em vez de uma porcentagem.

4) Faça a mesma coisa do item 3, mas para o metacritic.

5) Faça a mesma coisa dos itens anteriores, mas agora
dando a média das 3 notas (rotten tomatoes, metacritic e imdb).
'''

'''
Voltemos para a busca por string.

Quando fazermos uma busca por string no omdb, temos
como resposta uma lista com 10 dicionários, cada um
representando um filme/jogo/serie.

Queremos contar quantos de cada existem.

A próxima função recebe uma string para buscar,
e devolve um dicionário, dizendo quantos de cada "tipo"
de resultado tivemos.

Por exemplo,
ao fazer conta_tipos_de_midia_para_busca('menace') devemos
receber a resposta {'movie':8,'series':2}.

Confira, acessando a URL: 
http://www.omdbapi.com/?s=menace&apikey={SUA-CHAVE-VEM-AQUI}
'''
def conta_tipos_de_midia_para_busca(texto_buscar):
    resultado = busca_por_texto(texto_buscar)
    total = {}
    for item in resultado['Search']:
        if item['Type'] not in total:
            total[item['Type']] = 0
        total[item['Type']] += 1
    return total

'''
Outra coisa que podemos fazer com nossos 10 resultados é
descobrir qual o filme mais antigo que apareceu.

A função id_do_mais_velho faz exatamente isso:
 * Recebe um texto a buscar;
 * Retorna a id do mais velho dentre os 10 primeiros.
'''
def id_do_mais_velho(texto_buscar):
    resultado = busca_por_texto(texto_buscar)['Search']
    items = [
        { "ano": int(item['Year'].split('-')[0]), "id": item['imdbID'] }
        for item in resultado
    ]
    items.sort(key=lambda item: item['ano'])

    return items[0]['id']

'''
Faça uma função ids_dos_tres_primeiros, que faz uma busca
e retorna uma lista com as ids dos três primeiros produtos
encontrados.
'''
def ids_dos_tres_primeiros(texto_buscar):
    resultado = busca_por_texto(texto_buscar)['Search']
    return [item['imdbID'] for item in resultado]

'''
Agora, podemos cruzar os dados.

A lista de 10 filmes nao contém notas, mas nós sabemos fazer outra
consulta para achar as notas.

Crie uma função mais_bem_avaliado_dos_3_primeiros, que recebe uma
string para buscar, e retorna a id do mais bem avaliado entre os
3 primeiros resultados.

Não façamos com mais resultados, para não sobrecarregar o servidor.
'''
def mais_bem_avaliado_dos_3_primeiros(texto_buscar):
    items = [
        dicionario_do_filme_por_id(id)
        for id in ids_dos_tres_primeiros(texto_buscar)
    ]
    items.sort(reverse=True, key=lambda item: item['nota_media'])
    return items[0]['id']
'''
A próxima função já vem pronta, mas vamos melhorar ela depois.

O que ela faz? Recebe uma id do filme e baixa um arquivo Poster.jpg
com o poster do filme.

Basicamente, ela acessa uma URL como
http://img.omdbapi.com/?apikey={SUA-CHAVE-VEM-AQUI}&i=tt0120915
'''
def baixar_poster(id_filme):
    url = "http://img.omdbapi.com/?apikey={0}&i={1}".format(api_key, id_filme)
    retorno = requests.get(url)

    if retorno.status_code == 404:
        return 'id invalida'

    arquivo = open("Poster.jpg", "wb")
    arquivo.write(retorno.content)
    arquivo.close()
    return 'id valida'

'''
'tt0796366' é a id de star trek.
'tt1211837' é a id de doctor strange.
'naoexiste' é uma id inválida.

1) Experimente digitar as URLs, juntando as IDs acima.

2) Experimente a função, usando as ids acima.

3) Tente rodar a funcao com a id naonaonao. O que ocorreu?

4) Corrija o problema: Faça a função retornar 'id inválida' quando 
ela recebeu uma id inválida, e 'id válida' quando a id era valida.

Dica: Procure o código de status usando o imsomnium
https://github.com/ArchGPT/insomnium/releases/download/core%400.2.3-a/Insomnium.Core-0.2.3-a-portable.exe
https://github.com/ArchGPT/insomnium/releases

(ou, se quiser usar o firefox:
Faça a chamada válida e a chamada inválida, mas antes de cada uma,
vá em ferramentas de desenvolvedor > network.)

Dica 2: Para ver o código de status na biblioteca requests, use
r.status_code
'''


import unittest


class IdInvalida(Exception):
    pass


class TestStringMethods(unittest.TestCase):
    def test_000_qdt_total(self):
        #os valores são aproximados, pro teste nao falhar com mudanças no banco de dados
        self.assertTrue(867 * 0.9 < int(busca_qtd_total('star wars')) < 867 * 1.1)
        self.assertTrue(493 * 0.9 < int(busca_qtd_total('star trek')) < 493 * 1.1)

    def test_001_qdt_filmes(self):
        #os valores são aproximados, pro teste nao falhar com mudanças no banco de dados
        self.assertTrue(611 * 0.9 < int(busca_qtd_filmes('star wars')) < 611 * 1.1)
        self.assertTrue(351 * 0.9 < int(busca_qtd_filmes('star trek')) < 351 * 1.1)
        self.assertTrue(163 * 0.9 < int(busca_qtd_filmes('menace')) < 163 * 1.1)
        self.assertTrue(1661 * 0.9 < int(busca_qtd_filmes('future')) < 1661 * 1.1)

    def test_002_qdt_jogos(self):
        #os valores são aproximados, pro teste nao falhar com mudanças no banco de dados
        self.assertTrue(110 * 0.9 < int(busca_qtd_jogos('star wars')) < 110 * 1.1)
        self.assertTrue(67 * 0.9 < int(busca_qtd_jogos('star trek')) < 67 * 1.1)
        self.assertTrue(10 * 0.8 < int(busca_qtd_jogos('menace')) < 10 * 1.2 )
        self.assertTrue(41 * 0.9 < int(busca_qtd_jogos('future')) < 41 * 1.1)

    def test_003_nome_do_filme_por_id(self):
        self.assertEqual(nome_do_filme_por_id('tt0796366'), 'Star Trek')
        self.assertEqual(nome_do_filme_por_id('tt0861739'), 'Elite Squad')

    def test_004_ano_do_filme_por_id(self):
        self.assertEqual(ano_do_filme_por_id('tt0076759'), '1977')
        self.assertEqual(ano_do_filme_por_id('tt1211837'), '2016')

    def test_005_dicionario_filme_por_id(self):
        d1 = dicionario_do_filme_por_id('tt0076759')
        self.assertTrue(type(d1) is dict)
        self.assertEqual(d1['ano'], '1977')
        self.assertEqual(d1['diretor'], 'George Lucas')
        self.assertTrue('Action' in d1['genero'])
        d2 = dicionario_do_filme_por_id('tt1211837')
        self.assertTrue(type(d2) is dict)
        self.assertEqual(d2['ano'], '2016')
        self.assertEqual(d2['nome'], 'Doctor Strange')
        self.assertTrue('Fantasy' in d2['genero'])

    def test_006_busca(self):
        resposta = busca_filmes('star wars')
        self.assertEqual(len(resposta),10)
        achei = False
        for filme in resposta:
            if int(filme['ano']) == 1977:
                achei = True
            if 'ano' not in filme:
                self.fail('Ano não encontrado')
            if 'nome' not in filme:
                self.fail('Nome não encontrado')
        if not achei:
            self.fail('Filme "A New Hope" não encontrado')
    
    def test_007_busca_grande(self):
        resposta = busca_filmes_grande('star wars')
        self.assertEqual(len(resposta), 20)
        achei = False
        for filme in resposta:
            if int(filme['ano']) == 1977:
                achei = True
            if 'ano' not in filme:
                self.fail('Ano não encontrado.')
            if 'nome' not in filme:
                self.fail('Nome não encontrado.')
        if not achei:
            self.fail('Filme "A New Hope" não encontrado.')
    
    def test_008_dicionario_filme_por_id_tem_poster(self):
        resposta = dicionario_do_filme_por_id('tt0796366')
        self.assertTrue(
        "MV5BMjE5NDQ5OTE4Ml5BMl5BanBnXkFtZTcwOTE3NDIzMw@@._V1_SX300.jpg" in
                resposta['poster'])
    
    def test_009_tenta_montar_dicionario_para_id_invalida(self):
        try:
            dicionario_do_filme_por_id('tt0796366naoao')
        except IdInvalida:
            print('Ok, você levantou a exceção desejada.')
        except:
            self.fail('Você levantou uma exceção diferente.')
        else:
            self.fail('Você não levantou exceção.')
    
    def test_010_dicionario_tem_nota_rotten_tomatoes(self):
        resposta = dicionario_do_filme_por_id('tt0796366')
        self.assertTrue(0.90 < resposta['nota_rotten_tomatoes'] < 0.98)
        resposta = dicionario_do_filme_por_id('tt0861739')
        self.assertTrue(0.41 < resposta['nota_rotten_tomatoes'] < 0.59)

    
    def test_011_dicionario_tem_nota_metacritic(self):
        resposta = dicionario_do_filme_por_id('tt0796366')
        self.assertTrue(0.8 < resposta['nota_metacritic'] < 0.84)
        resposta = dicionario_do_filme_por_id('tt0861739')
        self.assertTrue(0.3 < resposta['nota_metacritic'] < 0.35)
    
    def test_012_dicionario_tem_nota_media(self):
        resposta = dicionario_do_filme_por_id('tt0796366')

        self.assertTrue(0.80 < resposta['nota_media'] < 0.90)
        resposta = dicionario_do_filme_por_id('tt0861739')
        self.assertTrue(0.50 < resposta['nota_media'] < 0.60)

    def test_013_conta_tipos_de_midia_para_busca(self):
        d1 = conta_tipos_de_midia_para_busca('menace')
        self.assertEqual(d1, {'movie': 8, 'series': 2})
        d1 = conta_tipos_de_midia_para_busca('grim fandango')
        self.assertEqual(d1, {'game': 2})
   
    def test_014_id_do_mais_velho(self):
        self.assertEqual(id_do_mais_velho('star wars'), 'tt0076759')
        self.assertEqual(id_do_mais_velho('grim fandango'), 'tt0177822')

    def test_015_ids_dos_tres_primeiros(self):
        lista = ids_dos_tres_primeiros('star wars')
        self.assertTrue('tt0076759' in lista)
        self.assertTrue('tt0080684' in lista)
        self.assertTrue('tt0086190' in lista)

    def test_016_mais_bem_avaliado(self):
        self.assertEqual(mais_bem_avaliado_dos_3_primeiros('star wars'), 'tt0076759')

    def test_017_poster_invalida(self):
        resposta = baixar_poster('tt0796366naoao')
        self.assertEqual(resposta, 'id invalida')
        resposta = baixar_poster('bonde')
        self.assertEqual(resposta, 'id invalida')
        resposta = baixar_poster('blackkamenrider')
        self.assertEqual(resposta, 'id invalida')

    def test_018_poster_valida(self):
        resposta = baixar_poster('tt0796366')
        self.assertEqual(resposta, 'id valida')

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)

#pode deletar o try e except a seguir, nao é util pra você, só pro professor
try:
    from omdb_gabarito import *
except:
    pass

# esse aqui nao delete
if __name__ == "__main__":
    runTests()

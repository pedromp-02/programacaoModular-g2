from reutilizaveis.manipulacao import *
from reutilizaveis.casingComp import *
from prog1.substituicao import *
from prog2.contagem import *
from prog3.lista_linhas import *

# Testes do módulo de manipulação:
def test_gera_string():
    with open("teste.txt", 'w') as f:
        f.write('This is another test\n')
    f.close()
    with open("teste.txt", 'r') as f:
        assert f.read() == gera_string("teste.txt")
    f.close()
    
def test_gera_arquivo():
    string = 'This is a test\n'
    diretorio = "texto-alterado.txt"
    f = gera_arquivo(string,diretorio)
    with open(diretorio, 'r') as f:
        assert string == f.read()
    f.close()   
    
# Testes do módulo de comparação e casing match de palavras:
def test_compara_palavras():
    assert compara_palavras('fine', 'fine') == True
    assert compara_palavras('fine', 'Fine') == True
    assert compara_palavras('fine', 'FINE') == True
    assert compara_palavras('fine', 'fINE') == True
    
    assert compara_palavras('Fine', 'fine') == True
    assert compara_palavras('Fine', 'Fine') == True
    assert compara_palavras('Fine', 'FINE') == True
    assert compara_palavras('Fine', 'fINE') == True
    
    assert compara_palavras('FINE', 'fine') == True
    assert compara_palavras('FINE', 'Fine') == True
    assert compara_palavras('FINE', 'FINE') == True
    assert compara_palavras('FINE', 'fINE') == True
    
    assert compara_palavras('fINE', 'fine') == True
    assert compara_palavras('fINE', 'Fine') == True
    assert compara_palavras('fINE', 'FINE') == True
    assert compara_palavras('fINE', 'fINE') == True
    
    assert compara_palavras('fine', 'nice') == False
    assert compara_palavras('fine', 'nICE') == False
    assert compara_palavras('fine', 'NICE') == False
    assert compara_palavras('fine', 'Nice') == False
    
    assert compara_palavras('Fine', 'nice') == False
    assert compara_palavras('Fine', 'nICE') == False
    assert compara_palavras('Fine', 'NICE') == False
    assert compara_palavras('Fine', 'Nice') == False
    
    assert compara_palavras('fINE', 'nice') == False
    assert compara_palavras('fINE', 'nICE') == False
    assert compara_palavras('fINE', 'NICE') == False
    assert compara_palavras('fINE', 'Nice') == False
    
    assert compara_palavras('FINE', 'nice') == False
    assert compara_palavras('FINE', 'nICE') == False
    assert compara_palavras('FINE', 'NICE') == False
    assert compara_palavras('FINE', 'Nice') == False
    
def test_match_casing():
    assert match_casing('!*(&', 'test') == 'test'
    assert match_casing('221', 'test') == 'test'
        
    assert match_casing('I', 'i') == 'I'
    assert match_casing('i', 'i') == 'i' 
    
    assert match_casing('I', 'am') == 'AM'
    assert match_casing('i', 'am') == 'am' 
    
    assert match_casing('HE', 'my') == 'MY'
    assert match_casing('He', 'my') == 'My' 
    assert match_casing('he', 'my') == 'my'
    assert match_casing('hE', 'my') == 'my' 
    
    assert match_casing('HI', 'hello') == 'HELLO'
    assert match_casing('Hi', 'hello') == 'Hello' 
    assert match_casing('hi', 'hello') == 'hello'
    assert match_casing('hI', 'hello') == 'hello'    
    
    assert match_casing('TRY', 'dry') == 'DRY'
    assert match_casing('Try', 'dry') == 'Dry'
    assert match_casing('try', 'dry') == 'dry'
    assert match_casing('tRY', 'dry') == 'dry'    
    assert match_casing('trY', 'dry') == 'dry'
    assert match_casing('TrY', 'dry') == 'dry'
    assert match_casing('TRy', 'dry') == 'dry'
    
    assert match_casing('WHY', 'where') == 'WHERE'
    assert match_casing('Why', 'where') == 'Where'
    assert match_casing('why', 'where') == 'where'
    assert match_casing('wHY', 'where') == 'where'    
    assert match_casing('whY', 'where') == 'where'
    assert match_casing('WhY', 'where') == 'where'
    assert match_casing('WHy', 'where') == 'where'
    
    assert match_casing('FINE', 'good') == 'GOOD'
    assert match_casing('Fine', 'good') == 'Good'
    assert match_casing('fine', 'good') == 'good'
    assert match_casing('fINE', 'good') == 'good'    
    assert match_casing('FinE', 'good') == 'good'
    assert match_casing('fiNE', 'good') == 'good'
    assert match_casing('fIne', 'good') == 'good'
   
    assert match_casing('SOUP', 'vegetable') == 'VEGETABLE'
    assert match_casing('Soup', 'vegetable') == 'Vegetable'
    assert match_casing('soup', 'vegetable') == 'vegetable'
    assert match_casing('sOUP', 'vegetable') == 'vegetable'    
    assert match_casing('SouP', 'vegetable') == 'vegetable'
    assert match_casing('soUP', 'vegetable') == 'vegetable'
    assert match_casing('sOup', 'vegetable') == 'vegetable'
    
    assert match_casing('LIGHT', 'heavy') == 'HEAVY'
    assert match_casing('Light', 'heavy') == 'Heavy'
    assert match_casing('light', 'heavy') == 'heavy'
    assert match_casing('lIGHT', 'heavy') == 'heavy'    
    assert match_casing('liGHT', 'heavy') == 'heavy'
    assert match_casing('LIght', 'heavy') == 'heavy'
    assert match_casing('LighT', 'heavy') == 'heavy'
    
    assert match_casing('RANCH', 'hyperbole') == 'HYPERBOLE'
    assert match_casing('Ranch', 'hyperbole') == 'Hyperbole'
    assert match_casing('ranch', 'hyperbole') == 'hyperbole'
    assert match_casing('rANCH', 'hyperbole') == 'hyperbole'    
    assert match_casing('raNCH', 'hyperbole') == 'hyperbole'
    assert match_casing('RAnch', 'hyperbole') == 'hyperbole'
    assert match_casing('RancH', 'hyperbole') == 'hyperbole'
    
    assert match_casing('HEIGHT', 'crouch') == 'CROUCH'
    assert match_casing('Height', 'crouch') == 'Crouch'
    assert match_casing('height', 'crouch') == 'crouch'
    assert match_casing('hEIGHT', 'crouch') == 'crouch'    
    assert match_casing('heiGHT', 'crouch') == 'crouch'
    assert match_casing('HEIght', 'crouch') == 'crouch'
    assert match_casing('HeighT', 'crouch') == 'crouch'
    
    assert match_casing('MIGHTY', 'henceforth') == 'HENCEFORTH'
    assert match_casing('Mighty', 'henceforth') == 'Henceforth'
    assert match_casing('mighty', 'henceforth') == 'henceforth'
    assert match_casing('mIGHTY', 'henceforth') == 'henceforth'    
    assert match_casing('migHTY', 'henceforth') == 'henceforth'
    assert match_casing('MIGhty', 'henceforth') == 'henceforth'
    assert match_casing('MightY', 'henceforth') == 'henceforth'
    
# Testes do módulo de substituição de palavras:
def test_substitui_palavra():
    assert substitui_palavra('a string', 'a', 'another') == 'another string'
    assert substitui_palavra('EXAMPLE', 'EXAMPLE', 'TEST') == 'TEST'
    assert substitui_palavra('Small test', 'small', 'big') == 'Big test'
    assert substitui_palavra('hello world', 'HELLO', 'hi') == 'hi world'
    assert substitui_palavra('Odds Evens ODDS EVENS odds evens oDDS eVENS', 'odds', 'evens') == 'Evens Evens EVENS EVENS evens evens evens eVENS'
    assert substitui_palavra('This is sPECIFIC', 'SpeCiFiC', 'nEAT') == 'This is neat'
    assert substitui_palavra('Make it WORk', 'work', 'rUN') == 'Make it run'
    assert substitui_palavra('Have a good DaY', 'DAY', 'EveninG') == 'Have a good evening'
    assert substitui_palavra('This is clearlY a test', 'Clearly', 'Simply') == 'This is simply a test'
    assert substitui_palavra('The following word is deleted', 'DELETED', '') == 'The following word is '
    assert substitui_palavra('There are 365 days in a year.', '365', '999') == 'There are 365 days in a year.'

# Testes do módulo de contagem:
def test_contagem():
    texto = "Teste Simples Módulo:\nExemplo de teste bastante simples.\nTESTE.\n"
    esperado = 'Teste - 3\nSimples - 2\nMódulo - 1\nExemplo - 1\nDe - 1\nBastante - 1\n'
    assert gera_matriz_indice(texto) == esperado
    
    texto = "Esse: TESTe TESTE é\nMuito. ESPECÍFICO\ne Possui\nVÁRIAS, linhas LINHAS,.\nde teste!\n"
    esperado = 'Esse - 1\nTeste - 3\nÉ - 1\nMuito - 1\nEspecífico - 1\nE - 1\nPossui - 1\nVárias - 1\nLinhas - 2\nDe - 1\n'
    assert gera_matriz_indice(texto) == esperado
    
# Testes do módulo de lista de linhas:
def test_lista_linhas():
    texto = "Esse teste é muito importante.\nNosso trabalho é feito em Python.\nCada teste possui sua utilidade.\n"
    palavra = "teste"
    esperado = "1 - Esse teste é muito importante.\n3 - Cada teste possui sua utilidade.\n"
    assert gera_lista_linhas(texto,palavra) == esperado
    
    texto = "Linha 1.\nNada.\nNada.\nlINHA 4!\nteste.\nSexta linha.\nSétima lINHA.\n"
    palavra = "linha"
    esperado = "1 - Linha 1.\n4 - lINHA 4!\n6 - Sexta linha.\n7 - Sétima lINHA.\n"
    assert gera_lista_linhas(texto,palavra) == esperado

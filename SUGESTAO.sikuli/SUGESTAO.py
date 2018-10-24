# SUGESTAO PADRAO

def endereco():
    if(exists("1537836711054-8.png")):
        click("1537836711054-8.png")
    else:
        find("1537837616092-8.png")
        click("1537837616092-8.png")
    find("1536792463168-11.png")
    type('localhost')
    def typeSlash():
        keyDown(Key.ALT)
        type(Key.NUM4+Key.NUM7)
        keyUp()
    typeSlash()
    type('projeto')
    typeSlash()
    type('sugestao')
    typeSlash()
    type('cadastrar')
    type(Key.ENTER)
    sleep(2)
    
endereco()

find("1536792680544.png")
click("1536792680544.png")
type('Spock')
find("1536792667843.png")
click("1536792667843.png")
type('spock@enterprise1701.uss')
find("1536792749488.png")
click("1536792749488.png")
type('Nao digitar acentos eh ilogico.')
find("1536800656068.png")
click("1536800656068.png")

def word(teste):
    sleep(2)
    type(Key.PRINTSCREEN)
    if(exists("1536795174517-11.png")):
        click("1536795174517-11.png")
    else:
        find("1538440425431-6.png")
        click("1538440425431-6.png")
        type('word' + Key.ENTER)
        sleep(2)
        wait("1537835985449-11.png")
        type(Key.ENTER)    
    type('sugestao '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    find("1537404525832-12.png")
    click("1537404525832-12.png")

teste = 'padrao'
word(teste)


# DESCRICAO


endereco()

find("1536792680544-1.png")
click("1536792680544-1.png")
type('Spock')
find("1536792667843-1.png")
click("1536792667843-1.png")
type('spock@enterprise1701.uss')
find("1536792749488-1.png")
click("1536792749488-1.png")
type(',', Key.SHIFT)
find("1536800656068-1.png")
click("1536800656068-1.png")

teste = 'descricao com caracteres especiais'
word(teste)


# EMAIL


endereco()

find("1536792680544-2.png")
click("1536792680544-2.png")
type('Spock')
find("1536792667843-2.png")
click("1536792667843-2.png")
type('spock.enterprise1701.uss')
find("1536792749488-2.png")
click("1536792749488-2.png")
type('Nao digitar acentos eh ilogico.')
find("1536800656068-2.png")
click("1536800656068-2.png")

teste = 'email'
word(teste)


# NOME NUMEROS


endereco()

find("1536792680544-3.png")
click("1536792680544-3.png")
type('123')
find("1536792667843-3.png")
click("1536792667843-3.png")
type('spock@enterprise1701.uss')
find("1536792749488-3.png")
click("1536792749488-3.png")
type('Nao digitar acentos eh ilogico.')
find("1536800656068-3.png")
click("1536800656068-3.png")

teste = 'nome com numeros'
word(teste)


# NOME CARACTERES ESPECIAIS


endereco()

find("1536792680544-3.png")
click("1536792680544-3.png")
type(',', Key.SHIFT)
find("1536792667843-3.png")
click("1536792667843-3.png")
type('spock@enterprise1701.uss')
find("1536792749488-3.png")
click("1536792749488-3.png")
type('Nao digitar acentos eh ilogico.')
find("1536800656068-3.png")
click("1536800656068-3.png")

teste = 'nome com caracteres especiais'
word(teste)


# VOLTAR

endereco()

find("1536792680544-4.png")
click("1536792680544-4.png")
type('Spock')
find("1536792667843-4.png")
click("1536792667843-4.png")
type('spock@enterprise1701.uss')
find("1536792749488-4.png")
click("1536792749488-4.png")
type('Nao digitar acentos eh ilogico.')
find("1536798681943.png")
click("1536798681943.png")

teste = 'voltar ao login'
word(teste)

click("1536795174517-13.png")

find("1538229390137-1.png")
click("1538229390137-1.png")
find("1538229412402-1.png")
doubleClick("1538229412402-1.png")
find("1539650165371.png")
click("1539650165371.png")
find("1538229509689-1.png")
click("1538229509689-1.png")
type('sugestao testes')
find("1538229537023-1.png")
click("1538229537023-1.png")
find("1538229937734-1.png")
click("1538229937734-1.png")
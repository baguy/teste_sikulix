# ALMOXARIFADO

def endereco():
    if(exists("1537836711054.png")):
        click("1537836711054.png")
    else:
        find("1537837616092.png")
        click("1537837616092.png")
    find("1536792463168.png")
    type('localhost')
    def typeSlash():
        keyDown(Key.ALT)
        type(Key.NUM4+Key.NUM7)
        keyUp()
    typeSlash()
    type('projeto')
    typeSlash()
    type('almoxarifado')
    typeSlash()
    type('cadastrar')
    type(Key.ENTER)
    sleep(2)


# PADRAO


endereco()

find("1539218410606.png")
click("1539218410606.png")
type('coisa')
find("1539218528869.png")
click("1539218528869.png")
type('3')
find("1539218557805.png")
click("1539218557805.png")
type('222222')
find("1539220293856.png")
click("1539220293856.png")
type('alguma coisa')
find("1539220325267.png")
click("1539220325267.png")
type('10102018')
find("1539220349544.png")
click("1539220349544.png")
type(Key.DOWN + Key.ENTER)
find("1539220474860.png")
click("1539220474860.png")

def word(teste):
    sleep(2)
    type(Key.PRINTSCREEN)
    if(exists("1536795174517-6.png")):
        click("1536795174517-6.png")
    else:
        find("1538440425431-1.png")
        click("1538440425431-1.png")
        type('word' + Key.ENTER)
        sleep(2)
        wait("1537835985449-6.png")
        type(Key.ENTER)    
    type('Almoxarifado '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    type(Key.ENTER)
    find("1537404525832-6.png")
    click("1537404525832-6.png")

teste = 'padrao'
word(teste)

# NOME

endereco()

sleep(2)
find("1539218410606.png")
click("1539218410606.png")
type('123')
find("1539218528869.png")
click("1539218528869.png")
type('3')
find("1539218557805.png")
click("1539218557805.png")
type('222222')
find("1539220293856.png")
click("1539220293856.png")
type('alguma coisa')
find("1539220325267.png")
click("1539220325267.png")
type('10102018')
find("1539220349544.png")
click("1539220349544.png")
type(Key.DOWN + Key.ENTER)
find("1539220474860.png")
click("1539220474860.png")
 
teste = 'numeros inseridos no campo NOME - DEVE apresentar mensagem de erro'
word(teste)


# QUANTIDADE


endereco()

sleep(2)
find("1539218410606.png")
click("1539218410606.png")
type('outra coisa')
find("1539218528869.png")
click("1539218528869.png")
type('e')
find("1539218557805.png")
click("1539218557805.png")
type('322222')
find("1539220293856.png")
click("1539220293856.png")
type('alguma coisa')
find("1539220325267.png")
click("1539220325267.png")
type('10102018')
find("1539220349544.png")
click("1539220349544.png")
type(Key.DOWN + Key.ENTER)
find("1539220474860.png")
click("1539220474860.png")
 
teste = 'letra inserida no campo QUANTIDADE - DEVE apresentar mensagem de erro'
word(teste)


# VALOR


endereco()

sleep(2)
find("1539218410606.png")
click("1539218410606.png")
type('mais coisa')
find("1539218528869.png")
click("1539218528869.png")
type('4')
find("1539218557805.png")
click("1539218557805.png")
type('abc')
find("1539220293856.png")
click("1539220293856.png")
type('alguma coisa')
find("1539220325267.png")
click("1539220325267.png")
type('10102018')
find("1539220349544.png")
click("1539220349544.png")
type(Key.DOWN + Key.ENTER)
find("1539220474860.png")
click("1539220474860.png")
 
teste = 'letras inseridas no campo VALOR - DEVE apresentar mensagem de erro'
word(teste)


# DESCRICAO


endereco()

sleep(2)
find("1539218410606.png")
click("1539218410606.png")
type('mais coisa')
find("1539218528869.png")
click("1539218528869.png")
type('4')
find("1539218557805.png")
click("1539218557805.png")
type('555')
find("1539220293856.png")
click("1539220293856.png")
type(',', Key.SHIFT)
find("1539220325267.png")
click("1539220325267.png")
type('10102018')
find("1539220349544.png")
click("1539220349544.png")
type(Key.DOWN + Key.ENTER)
find("1539220474860.png")
click("1539220474860.png")
 
teste = 'caractere especial - menor - inserido no campo DESCRIÇÃO - DEVE apresentar mensagem de erro'
word(teste)


# DATA DE RECEBIMENTO


endereco()

sleep(2)
find("1539218410606.png")
click("1539218410606.png")
type('mais uma coisa')
find("1539218528869.png")
click("1539218528869.png")
type('9')
find("1539218557805.png")
click("1539218557805.png")
type('10555')
find("1539220293856.png")
click("1539220293856.png")
type('aaae')
find("1539220325267.png")
click("1539220325267.png")
type('32132222')
find("1539220349544.png")
click("1539220349544.png")
type(Key.DOWN + Key.ENTER)
find("1539220474860.png")
click("1539220474860.png")
 
teste = 'data impossivel no campo DATA DE RECEBIMENTO - DEVE apresentar mensagem de erro'
word(teste)


# UNIDADE DE MEDIDA


endereco()

find("1539218410606.png")
click("1539218410606.png")
type('mais uma coisa')
find("1539218528869.png")
click("1539218528869.png")
type('9')
find("1539218557805.png")
click("1539218557805.png")
type('10555')
find("1539220293856.png")
click("1539220293856.png")
type('descricao')
find("1539220325267.png")
click("1539220325267.png")
type('10102017')
find("1539220474860.png")
click("1539220474860.png")
 
teste = 'unidade de medida nao selecionado - DEVE apresentar mensagem de erro'
word(teste)

click("1536795174517-6.png")
find("1538229390137.png")
click("1538229390137.png")
find("1538229412402.png")
doubleClick("1538229412402.png")
find("1539650165371.png")
click("1539650165371.png")
find("1538229509689.png")
click("1538229509689.png")
type('almoxarifado testes')
find("1538229537023.png")
click("1538229537023.png")
find("1538229937734.png")
click("1538229937734.png")
# PRODUTO PADRÃO

def endereco():
    if(exists("1537836711054-10.png")):
        click("1537836711054-10.png")
    else:
        find("1537837616092-10.png")
        click("1537837616092-10.png")
    find("1536792463168.png")
    type('localhost')
    def typeSlash():
        keyDown(Key.ALT)
        type(Key.NUM4+Key.NUM7)
        keyUp()
    typeSlash()
    type('projeto')
    typeSlash()
    type('produto')
    typeSlash()
    type('cadastrar')
    type(Key.ENTER)
    sleep(2)

endereco()

find("1534813808104.png")
click("1534813808104.png")
type('tiara')

find("1534813813076.png")
click("1534813813076.png")
type('06')

find("1542843475777.png")
find("1542843475777.png")
type("drgherger54")

find("1534813817875.png")
click("1534813817875.png")
type('123')

find("1534813822452.png")
click("1534813822452.png")
type('531826')

find("1534813840608.png")
click("1534813840608.png")
type('11112011')

find("1534813833622.png")
click("1534813833622.png")
type('11112022')

find("1534977686771.png")
click("1534977686771.png")
type('06062018')

find("1534813854863.png")
click("1534813854863.png")
type(Key.DOWN + Key.ENTER)

find("1533776396884.png")
click("1533776396884.png")

teste = "padrao"

def word(teste):
    sleep(2)
    type(Key.PRINTSCREEN)
    if(exists("1536795174517-1.png")):
        click("1536795174517-1.png")
    else:
        find("1538440425431-7.png")
        click("1538440425431-7.png")
        type('word' + Key.ENTER)
        wait("1537835985449-1.png")
        type(Key.ENTER)   
    type('Produto ' + teste + Key.ENTER)
    type('v', KEY_CTRL)
    find("1537404525832-1.png")
    click("1537404525832-1.png")

# CODIGO

endereco()

find("1534813808104-1.png")
click("1534813808104-1.png")
type('bambole')

find("1534813813076-1.png")
click("1534813813076-1.png")
type('abc')

find("1542843475777.png")
find("1542843475777.png")
type("drgherger54")

find("1534813817875-1.png")
click("1534813817875-1.png")
type('abc2')

find("1534813822452-1.png")
click("1534813822452-1.png")
type('531826')

find("1534813840608-1.png")
click("1534813840608-1.png")
type('11112011')

find("1534813833622-1.png")
click("1534813833622-1.png")
type('11112022')

find("1534977686771-1.png")
click("1534977686771-1.png")
type('06062018')

find("1534813854863-1.png")
click("1534813854863-1.png")
type(Key.DOWN + Key.ENTER)

find("1533776396884-1.png")
click("1533776396884-1.png")

teste = "inserir letras e numeros em CODIGO DO PRODUTO - DEVE permitir"
word(teste)

# DATA DE FABRICAÇÃO

endereco()

find("1534813808104-2.png")
click("1534813808104-2.png")
type('chinelo')

find("1534813813076-2.png")
click("1534813813076-2.png")
type('06')

find("1542843475777.png")
find("1542843475777.png")
type("drgherger54")

find("1534813817875-2.png")
click("1534813817875-2.png")
type('123')

find("1534813822452-2.png")
click("1534813822452-2.png")
type('531826')

find("1534813840608-2.png")
click("1534813840608-2.png")
type('11112042')

find("1534813833622-2.png")
click("1534813833622-2.png")
type('12112022')

find("1534977686771-2.png")
click("1534977686771-2.png")
type('13122022')

find("1534813854863-2.png")
click("1534813854863-2.png")
type(Key.DOWN + Key.ENTER)

find("1533776396884-2.png")
click("1533776396884-2.png")

teste = "DATA DE FABRICACAO impossivel no futuro - DEVE apresentar mensagem de erro"
word(teste)

# DATA DE RECEBIMENTO

endereco()

find("1534813808104-3.png")
click("1534813808104-3.png")
type('brinco')

find("1534813813076-3.png")
click("1534813813076-3.png")
type('206')

find("1542843475777.png")
find("1542843475777.png")
type("drgherger54")

find("1534813817875-3.png")
click("1534813817875-3.png")
type('123')

find("1534813822452-3.png")
click("1534813822452-3.png")
type('531826')

find("1534813840608-3.png")
click("1534813840608-3.png")
type('11112011')

find("1534813833622-3.png")
click("1534813833622-3.png")
type('11112022')

find("1534977686771-3.png")
click("1534977686771-3.png")
type('06062018')

find("1534813854863-3.png")
click("1534813854863-3.png")
type(Key.DOWN + Key.ENTER)

find("1533776396884-3.png")
click("1533776396884-3.png")

teste = "DATA DE RECEBIMENTO impossivel no passado - DEVE apresentar mensagem de erro"
word(teste)

# DATAS

endereco()

find("1534813808104-4.png")
click("1534813808104-4.png")
type('drone')

find("1534813813076-4.png")
click("1534813813076-4.png")
type('36')

find("1542843475777.png")
find("1542843475777.png")
type("drgherger54")

find("1534813817875-4.png")
click("1534813817875-4.png")
type('123')

find("1534813822452-4.png")
click("1534813822452-4.png")
type('531826')

find("1534813840608-4.png")
click("1534813840608-4.png")
type('32121099')

find("1534813833622-4.png")
click("1534813833622-4.png")
type('33132033')

find("1534977686771-4.png")
click("1534977686771-4.png")
type('32132018')

find("1534813854863-4.png")
click("1534813854863-4.png")
type(Key.DOWN + Key.ENTER)

find("1533776396884-4.png")
click("1533776396884-4.png")

teste = "DATAS impossiveis - DEVE apresentar mensagem de erro"
word(teste)

# DATA DE VALIDADE

endereco()

find("1534813808104-5.png")
click("1534813808104-5.png")
type('mouse')

find("1534813813076-5.png")
click("1534813813076-5.png")
type('89')

find("1542843475777.png")
find("1542843475777.png")
type("drgherger54")

find("1534813817875-5.png")
click("1534813817875-5.png")
type('123')

find("1534813822452-5.png")
click("1534813822452-5.png")
type('531826')

find("1534813840608-5.png")
click("1534813840608-5.png")
type('11112017')

find("1534813833622-5.png")
click("1534813833622-5.png")
type('11102017')

find("1534977686771-5.png")
click("1534977686771-5.png")
type('06062018')

find("1534813854863-5.png")
click("1534813854863-5.png")
type(Key.DOWN + Key.ENTER)

find("1533776396884-5.png")
click("1533776396884-5.png")

teste = "DATA DE VALIDADE vencida - DEVE apresentar mensagem de erro"
word(teste)

# FORNECEDOR

endereco()

find("1534813808104-6.png")
click("1534813808104-6.png")
type('hq')

find("1534813813076-6.png")
click("1534813813076-6.png")
type('069')

find("1542843475777.png")
find("1542843475777.png")
type("drgherger54")

find("1534813817875-6.png")
click("1534813817875-6.png")
type('123')

find("1534813822452-6.png")
click("1534813822452-6.png")
type('531826')

find("1534813840608-6.png")
click("1534813840608-6.png")
type('11112011')

find("1534813833622-6.png")
click("1534813833622-6.png")
type('11112022')

find("1534977686771-6.png")
click("1534977686771-6.png")
type('06062018')

find("1533776396884-6.png")
click("1533776396884-6.png")

teste = "nao selecionar FORNECEDOR - DEVE apresentar mensagem de erro"
word(teste)

# LOTE

endereco()

find("1534813808104-7.png")
click("1534813808104-7.png")
type('pelucia')

find("1534813813076-7.png")
click("1534813813076-7.png")
type('abc')

find("1542843475777.png")
find("1542843475777.png")
type("drgherger54")

find("1534813817875-7.png")
click("1534813817875-7.png")
type('123')

find("1534813822452-7.png")
click("1534813822452-7.png")
type('531826')

find("1534813840608-7.png")
click("1534813840608-7.png")
type('11112011')

find("1534813833622-7.png")
click("1534813833622-7.png")
type('11112022')

find("1534977686771-7.png")
click("1534977686771-7.png")
type('06062018')

find("1534813854863-6.png")
click("1534813854863-6.png")
type(Key.DOWN + Key.ENTER)

find("1533776396884-7.png")
click("1533776396884-7.png")

teste = "letras inseridas no campo LOTE - DEVE apresentar mensagem de erro"
word(teste)

# NOME

endereco()

find("1534813808104-8.png")
click("1534813808104-8.png")
type('123')

find("1534813813076-8.png")
click("1534813813076-8.png")
type('06')

find("1542843475777.png")
find("1542843475777.png")
type("drgherger54")

find("1534813817875-8.png")
click("1534813817875-8.png")
type('123')

find("1534813822452-8.png")
click("1534813822452-8.png")
type('531826')

find("1534813840608-8.png")
click("1534813840608-8.png")
type('11112011')

find("1534813833622-8.png")
click("1534813833622-8.png")
type('11112022')

find("1534977686771-8.png")
click("1534977686771-8.png")
type('06062018')

find("1534813854863-7.png")
click("1534813854863-7.png")
type(Key.DOWN + Key.ENTER)

find("1533776396884-8.png")
click("1533776396884-8.png")

teste = "numeros inseridos no campo NOME - DEVE apresentar mensagem de erro"
word(teste)

# VALOR

endereco()

find("1534813808104-9.png")
click("1534813808104-9.png")
type('cal')

find("1534813813076-9.png")
click("1534813813076-9.png")
type('806')

find("1542843475777.png")
find("1542843475777.png")
type("drgherger54")

find("1534813817875-9.png")
click("1534813817875-9.png")
type('123')

find("1534813822452-9.png")
click("1534813822452-9.png")
type('00')

find("1534813840608-9.png")
click("1534813840608-9.png")
type('11112011')

find("1534813833622-9.png")
click("1534813833622-9.png")
type('11112022')

find("1534977686771-9.png")
click("1534977686771-9.png")
type('06062018')

find("1534813854863-8.png")
click("1534813854863-8.png")
type(Key.DOWN + Key.ENTER)

find("1533776396884-9.png")
click("1533776396884-9.png")

teste = "inserir zero no campo VALOR DO PRODUTO - DEVE apresentar mensagem de erro"
word(teste)

# CANCELAR

endereco()

find("1534813808104-10.png")
click("1534813808104-10.png")
type('tiara')

find("1534813813076-10.png")
click("1534813813076-10.png")
type('06')

find("1542843475777.png")
find("1542843475777.png")
type("drgherger54")

find("1534813817875-10.png")
click("1534813817875-10.png")
type('123')

find("1534813822452-10.png")
click("1534813822452-10.png")
type('531826')

find("1534813840608-10.png")
click("1534813840608-10.png")
type('11112011')

find("1534813833622-10.png")
click("1534813833622-10.png")
type('11112022')

find("1534977686771-10.png")
click("1534977686771-10.png")
type('06062018')

find("1534813854863-9.png")
click("1534813854863-9.png")
type(Key.DOWN + Key.ENTER)

find("1534201439407.png")
click("1534201439407.png")

teste = "cancelar"
word(teste)

# EXCLUIR

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
type('produto')
type(Key.DELETE)
type(Key.ENTER)

find("1534203679406.png")
click("1534203679406.png")
wait("1534203760756.png")
find("1534203719624.png")
click("1534203719624.png")

teste = "excluir"
word(teste)

# NOVO CADASTRO

if(exists("1537836711054-9.png")):
    click("1537836711054-9.png")
else:
    find("1537837616092-9.png")
    click("1537837616092-9.png")
find("1536792463168-12.png")
type('localhost')
def typeSlash():
    keyDown(Key.ALT)
    type(Key.NUM4+Key.NUM7)
    keyUp()
typeSlash()
type('projeto')
typeSlash()
type('produto')
type(Key.DELETE)
type(Key.ENTER)

find("1534201551167.png")
click("1534201551167.png")

teste = "novo cadastro"
word(teste)
click("1536795174517-1.png")

find("1538229390137.png")
click("1538229390137.png")
find("1538229412402.png")
doubleClick("1538229412402.png")
find("1538229459707.png")
click("1538229459707.png")
find("1538229509689.png")
click("1538229509689.png")
type('produto testes')
find("1538229537023.png")
click("1538229537023.png")
find("1538229937734.png")
click("1538229937734.png")
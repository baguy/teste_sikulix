# SETOR PADRAO

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
    type('setor')
    typeSlash()
    type('cadastrar')
    type(Key.ENTER)
    sleep(2)
    
endereco()

wait("1534202609484.png")
find("1534202626818.png")
click("1534202626818.png")
type('rh')
find("1533776396884.png")
click("1533776396884.png")

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
    type('setor '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    find("1537404525832-12.png")
    click("1537404525832-12.png")

teste = 'padrao'
word(teste)


# SETOR

endereco()

wait("1534202609484-1.png")
find("1534202626818-1.png")
click("1534202626818-1.png")
type(',' + Key.SHIFT)
find("1533776396884-1.png")
click("1533776396884-1.png")

teste = 'setor'
word(teste)


# CANCELAR


endereco()

wait("1534202609484-2.png")
find("1534202626818-2.png")
click("1534202626818-2.png")
type('rh')
find("1534201439407.png")
click("1534201439407.png")

teste = 'cancelar'
word(teste)


# NOVO CADASTRO


def endereco2():
    if(exists("1537836711054-11.png")):
        click("1537836711054-11.png")
    else:
        find("1537837616092-11.png")
        click("1537837616092-11.png")
    find("1536792463168-13.png")
    type('localhost')
    def typeSlash():
        keyDown(Key.ALT)
        type(Key.NUM4+Key.NUM7)
        keyUp()
    typeSlash()
    type('projeto')
    typeSlash()
    type('setor')
    type(Key.DELETE)
    type(Key.ENTER)
    sleep(2)

endereco2()

find("1534201551167.png")
click("1534201551167.png")

teste = 'novo cadastro'
word(teste)


# EXCLUIR


endereco2()

find("1534203679406.png")
click("1534203679406.png")
wait("1534203760756.png")
find("1534203719624.png")
click("1534203719624.png")

teste = 'excluir'
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
type('setor testes')
find("1538229537023-1.png")
click("1538229537023-1.png")
find("1538229937734-1.png")
click("1538229937734-1.png")
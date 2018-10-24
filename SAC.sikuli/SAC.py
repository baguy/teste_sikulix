# SAC PADRAO

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
    type('sac')
    typeSlash()
    type('cadastrar')
    type(Key.ENTER)
    sleep(2)
    
endereco()

wait("1534206605546.png")
find("1534206613535.png")
click("1534206613535.png")
type('Reclamation')
find("1534206628946.png")
click("1534206628946.png")
type(Key.DOWN + Key.ENTER)
find("1534206655764.png")
click("1534206655764.png")
type(Key.DOWN + Key.ENTER)
find("1534206664881.png")
click("1534206664881.png")
type('Problemas.')
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
    type('sac '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    find("1537404525832-12.png")
    click("1537404525832-12.png")

teste = 'padrao'
word(teste)


# TITULO


endereco()

wait("1534206605546-1.png")
find("1534206613535-1.png")
click("1534206613535-1.png")
type(',' + Key.SHIFT)
find("1534206628946-1.png")
click("1534206628946-1.png")
type(Key.DOWN + Key.ENTER)
find("1534206655764-1.png")
click("1534206655764-1.png")
type(Key.DOWN + Key.ENTER)
find("1534206664881-1.png")
click("1534206664881-1.png")
type('Problemas.')
find("1533776396884-1.png")
click("1533776396884-1.png")

teste = 'titulo'
word(teste)


# PROBLEMA


endereco()

wait("1534206605546-2.png")
find("1534206613535-2.png")
click("1534206613535-2.png")
type('Reclamation')
find("1534206628946-2.png")
click("1534206628946-2.png")
type(Key.DOWN + Key.ENTER)
find("1534206655764-2.png")
click("1534206655764-2.png")
type(Key.DOWN + Key.ENTER)
find("1534206664881-2.png")
click("1534206664881-2.png")
type(',' + Key.SHIFT + 'script')
find("1533776396884-2.png")
click("1533776396884-2.png")

teste = 'problema'
word(teste)


# CANCELAR


endereco()

wait("1534206605546-3.png")
find("1534206613535-3.png")
click("1534206613535-3.png")
type('Reclamation')
find("1534206628946-3.png")
click("1534206628946-3.png")
type(Key.DOWN + Key.ENTER)
find("1534206655764-3.png")
click("1534206655764-3.png")
type(Key.DOWN + Key.ENTER)
find("1534206664881-3.png")
click("1534206664881-3.png")
type('Problemas.')
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
    type('sac')
    type(Key.DELETE)
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
type('produto testes')
find("1538229537023-1.png")
click("1538229537023-1.png")
find("1538229937734-1.png")
click("1538229937734-1.png")
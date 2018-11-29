# PADRAO VAGA

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
    type('vaga')
    typeSlash()
    type('cadastrar')
    type(Key.ENTER)
    sleep(2)
    
endereco()


if(exists("1539217740756.png")):
    find("1539217004478.png")
    click("1539217004478.png")
    sleep(2)
    find("1534202469651.png")
    click("1534202469651.png")
    type('Rebolador')
    type(Key.TAB)
    type('62')
    find("1534202482581.png")
    click("1534202482581.png")
    type('rebolar')
    find("1538440545781.png")
    click("1538440545781.png")
    type('654321')
    find("1534202516210.png")
    click("1534202516210.png")
    type(Key.DOWN + Key.ENTER)
    find("1533776396884-6.png")
    click("1533776396884-6.png")
    endereco()
    
find("1534814792747.png")
click("1534814792747.png")
type(Key.DOWN + Key.ENTER)
find("1534202735219.png")
click("1534202735219.png")
type('11112019')
find("1534202748622.png")
click("1534202748622.png")
type('5')
find("1534202762687.png")
click("1534202762687.png")
type('Falsete')
find("1533776396884.png")
click("1533776396884.png")

def word(teste):
    sleep(2)
    type(Key.PRINTSCREEN)
    if(exists("1536795174517-11.png")):
        click("1536795174517-11.png")
    else:
        find("1538440425431-11.png")
        click("1538440425431-11.png")
        type('word' + Key.ENTER)
        sleep(2)
        wait("1537835985449-11.png")
        type(Key.ENTER)    
    type('vaga '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    find("1537404525832-12.png")
    click("1537404525832-12.png")

teste = 'padrao'
word(teste)


# CARGO


endereco()

find("1534202735219-1.png")
click("1534202735219-1.png")
type('11112019')
find("1534202748622-1.png")
click("1534202748622-1.png")
type('5')
find("1534202762687-1.png")
click("1534202762687-1.png")
type('Falsete')
find("1533776396884-1.png")
click("1533776396884-1.png")

teste = 'CARGO nao selecionado - DEVE apresentar mensagem de erro'
word(teste)


# DATA


endereco()


find("1534814792747-2.png")
click("1534814792747-2.png")
type(Key.DOWN + Key.ENTER)
find("1534202735219-2.png")
click("1534202735219-2.png")
type('32131899')
find("1534202748622-2.png")
click("1534202748622-2.png")
type('5')
find("1534202762687-2.png")
click("1534202762687-2.png")
type('Falsete')
find("1533776396884-2.png")
click("1533776396884-2.png")

teste = 'DATA impossivel - DEVE apresentar mensagem de erro'
word(teste)


# QUANTIDADE


endereco()

find("1534814792747-3.png")
click("1534814792747-3.png")
type(Key.DOWN + Key.ENTER)
find("1534202735219-3.png")
click("1534202735219-3.png")
type('11112019')
find("1534202748622-3.png")
click("1534202748622-3.png")
type('abc')
find("1534202762687-3.png")
click("1534202762687-3.png")
type('Falsete')
find("1533776396884-3.png")
click("1533776396884-3.png")

teste = 'letras no campo QUANTIDADE - DEVE apresentar mensagem de erro'
word(teste)


# REQUISITOS


endereco()

find("1534814792747-4.png")
click("1534814792747-4.png")
type(Key.DOWN + Key.ENTER)
find("1534202735219-4.png")
click("1534202735219-4.png")
type('11112019')
find("1534202748622-4.png")
click("1534202748622-4.png")
type('5')
find("1534202762687-4.png")
click("1534202762687-4.png")
type(",", Key.SHIFT)
find("1533776396884-4.png")
click("1533776396884-4.png")

teste = 'caractere especial no campo REQUISITOS - DEVE apresentar mensagem de erro'
word(teste)


# CANCELAR


endereco()

find("1534814792747-6.png")
click("1534814792747-6.png")
find("1534201439407.png")
click("1534201439407.png")

teste = 'cancelar - DEVE retornar para tela de vaga'
word(teste)


# EXCLUIR


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
    type('vaga')
    type(Key.DELETE)
    type(Key.ENTER)
    sleep(2)

endereco2()

find("1534203679406.png")
click("1534203679406.png")
wait("1534203760756.png")
find("1534203719624.png")
click("1534203719624.png")

teste = 'excluir - DEVE apresentar mensagem de confirmacao'
word(teste)


# NOVO CADASTRO


endereco2()

find("1539219913816.png")
click("1539219913816.png")

teste = 'novo cadastro'
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
type('vaga testes')
find("1538229537023-1.png")
click("1538229537023-1.png")
find("1538229937734-1.png")
click("1538229937734-1.png")
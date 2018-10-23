# PADRAO

def endereco():
    if(exists("1537836711054-8.png")):
        click("1537836711054-8.png")
    else:
        find("1537837616092-8.png")
        click("1537837616092-8.png")
    find("1536792463168-8.png")
    type('localhost')
    def typeSlash():
        keyDown(Key.ALT)
        type(Key.NUM4+Key.NUM7)
        keyUp()
    typeSlash()
    type('projeto')
    typeSlash()
    type('cargo')
    typeSlash()
    type('cadastrar')
    type(Key.ENTER)
    sleep(2)

endereco()

sleep(2)
wait("1534202461884.png")
find("1534202469651.png")
click("1534202469651.png")
type('Cantor')
type(Key.TAB)
type('40')
find("1534202482581.png")
click("1534202482581.png")
type('cantar')
find("1538440545781.png")
click("1538440545781.png")
type('1253')
find("1534202516210.png")
click("1534202516210.png")
type(Key.DOWN + Key.ENTER)
find("1533776396884.png")
click("1533776396884.png")

sleep(2)
type(Key.PRINTSCREEN)
if(exists("1536795174517-1.png")):
    click("1536795174517-1.png")
else:
    find("1538440425431.png")
    click("1538440425431.png")
    type('word' + Key.ENTER)
    wait("1537835985449.png")
    type(Key.ENTER)  
type('Cargo padrao' + Key.ENTER)
type('v', KEY_CTRL)
find("1537404525832.png")
click("1537404525832.png")

# CARGA HORÁRIA

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
type('cargo')
typeSlash()
type('cadastrar')
type(Key.ENTER)

sleep(2)
wait("1534202461884.png")
find("1534202469651.png")
click("1534202469651.png")
type('Cantor')
type(Key.TAB)
type('0')
find("1534202482581.png")
click("1534202482581.png")
type('cantar')
find("1538440545781.png")
click("1538440545781.png")
type('1253')
find("1534202516210.png")
click("1534202516210.png")
type(Key.DOWN + Key.ENTER)
find("1533776396884.png")
click("1533776396884.png")

def word(teste):
    sleep(2)
    type(Key.PRINTSCREEN)
    if(exists("1536795174517-8.png")):
        click("1536795174517-8.png")
    else:
        find("1538440425431-1.png")
        click("1538440425431-1.png")
        type('word' + Key.ENTER)
        sleep(2)
        wait("1537835985449-7.png")
        type(Key.ENTER)    
    type('cargo '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    find("1537404525832-6.png")
    click("1537404525832-6.png")

teste = 'padrao'
word(teste)


# DESCRICAO


endereco()

wait("1534202461884-1.png")
find("1534202469651-1.png")
click("1534202469651-1.png")
type('Cantor')
type(Key.TAB)
type('40')
find("1534202482581-1.png")
click("1534202482581-1.png")
type('.', Key.SHIFT)
find("1538440545781.png")
click("1538440545781.png")
type('1253')
find("1534202516210-1.png")
click("1534202516210-1.png")
type(Key.DOWN + Key.ENTER)
find("1533776396884-1.png")
click("1533776396884-1.png")

teste = 'descricao'
word(teste)


# NOME


endereco()

wait("1534202461884-2.png")
find("1534202469651-2.png")
click("1534202469651-2.png")
type('789')
type(Key.TAB)
type('55')
find("1534202482581-2.png")
click("1534202482581-2.png")
type('cantar 1,2,3...')
find("1538440545781.png")
click("1538440545781.png")
type('1253')
find("1534202516210-2.png")
click("1534202516210-2.png")
type(Key.DOWN + Key.ENTER)
find("1533776396884-2.png")
click("1533776396884-2.png")

teste = 'nome'
word(teste)


# VALOR


endereco()

wait("1534202461884-3.png")
find("1534202469651-3.png")
click("1534202469651-3.png")
type('Cantor')
type(Key.TAB)
type('55')
find("1534202482581-3.png")
click("1534202482581-3.png")
type('cantar')
find("1538440545781.png")
click("1538440545781.png")
type('0')
find("1534202516210-3.png")
click("1534202516210-3.png")
type(Key.DOWN + Key.ENTER)
find("1533776396884-3.png")
click("1533776396884-3.png")

teste = 'valor'
word(teste)


# CANCELAR


endereco()

wait("1534202461884-4.png")
find("1534202469651-4.png")
click("1534202469651-4.png")
type('Cantor')
type(Key.TAB)
type('40')
find("1534202482581-4.png")
click("1534202482581-4.png")
type('cantar')
find("1538440545781.png")
click("1538440545781.png")
type('1253')
find("1534202516210-4.png")
click("1534202516210-4.png")
type(Key.DOWN + Key.ENTER)
find("1534201439407.png")
click("1534201439407.png")

teste = 'cancelar'
word(teste)


# NOVO CADASTRO


endereco()

find("1534201551167.png")
click("1534201551167.png")

teste = 'novo cadastro'
word(teste)


# EXCLUIR


if(exists("1537836711054-6.png")):
    click("1537836711054-6.png")
else:
    find("1537837616092-6.png")
    click("1537837616092-6.png")
find("1536792463168-6.png")
type('localhost')
def typeSlash():
    keyDown(Key.ALT)
    type(Key.NUM4+Key.NUM7)
    keyUp()
typeSlash()
type('projeto')
typeSlash()
type('cargo')
type(Key.DELETE)
type(Key.ENTER)

find("1534203679406.png")
click("1534203679406.png")
wait("1534203760756.png")
find("1534203719624.png")
click("1534203719624.png")


teste = 'excluir'
word(teste)


click("1536795174517-9.png")
find("1538229390137-1.png")
click("1538229390137-1.png")
find("1538229412402-1.png")
doubleClick("1538229412402-1.png")
find("1539650165371.png")
click("1539650165371.png")
find("1538229509689-1.png")
click("1538229509689-1.png")
type('cargo testes')
find("1538229537023-1.png")
click("1538229537023-1.png")
find("1538229937734-1.png")
click("1538229937734-1.png")
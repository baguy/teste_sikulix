# AVALIAÇÃO PADRAO

def endereco():
    if(exists("1537836711054-2.png")):
        click("1537836711054-2.png")
    else:
        find("1537837616092-2.png")
        click("1537837616092-2.png")
    find("1536792463168-2.png")
    type('localhost')
    def typeSlash():
        keyDown(Key.ALT)
        type(Key.NUM4+Key.NUM7)
        keyUp()
    typeSlash()
    type('projeto')
    typeSlash()
    type('funcionario')
    type(Key.ENTER)
    sleep(2)

endereco()

find("1536798907155.png")
click("1536798907155.png")
find("1536798933052.png")
click("1536798933052.png")
find("1536798985297.png")
click("1536798985297.png")
type(Key.DOWN + Key.DOWN + Key.ENTER)
find("1536799065341.png")
click("1536799065341.png")
type(Key.DOWN + Key.DOWN + Key.ENTER)
find("1536799080873.png")
click("1536799080873.png")
type(Key.DOWN + Key.DOWN + Key.ENTER)
find("1536799097388.png")
click("1536799097388.png")
type(Key.DOWN + Key.DOWN + Key.ENTER)
find("1536799117534.png")
click("1536799117534.png")
type(Key.DOWN + Key.DOWN + Key.ENTER)
find("1536799148963.png")
click("1536799148963.png")
wait("1536800463297.png")

teste = 'padrao'

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
    type('avaliacao funcionario '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    find("1537404525832-6.png")
    click("1537404525832-6.png")

word(teste)

# EDITAR

endereco()

find("1536798907155.png")
click("1536798907155.png")

find("1536799932517.png")
click("1536799932517.png")
find("1536799080873-1.png")
click("1536799080873-1.png")
type(Key.DOWN + Key.DOWN + Key.ENTER)
find("1536799148963-1.png")
click("1536799148963-1.png")
find("1536800358822.png")
click("1536800358822.png")
wait("1536800463297-1.png")

teste = 'editar'
word(teste)


# VISUALIZAR

endereco()

find("1539651288660.png")
click("1539651288660.png")

teste = 'visualizar'
word(teste)
click("1536795174517-8.png")

find("1538229390137-1.png")
click("1538229390137-1.png")
find("1538229412402-1.png")
doubleClick("1538229412402-1.png")
find("1539650165371.png")
click("1539650165371.png")
find("1538229509689-1.png")
click("1538229509689-1.png")
type('avaliacao funcionario testes')
find("1538229537023-1.png")
click("1538229537023-1.png")
find("1538229937734-1.png")
click("1538229937734-1.png")
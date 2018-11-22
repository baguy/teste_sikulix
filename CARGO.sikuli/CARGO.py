
# NOVO CADASTRO


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
    type(Key.ENTER)
    type(Key.DELETE)
    sleep(2)

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
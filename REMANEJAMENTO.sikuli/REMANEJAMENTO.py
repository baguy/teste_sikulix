# REMANEJAMENTO PADRÃO

def endereco():
    if(exists("1537836711054-1.png")):
        click("1537836711054-1.png")
    else:
        find("1537837616092-1.png")
        click("1537837616092-1.png")
    find("1536792463168-1.png")
    type('localhost')
    def typeSlash():
        keyDown(Key.ALT)
        type(Key.NUM4+Key.NUM7)
        keyUp()
    typeSlash()
    type('projeto')
    typeSlash()
    type('remanejamento')
  
endereco()
type(Key.ENTER)
sleep(5)  

find("1542060495469.png")
click("1542060495469.png")

sleep(2)

find("1542060542228.png")
click("1542060542228.png")
type(Key.DOWN + Key.ENTER)
find("1542060596594.png")
click("1542060596594.png")
type(Key.DOWN + Key.ENTER)
find("1542060629229.png")
click("1542060629229.png")
type(Key.DOWN + Key.ENTER)
find("1542060648978.png")
click("1542060648978.png")

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
    type('Remanejamento '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    find("1537404525832-6.png")
    click("1537404525832-6.png")

word(teste)

# NÃO SELECIONAR E CANCELAR

def typeSlash():
    keyDown(Key.ALT)
    type(Key.NUM4+Key.NUM7)
    keyUp()
endereco()
def cadastrar():
    typeSlash()
    type('cadastrar')
    type(Key.ENTER) 
cadastrar()
sleep(5)

find("1542060648978.png")
click("1542060648978.png")

teste = 'sem selecionar'
word(teste)

# CANCELAR

endereco()
cadastrar()
sleep(5)

find("1542061933008.png")
click("1542061933008.png")

teste = 'cancelar'
word(teste)

# EXCLUIR

endereco()
type(Key.ENTER)

find("1542065978727.png")
click("1542065978727.png")
find("1542065998021.png")
click("1542065998021.png")

teste = 'excluir'
word(teste)

click("1536795174517-8.png")

find("1538229390137.png")
click("1538229390137.png")
find("1538229412402.png")
doubleClick("1538229412402.png")
find("1539650165371.png")
click("1539650165371.png")
find("1538229509689.png")
click("1538229509689.png")
type('remanejamento testes')
find("1538229537023.png")
click("1538229537023.png")
find("1538229937734.png")
click("1538229937734.png")
# SAC PADRAO

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
    type('sac')
    typeSlash()
    type('cadastrar')
    type(Key.ENTER)
    sleep(2)
endereco()

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

teste = 'padrao'
def word(teste):
    sleep(2)
    type(Key.PRINTSCREEN)
    if(exists("1536795174517-1.png")):
        click("1536795174517-1.png")
    else:
        find("1538440425431-7.png")
        click("1538440425431-7.png")
        type('word' + Key.ENTER)
        wait("1537835985449.png")
        type(Key.ENTER)  
    type('SAC '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    find("1537404525832.png")
    click("1537404525832.png")
word(teste)

# TITULO

endereco()

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

teste = 'caractere especial no campo TITULO DE RECLAMACAO - DEVE apresentar mensagem de erro'
word(teste)

# PROBLEMA

endereco()

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

teste = 'caractere especial no campo PROBLEMA - DEVE apresentar mensagem de erro'
word(teste)

# CANCELAR

endereco()

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

teste = 'cancelar - DEVE retornar para a tela de SAC'
word(teste)

# NOVO CADASTRO

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
type('sac')
type(Key.DELETE)
type(Key.ENTER)
sleep(2)

find("1534201551167.png")
click("1534201551167.png")

teste = 'botao novo cadastro'
word(teste)

# ATUALIZAR

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
type('sac')
type(Key.DELETE)
type(Key.ENTER)
sleep(2)

find("1542062064391.png")
click("1542062064391.png")
find(Pattern("1542062972737.png").targetOffset(-1,15))
click(Pattern("1542062972737.png").targetOffset(-1,15))
type("a", KEY_CTRL)
type("Ar condicionado")
find(Pattern("1542845174121.png").targetOffset(-1,1))
click(Pattern("1542845174121.png").targetOffset(-1,1))
type(Key.DOWN + Key.DOWN + Key.ENTER)
find(Pattern("1542063593954.png").targetOffset(-2,13))
type(Key.UP + Key.ENTER)
find(Pattern("1542063698935.png").targetOffset(-2,14))
click(Pattern("1542063698935.png").targetOffset(-2,14))
type("a", KEY_CTRL)
type("quebrado")
find("1542063761540.png")
click("1542063761540.png")
find("1534203719624.png")
click("1534203719624.png")

teste = 'atualizar cadastro - DEVE apresentar mensagem de confirmacao'
word(teste)

# RESPOSTA

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
type('sac')
type(Key.DELETE)
type(Key.ENTER)
sleep(2)

find("1542063834007.png")
click("1542063834007.png")
find("1542063876746.png")
click("1542063876746.png")
find(Pattern("1542063698935.png").targetOffset(-2,14))
click(Pattern("1542063698935.png").targetOffset(-2,14))
type("funcionando, vlw")
find("1542065040392.png")
click("1542065040392.png")
find("1542065060358.png")
click("1542065060358.png")

teste = 'enviar RESPOSTA - DEVE apresentar mensagem de confirmacao'
word(teste)

# EXCLUIR

if(exists("1537836711054-5.png")):
    click("1537836711054-5.png")
else:
    find("1537837616092-5.png")
    click("1537837616092-5.png")
find("1536792463168-5.png")
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
type(Key.ENTER)

find("1534203679406.png")
click("1534203679406.png")
wait("1534203760756.png")
find("1534203719624.png")
click("1534203719624.png")

sleep(2)
type(Key.PRINTSCREEN)
if(exists("1536795174517-6.png")):
    click("1536795174517-6.png")
else:
    find("1538440425431-12.png")
    click("1538440425431-12.png")
    type('word' + Key.ENTER)
    wait("1537835985449-5.png")
    type(Key.ENTER)  
type('SAC excluir  - DEVE apresentar mensagem de confirmacao' + Key.ENTER)
type('v', KEY_CTRL)

find("1538229390137.png")
click("1538229390137.png")
find("1538229412402.png")
doubleClick("1538229412402.png")
find("1538229459707.png")
click("1538229459707.png")
find("1538229509689.png")
click("1538229509689.png")
type('sac testes')
find("1538229537023.png")
click("1538229537023.png")
find("1538229937734.png")
click("1538229937734.png")
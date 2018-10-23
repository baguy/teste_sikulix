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
    type('agenda')
    type(Key.ENTER)
    sleep(2)

endereco()

wait("1537402775994.png")

find("1538225313309.png")
click("1538225313309.png")

wait("1537402944469.png")
find("1537402956612.png")
click("1537402956612.png")
type('Palestra')
type(Key.TAB)
find("1537403076265.png")
click("1537403076265.png")
type(Key.DOWN + Key.ENTER)
find("1537403093452.png")
click("1537403093452.png")
type(Key.TAB)
type('22')
type(Key.TAB + Key.TAB)
find("1537403122936.png")
click("1537403122936.png")
type(Key.TAB)
type('10')

find("1537403883554.png")
click("1537403883554.png")

teste = 'padrao'

def word(teste):
    sleep(2)
    type(Key.PRINTSCREEN)
    if(exists("1536795174517-8.png")):
        click("1536795174517-8.png")
    else:
        find("1538440425431-8.png")
        click("1538440425431-8.png")
        type('word' + Key.ENTER)
        sleep(2)
        wait("1537835985449-8.png")
        type(Key.ENTER)    
    type('agenda '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    find("1537404525832-7.png")
    click("1537404525832-7.png")

word(teste)

# COR

endereco()

wait("1537402775994-1.png")

find("1538225313309-1.png")
click("1538225313309-1.png")

wait("1537402944469-1.png")
find("1537402956612-1.png")
click("1537402956612-1.png")
type('Palestra')
type(Key.TAB)

find("1537403093452-1.png")
click("1537403093452-1.png")
type(Key.TAB)
type('22')
type(Key.TAB + Key.TAB)
find("1537403122936-1.png")
click("1537403122936-1.png")
type(Key.TAB)
type('10')

find("1537403883554-1.png")
click("1537403883554-1.png")

teste = 'cor nao selecionada'
word()

# DIA

endereco()

wait("1537402775994-2.png")

find("1538225313309-2.png")
click("1538225313309-2.png")

wait("1537402944469-2.png")
find("1537402956612-2.png")
click("1537402956612-2.png")
type('Palestra')
type(Key.TAB)
find("1537403076265-1.png")
click("1537403076265-1.png")
type(Key.DOWN + Key.ENTER)
find("1537403093452-2.png")
click("1537403093452-2.png")
type(Key.TAB)
type('22')
type(Key.TAB)
find("1537403122936-2.png")
type('15012000')
type(Key.TAB)
type('10')

find("1537403883554-2.png")
click("1537403883554-2.png")

teste = 'dia'
word(teste)

# DATAS IMPOSSIVEIS

endereco()
wait("1537402775994-3.png")

find("1538225313309-3.png")
click("1538225313309-3.png")

wait("1537402944469-3.png")
find("1537402956612-3.png")
click("1537402956612-3.png")
type('Palestra')
type(Key.TAB)
find("1537403076265-2.png")
click("1537403076265-2.png")
type(Key.DOWN + Key.ENTER)
type(Key.TAB)
type('32131750')
type(Key.TAB)
type('22')
type(Key.TAB)
type('32131752')
type(Key.TAB)
type('10')

find("1537403883554-3.png")
click("1537403883554-3.png")

teste = 'datas impossiveis'
word(teste)

# HORARIO

endereco()

wait("1537402775994-4.png")

find("1538225313309-4.png")
click("1538225313309-4.png")

wait("1537402944469-4.png")
find("1537402956612-4.png")
click("1537402956612-4.png")
type('Palestra')
type(Key.TAB)
find("1537403076265-3.png")
click("1537403076265-3.png")
type(Key.DOWN + Key.DOWN + Key.ENTER)
find("1537403093452-3.png")
click("1537403093452-3.png")
type(Key.TAB)
type('22')
type(Key.TAB)
find("1537403122936-3.png")
type(Key.LEFT + Key.DELETE + Key.DELETE)
type('28')
type(Key.TAB)
type('10')

find("1537403883554-4.png")
click("1537403883554-4.png")

teste = 'horario'
word(teste)

# HORARIOS IMPOSSIVEIS

endereco()

wait("1537402775994-5.png")

find("1538225313309-5.png")
click("1538225313309-5.png")

wait("1537402944469-5.png")
find("1537402956612-5.png")
click("1537402956612-5.png")
type('Palestra')
type(Key.TAB)
find("1537403076265-4.png")
click("1537403076265-4.png")
type(Key.DOWN + Key.DOWN + Key.ENTER)
find("1537403093452-4.png")
click("1537403093452-4.png")
type(Key.TAB)
type('2562')
type(Key.TAB)
find("1537403122936-4.png")
type(Key.LEFT + Key.DELETE + Key.DELETE)
type('28')
type(Key.TAB)
type('2663')

find("1537403883554-5.png")
click("1537403883554-5.png")

teste = 'horarios impossiveis'
word(teste)

# TITULO

endereco()

wait("1537402775994-6.png")

find("1538225313309-6.png")
click("1538225313309-6.png")
wait("1537402944469-6.png")
find("1537402956612-6.png")
click("1537402956612-6.png")
type(',', Key.SHIFT)
type(Key.TAB)
find("1537403076265-5.png")
click("1537403076265-5.png")
type(Key.DOWN + Key.ENTER)
find("1537403093452-5.png")
click("1537403093452-5.png")
type(Key.TAB)
type('22')
type(Key.TAB + Key.TAB)
find("1537403122936-5.png")
click("1537403122936-5.png")
type(Key.TAB)
type('10')

find("1537403883554-6.png")
click("1537403883554-6.png")

teste = 'titulo'
word(teste)

# EXCLUIR

endereco()

wait("1537402775994-7.png")

find("1538226902478.png")
click("1538226902478.png")

wait("1538226921497.png")

find("1538226940200.png")
click("1538226940200.png")

find("1538226969720.png")
click("1538226969720.png")

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
type('agenda testes')
find("1538229537023.png")
click("1538229537023.png")
find("1538229937734.png")
click("1538229937734.png")
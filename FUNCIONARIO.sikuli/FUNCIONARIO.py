# FUNCIONARIO PADRAO

def endereco():
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
    type('funcionario')
    typeSlash()
    type('cadastrar')
    type(Key.ENTER)
    sleep(2)
    
endereco()

find("1534200917845.png")
click("1534200917845.png")
type('Alex')
find("1534200935479.png")
click("1534200935479.png")
type('alex@marte.com.mr')
find("1534201017178.png")
click("1534201017178.png")
type('11112002')
find("1534201034187.png")
click(Pattern("1534201034187.png").targetOffset(9,1))
find("1534201062010.png")
click("1534201062010.png")
type('37737259813')
find("1534201080186.png")
click("1534201080186.png")
type('12555555555')
find("1534201098496.png")
click("1534201098496.png")
type('11665030')
find("1534201189066.png")
click("1534201189066.png")
type('123')
find("1534201204889.png")
click("1534201204889.png")
type('2 quadras do upa')
find("1533776396884.png")
click("1533776396884.png")

def word(teste):
    sleep(2)
    type(Key.PRINTSCREEN)
    if(exists("1536795174517-7.png")):
        click("1536795174517-7.png")
    else:
        find("1538440425431-6.png")
        click("1538440425431-6.png")
        type('word' + Key.ENTER)
        sleep(2)
        wait("1537835985449-6.png")
        type(Key.ENTER)    
    type('funcionario '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    find("1537404525832-6.png")
    click("1537404525832-6.png")

teste = 'padrao'
word(teste)


# NOME


endereco()

find("1534200917845-1.png")
click("1534200917845-1.png")
type('123')
find("1534200935479-1.png")
click("1534200935479-1.png")
type('alex@plutao.com.pl')
find("1534201017178-1.png")
click("1534201017178-1.png")
type('11112002')
find("1534201034187-1.png")
click(Pattern("1534201034187-1.png").targetOffset(9,1))
find("1534201062010-1.png")
click("1534201062010-1.png")
type('37737259813')
find("1534201080186-1.png")
click("1534201080186-1.png")
type('12555555555')
find("1534201098496-1.png")
click("1534201098496-1.png")
type('11665030')
find("1534201189066-1.png")
click("1534201189066-1.png")
type('123')
find("1534201204889-1.png")
click("1534201204889-1.png")
type('2 quadras do upa')
find("1533776396884-1.png")
click("1533776396884-1.png")

teste = 'nome'
word(teste)


# EMAIL


endereco()

find("1534200917845-2.png")
click("1534200917845-2.png")
type('Alex')
find("1534200935479-2.png")
click("1534200935479-2.png")
type('alex.marte.com.mr')
find("1534201017178-2.png")
click("1534201017178-2.png")
type('11112002')
find("1534201034187-2.png")
click(Pattern("1534201034187-2.png").targetOffset(9,1))
find("1534201062010-2.png")
click("1534201062010-2.png")
type('37737259813')
find("1534201080186-2.png")
click("1534201080186-2.png")
type('12555555555')
find("1534201098496-2.png")
click("1534201098496-2.png")
type('11665030')
find("1534201189066-2.png")
click("1534201189066-2.png")
type('123')
find("1534201204889-2.png")
click("1534201204889-2.png")
type('2 quadras do upa')
find("1533776396884-2.png")
click("1533776396884-2.png")

teste = 'email'
word(teste)


# BAIRRO


endereco()

find("1534200917845-3.png")
click("1534200917845-3.png")
type('Spock')
find("1534200935479-3.png")
click("1534200935479-3.png")
type('spock@enterprise.uss')
find("1534201017178-3.png")
click("1534201017178-3.png")
type('11112002')
find("1534201034187-3.png")
click(Pattern("1534201034187-3.png").targetOffset(9,1))
find("1534201062010-3.png")
click("1534201062010-3.png")
type('37737259813')
find("1534201080186-3.png")
click("1534201080186-3.png")
type('12555555555')
find("1534201098496-3.png")
click("1534201098496-3.png")
type('11665030')
type(Key.TAB + Key.TAB + Key.TAB)
type(",", Key.SHIFT)
find("1534201189066-3.png")
click("1534201189066-3.png")
type('123')
find("1534201204889-3.png")
click("1534201204889-3.png")
type('2 quadras do upa')
find("1533776396884-3.png")
click("1533776396884-3.png")

teste = 'bairro'
word(teste)


# DATA DE NASCIMENTO


endereco()

find("1534200917845-4.png")
click("1534200917845-4.png")
type('Alex')
find("1534200935479-4.png")
click("1534200935479-4.png")
type('alex@venus.com.vn')
find("1534201017178-4.png")
click("1534201017178-4.png")
type('32132032')
find("1534201034187-4.png")
click(Pattern("1534201034187-4.png").targetOffset(9,1))
find("1534201062010-4.png")
click("1534201062010-4.png")
type('37737259813')
find("1534201080186-4.png")
click("1534201080186-4.png")
type('12555555555')
find("1534201098496-4.png")
click("1534201098496-4.png")
type('11665030')
find("1534201189066-4.png")
click("1534201189066-4.png")
type('123')
find("1534201204889-4.png")
click("1534201204889-4.png")
type('2 quadras do upa')
find("1533776396884-4.png")
click("1533776396884-4.png")

teste = 'data de nascimento'
word(teste)


# CPF


endereco()

find("1534200917845-5.png")
click("1534200917845-5.png")
type('Alex')
find("1534200935479-5.png")
click("1534200935479-5.png")
type('alex@jupiter.com.jp')
find("1534201017178-5.png")
click("1534201017178-5.png")
type('11112002')
find("1534201034187-5.png")
click(Pattern("1534201034187-5.png").targetOffset(9,1))
find("1534201062010-5.png")
click("1534201062010-5.png")
type('abc11111111111')
find("1534201080186-5.png")
click("1534201080186-5.png")
type('12555555555')
find("1534201098496-5.png")
click("1534201098496-5.png")
type('11665030')
find("1534201189066-5.png")
click("1534201189066-5.png")
type('123')
find("1534201204889-5.png")
click("1534201204889-5.png")
type('2 quadras do upa')
find("1533776396884-5.png")
click("1533776396884-5.png")

teste = 'cpf'
word(teste)


# EXCLUIR


def endereco2():
    if(exists("1537836711054-7.png")):
        click("1537836711054-7.png")
    else:
        find("1537837616092-7.png")
        click("1537837616092-7.png")
    find("1536792463168-7.png")
    type('localhost')
    def typeSlash():
        keyDown(Key.ALT)
        type(Key.NUM4+Key.NUM7)
        keyUp()
    typeSlash()
    type('projeto')
    typeSlash()
    type('funcionario')
    type(Key.DELETE)
    sleep(2)

endereco2()

find("1538442504462.png")
click("1538442504462.png")
find("1538442523671.png")
click("1538442523671.png")

teste = 'excluir'
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
type('funcionario testes')
find("1538229537023-1.png")
click("1538229537023-1.png")
find("1538229937734-1.png")
click("1538229937734-1.png")
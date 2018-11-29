# CLIENTE PADRÃO

def endereco():
    if(exists("1537836711054-11.png")):
        click("1537836711054-11.png")
    else:
        find("1537837616092-11.png")
        click("1537837616092-11.png")
    find("1536792463168-11.png")
    type('localhost')
    def typeSlash():
        keyDown(Key.ALT)
        type(Key.NUM4+Key.NUM7)
        keyUp()
    typeSlash()
    type('projeto')
    typeSlash()
    type('cliente')
    typeSlash()
    type('cadastrar')
    type(Key.ENTER)
    sleep(2)

endereco()

find("1534200917845.png")
click("1534200917845.png")
type('Maria')
find("1534200935479.png")
click("1534200935479.png")
type('maria@netuno.com.br')
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
    if(exists("1536795174517-12.png")):
        click("1536795174517-12.png")
    else:
        find("1538440425431-1.png")
        click("1538440425431-1.png")
        type('word' + Key.ENTER)
        sleep(2)
        wait("1537835985449-11.png")
        type(Key.ENTER)    
    type('cliente '+ teste + Key.ENTER)
    type('v', KEY_CTRL)
    type(Key.ENTER)
    find("1537404525832-12.png")
    click("1537404525832-12.png")

teste = 'padrao'
word(teste)


# CANCELAR


endereco()

find("1534200917845-1.png")
click("1534200917845-1.png")
type('Maria')
find("1534200935479-1.png")
click("1534200935479-1.png")
type('maria@netuno.com.br')
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
find("1534201439407.png")
click("1534201439407.png")

teste = 'botao cancelar'
word(teste)


# COMPLEMENTO


endereco()

find("1534200917845-2.png")
click("1534200917845-2.png")
type('Maria')
find("1534200935479-2.png")
click("1534200935479-2.png")
type('maria@netuno.com.nt')
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
find("1534201204889-1.png")
click("1534201204889-1.png")
type(',', Key.SHIFT)
find("1533776396884-1.png")
click("1533776396884-1.png")

teste = 'caractere especial - menor - inserido no campo COMPLEMENTO - DEVE apresentar mensagem de erro'
word(teste)


# CPF


endereco()

find("1534200917845-3.png")
click("1534200917845-3.png")
type('Aragon')
find("1534200935479-3.png")
click("1534200935479-3.png")
type('rei@gondor.tm')
find("1534201017178-3.png")
click("1534201017178-3.png")
type('11112000')
find("1534201034187-3.png")
click(Pattern("1534201034187-3.png").targetOffset(9,1))
find("1534201062010-3.png")
click("1534201062010-3.png")
type('11227259815')
find("1534201080186-3.png")
click("1534201080186-3.png")
type('12555555555')
find("1534201098496-3.png")
click("1534201098496-3.png")
type('11665030')
find("1534201189066-3.png")
click("1534201189066-3.png")
type('123')
find("1534201204889-2.png")
click("1534201204889-2.png")
type('2 quadras do upa')
find("1533776396884-2.png")
click("1533776396884-2.png")

teste = 'CPF invalido - DEVE apresentar mensagem de erro'
word(teste)


# DATA DE NASCIMENTO


endereco()

sleep(2)

find("1534200917845-4.png")
click("1534200917845-4.png")
type('Aragon')
find("1534200935479-4.png")
click("1534200935479-4.png")
type('rei@gondor.terramedia.gr')
find("1534201017178-4.png")
click("1534201017178-4.png")
type('11112032')
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
find("1534201204889-3.png")
click("1534201204889-3.png")
type('2 quadras do upa')
find("1533776396884-3.png")
click("1533776396884-3.png")

teste = 'DATA de nascimento invalida - DEVE apresentar mensagem de erro'
word(teste)


# EMAIL


endereco()

find("1534200917845-5.png")
click("1534200917845-5.png")
type('Aragon')
find("1534200935479-5.png")
click("1534200935479-5.png")
type('www.reigondor.com.br')
find("1534201017178-5.png")
click("1534201017178-5.png")
type('11112002')
find("1534201034187-5.png")
click(Pattern("1534201034187-5.png").targetOffset(9,1))
find("1534201062010-5.png")
click("1534201062010-5.png")
type('37737259813')
find("1534201080186-5.png")
click("1534201080186-5.png")
type('12555555555')
find("1534201098496-5.png")
click("1534201098496-5.png")
type('11665030')
find("1534201189066-5.png")
click("1534201189066-5.png")
type('123')
find("1534201204889-4.png")
click("1534201204889-4.png")
type('2 quadras do upa')
find("1533776396884-4.png")
click("1533776396884-4.png")

teste = 'EMAIL invalido - DEVE apresentar mensagem de erro'
word(teste)


# LETRAS EM CAMPOS NUMÉRICOS


endereco()


find("1534200917845-6.png")
click("1534200917845-6.png")
type('Gwendolyn')
find("1534200935479-6.png")
click("1534200935479-6.png")
type('gwen@gondor.com.tm')
find("1534201017178-6.png")
click("1534201017178-6.png")
type('abc')
find("1534201034187-6.png")
click(Pattern("1534201034187-6.png").targetOffset(9,1))
find("1534201062010-6.png")
click("1534201062010-6.png")
type('abc')
find("1534201080186-6.png")
click("1534201080186-6.png")
type('abc')
find("1534201098496-6.png")
click("1534201098496-6.png")
type('abc')
find("1534201189066-6.png")
click("1534201189066-6.png")
type('abc')
find("1534201204889-5.png")
click("1534201204889-5.png")
type('2 quadras do upa')
find("1533776396884-5.png")
click("1533776396884-5.png")

teste = 'letras em campos numericos - DEVE apresentar mensagem de erro'
word(teste)


# NOME


endereco()

find("1534200917845-7.png")
click("1534200917845-7.png")
type('123')
find("1534200935479-7.png")
click("1534200935479-7.png")
type('maria@netuno.com.pl')
find("1534201017178-7.png")
click("1534201017178-7.png")
type('11112002')
find("1534201034187-7.png")
click(Pattern("1534201034187-7.png").targetOffset(9,1))
find("1534201062010-7.png")
click("1534201062010-7.png")
type('37737259813')
find("1534201080186-7.png")
click("1534201080186-7.png")
type('12555555555')
find("1534201098496-7.png")
click("1534201098496-7.png")
type('11665030')
find("1534201189066-7.png")
click("1534201189066-7.png")
type('123')
find("1534201204889-6.png")
click("1534201204889-6.png")
type('2 quadras do upa')
find("1533776396884-6.png")
click("1533776396884-6.png")

teste = 'numeros inseridos no campo NOME - DEVE apresentar mensagem de erro'
word(teste)


# TELEFONE


endereco()

find("1534200917845-8.png")
click("1534200917845-8.png")
type('Aragon')
find("1534200935479-8.png")
click("1534200935479-8.png")
type('rei@gondor.com.sr')
find("1534201017178-8.png")
click("1534201017178-8.png")
type('11112002')
find("1534201034187-8.png")
click(Pattern("1534201034187-8.png").targetOffset(9,1))
find("1534201062010-8.png")
click("1534201062010-8.png")
type('37737259813')
find("1534201080186-8.png")
click("1534201080186-8.png")
type('DDD(12) 55555-5555')
find("1534201098496-8.png")
click("1534201098496-8.png")
type('11665030')
find("1534201189066-8.png")
click("1534201189066-8.png")
type('123')
find("1534201204889-7.png")
click("1534201204889-7.png")
type('2 quadras do upa')
find("1533776396884-7.png")
click("1533776396884-7.png")

teste = 'letras inseridas no campo TELEFONE - DEVE ignorar letras'
word(teste)


# NOVO CADASTRO

def endereco2():    
    if(exists("1537836711054-10.png")):
        click("1537836711054-10.png")
    else:
        find("1537837616092-10.png")
        click("1537837616092-10.png")
    find("1536792463168-10.png")
    type('localhost')
    def typeSlash():
        keyDown(Key.ALT)
        type(Key.NUM4+Key.NUM7)
        keyUp()
    typeSlash()
    type('projeto')
    typeSlash()
    type('cliente')
    type(Key.DELETE)
    type(Key.ENTER)

endereco2()

find("1538438138577.png")
click("1538438138577.png")

teste = 'botao novo cadastro'
word(teste)


# EXCLUIR


endereco2()

find("1534203679406.png")
click("1534203679406.png")
wait("1534203760756.png")
find("1534203719624.png")
click("1534203719624.png")

teste = 'excluir - DEVE apresentar mensagem de confirmacao'
word(teste)

click("1536795174517-14.png")
find("1538229390137-1.png")
click("1538229390137-1.png")
find("1538229412402-1.png")
doubleClick("1538229412402-1.png")
find("1539650165371.png")
click("1539650165371.png")
find("1538229509689-1.png")
click("1538229509689-1.png")
type('cliente testes')
find("1538229537023-1.png")
click("1538229537023-1.png")
find("1538229937734-1.png")
click("1538229937734-1.png")
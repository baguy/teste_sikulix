# teste_sikulix

# Passo a passo: Como usar os testes do Sikulix com o projeto Lambda ERP

### CRM/HRM criado pelos alunos do Instituto Federal de São Paulo campus Caraguatatuba (2018)
#### Tutorial: Mayra Dantas Bueno

## Sumário
- Passo 01 - Iniciando o projeto
- Passo 02 - Login
- Passo 03 - Sikulix
- Passo 04 - Abrir testes
- Passo 05 - Executar testes
- Passo 06 - Relatórios
- Observações

## Passo 01 - Iniciando o projeto
Certifique-se de que a pasta do projeto esteja na pasta htdocs do servidor local (o servidor usado para o projeto foi o XAMPP). Inicie o servidor local e dê _Start_ no Apache e no MySQL.

## Passo 02 - Login
- Acesse o projeto localmente digitando na barra de endereço do navegador: localhost/projeto
- Depois, clique em "Login"
- Em seguida, insira e-mail e senha. Preferencialmente, logar como administrador do sistema para ter acesso a todos os formulários.
  - Login padrão:
  - e-mail: admin@admin.com
  - senha: admin

## Passo 03 - Sikulix
Baixe o Sikulix, instale-o e abra-o.
  - Para download: [clique aqui](http://sikulix.com/)
  
Para mais detalhes sobre o Sikulix e como usá-lo: [acesse o tutorial](https://github.com/baguy/Tutorial_Sikuli/blob/master/tutorial_sikulix.md).

## Passo 04 - Abrir testes
- Acessar os testes no [github](https://github.com/baguy/teste_sikulix). Fazer download ou clonar.
- Na IDE do Sikulix, clicar em _Arquivo_ e em _Abrir..._ (ctrl+o).
- Selecionar pasta do teste que deseja rodar.

## Passo 05 - Executar testes
Clique no botão Executar no topo da IDE.

## Passo 06 - Relatórios
A cada término de rotina do teste, será gerado um relatório em documento Word com capturas de tela dos resultados. Os relatórios devem ser analisados.

## Observações
- O teste foi configurado para rodar no navegador Chrome, pois o Sikulix busca o símbolo de nova aba e barra de endereço do navegador para abrir a página do projeto. Caso seja necessário rodar em outro navegador, configurar apropriadamente em todos os testes.
- Atentar-se para a resolução da tela em que o teste será rodado. Mais detalhes no [tutorial](https://github.com/baguy/Tutorial_Sikuli/blob/master/tutorial_sikulix.md).
- Caso as rotas do projeto sejam mudadas, atentar-se para mudá-las nas funções endereço() em cada rotina de teste.
- O computador deve ter memória livre suficiente para o teste rodar normalmente. Caso contrário, o programa poderá fechar ou apresentar erro.

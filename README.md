DOCUMENTAÇÃO DO PROJETO
Arquivos de códigos-fonte presentes
main.py - executa todo o código fonte.
analisadorSintatico.py - contém o arquivo do analisador sintático.
analisadorLexico.py - contém o código analisador Léxico.
exemplo1.txt - contém um arquivo de programa a ser analisado.
exemplo2.txt - contém um arquivo de programa inválido a ser analisado.
fases de desenvolvimento
Parte 1 - Analisador Léxico.
parte 2 - Analisador Sintático.
parte 3 - Analisador Semântico.
DESENVOLVIMENTO
Foi implementado um analisador léxico para a seguinte tabela de símbolos

Palavra Token	Expressão regular correspondente
KeyWords	if then else write read integer real program begin end
Identificadores	(Letra)*
Numero	(Digito)*
Letra	a..z
Dígito	0..9
Operadores	= < <= <> > >= := 
Símbolos	; , : $ ( ) { } [ ]
regras Léxicas
seguinte o autômato abaixo:

Autômato Analisador Léxico



Gramática Livre de Contexto da Linguagem - Forma BNF
<programa> -> program ident <corpo> .

<corpo> -> <dc> begin <comandos> end

<dc> -> <dc_v> <mais_dc> | λ

<mais_dc> -> ; <dc> | λ

<dc_v> -> <tipo_var> : <variaveis>  {addtype(id.entry, T.type) }

<tipo_var> -> real | integer

<variaveis> -> ident <mais_var>

<mais_var> -> , <variaveis> | λ

<comandos> -> <comando> <mais_comandos>

<mais_comandos> -> ; <comandos> | λ

<comando> -> read (ident) |write (ident) |ident := <expressao> |if <condicao> then <comandos> <pfalsa> $

<condicao> -> <expressao> <relacao> <expressao>

<relacao> -> = | <> | >= | <= | > | <

<expressao> -> <termo> <outros_termos>

<termo> -> <op_un> <fator> <mais_fatores>

<op_un> -> - | λ

<fator> -> ident | numero_int | numero_real | (<expressao>)

<outros_termos> -> <op_ad> <termo>

<outros_termos> | λ

<op_ad> -> + | -

<mais_fatores> -> <op_mul> <fator>

<mais_fatores> | λ

<op_mul> -> * | /

<pfalsa> -> else <comandos> | λ

Analise sintática:
para análise Semântica foram adicionadas as seguintes regras

atribuir tipo ao identificador na tabela de simbolos
verificar se um identificador foi declarada para ser usada.
garantir unicidade de identificador
verificar variaveis utilizadas


Informações Gerais:
O analisador sintático construído foi do tipo Descendente Preditivo Recursivo. Para cada símbolo não-terminal da gramática, uma nova função foi construída. As produções da gramática foram representadas por chamadas sucessivas dessas funções.
Quando um erro léxico ou Sintático ou Semântico é encontrado o programa é parado imediatamente uma vez que o analisador sintático pode encontrar erros em cascata devido ao erro inicial. e para os erros Sintáticos e semânticos é colocado no arquivo o erro e a linha onde este se encontra.
o programa main.py ao iniciar ira procurar todos os arquivos com extensão  .txt e irá tentar compilar cada um deles, gerando uma saida individual para cada uma das entradas encontradas onde constará as funções ou seja  cada símbolo não-terminal da gramática ou os possiveis erros. (entrada.txt) -> (entrada_saida.txt).
No emulador terminal serão printados cada uma das funções ou seja  cada símbolo não-terminal da gramática.
por fim se o arquivo estiver de acordo com a linguagem é printado uma mensagem de sucesso tanto no arquivo quanto no emulador.

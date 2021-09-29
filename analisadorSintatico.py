from os import scandir
from analisadorSemantico import *

class AnalisadorSintatico:
    simbolo =""
    LINHA = 1
    def __init__(self,path):
        self.scan = ScannerLexema(path)

    def obtemSimbolo(self):
        self.token = self.scan.NextToken()
        self.simbolo = None
        if self.token != None:
             self.simbolo = self.token
    
    def analise(self):
        self.obtemSimbolo()
        self.programa()
        if self.simbolo is None:
            print("tudo Certo")
        else:
            raise Exception('Erro sintatico, esperado fim de cadeia LINHA:' + str(self.scan.LINHA))

    def programa(self):
        if self.simbolo.termo == "program":
            self.obtemSimbolo()
            if self.simbolo.tipo == "ident":
                self.obtemSimbolo()
                self.corpo()
            else:
                raise Exception('Erro sintatico, esperado ident LINHA:' + str(self.scan.LINHA))
        else:
            raise Exception('Erro sintatico, esperado program LINHA:' + str(self.scan.LINHA))
    
    def corpo(self):
        self.dc()
        if self.simbolo.termo == "begin":
            self.obtemSimbolo()
            self.comandos()
            if self.simbolo.termo == "end":
                self.obtemSimbolo()
            else:
                raise Exception('Erro sintatico, esperado "end" LINHA:' + str(self.scan.LINHA))
        else:
            raise Exception('Erro sintatico, esperado "begin" LINHA:' + str(self.scan.LINHA))
    
    def dc(self):
        if self.simbolo.tipo == "tipo_var":
            self.dcV()
            self.maisDc()
        else :
            pass
    
    def maisDc(self):
        if self.simbolo.tipo == ";":
            self.obtemSimbolo()
            self.dc()
        else:
            pass


    def dcV(self):
        if self.simbolo.tipo == "tipo_var":
            self.obtemSimbolo()
            if self.simbolo.termo == ":":
                self.obtemSimbolo()
                self.variaveis()
                self.obtemSimbolo
            else:
                raise Exception('Erro sintatico, esperado ":" LINHA:' + str(self.scan.LINHA))
        else :
            pass

    def comandos(self):
        self.comando()
        self.maisComandos()
    
    def maisComandos(self):
        if self.simbolo.termo == ";":
            self.obtemSimbolo()
            self.comandos()
        else:
            pass

    def parIdent(self):
        if self.simbolo.termo == "(":
            self.obtemSimbolo()
            if self.simbolo.tipo == "ident":
                self.obtemSimbolo()
                if self.simbolo.termo == ")":
                    self.obtemSimbolo()
                else:
                    raise Exception('Erro sintatico, esperado ")" LINHA:' + str(self.scan.LINHA))
            else:
                raise Exception('Erro sintatico, esperado "ident" LINHA:' + str(self.scan.LINHA))
        else:
            raise Exception('Erro sintatico, esperado "(" LINHA:' + str(self.scan.LINHA))

    def atribuirVal(self):
        if self.simbolo.termo == ":":
            self.obtemSimbolo()
            if self.simbolo.termo == "=":
                    self.obtemSimbolo()
                    self.expressao()
            else:
                raise Exception('Erro sintatico, esperado "=" LINHA:' + str(self.scan.LINHA))
        else:
            raise Exception('Erro sintatico, esperado ":" LINHA:' + str(self.scan.LINHA))

    def condicional(self):
        self.condicao()
        if self.simbolo.termo == "then":
            self.obtemSimbolo()
            self.comandos()
            self.pFalsa()
            if self.simbolo.termo == "$":
                self.obtemSimbolo()
            else:
                raise Exception('Erro sintatico, esperado "$" LINHA:' + str(self.scan.LINHA))
        else:
            raise Exception('Erro sintatico, esperado "then" LINHA:' + str(self.scan.LINHA))

    def pFalsa(self):
        if self.simbolo.termo == "else":
            self.obtemSimbolo()
            self.comandos()
        else:
            pass

    def condicao(self):
        self.expressao()
        self.relacao()
        self.expressao()

    def relacao(self):
        if self.simbolo.termo == "=":
            self.obtemSimbolo()
        elif self.simbolo.termo == "<":
            self.obtemSimbolo()
            if self.simbolo.termo == ">":
                self.obtemSimbolo()
            if self.simbolo.termo == "=":
                self.obtemSimbolo()
            else:
                pass
        elif self.simbolo.termo == ">":
            self.obtemSimbolo()
            if self.simbolo.termo == "=":
                self.obtemSimbolo()
            else:
                pass
        else:
            raise Exception('Erro sintatico, esperado "operador" LINHA:' + str(self.scan.LINHA))


    def expressao(self):
        self.termo()
        self.outrosTermos()

    def termo(self):
        self.opUn()
        self.fator()
        self.maisFatores()

    def opUn(self):
        if self.simbolo.termo == "-":
            self.obtemSimbolo()
        else:
            pass
    
    def outrosTermos(self):
        if self.simbolo.termo == "+" or self.simbolo.termo == "-":
            self.opAd()
            self.fator()
            self.maisFatores()
        else:
            pass

    def opAd(self):
        if self.simbolo.termo == "+":
            self.obtemSimbolo()
        elif self.simbolo.termo == "-":
            self.obtemSimbolo()
        else:
            raise Exception('Erro sintatico, esperador "+" ou operador "-" LINHA:' + str(self.scan.LINHA))

    def opMul(self):
        if self.simbolo.termo == "*":
            self.obtemSimbolo()
        elif self.simbolo.termo == "/":
            self.obtemSimbolo()
        else:
            raise Exception('Erro sintatico, esperador "+" ou operador "-" LINHA:' + str(self.scan.LINHA))

    def maisFatores(self):
        if self.simbolo.termo == "*":
            self.opMul()
            self.fator()
            self.maisFatores()
        else:
            pass
    
    def fator(self):
        if self.simbolo.tipo == "ident":
            self.obtemSimbolo()
        elif self.simbolo.tipo == "numero_int":
            self.obtemSimbolo()
        elif self.simbolo.tipo == "numero_real":
            self.obtemSimbolo()
        elif self.simbolo.termo == "(":
            self.obtemSimbolo()
            self.expressao()
            if self.simbolo.termo == ")":
                self.obtemSimbolo()
            else:
                raise Exception('Erro sintatico, esperado ")" LINHA:' + str(self.scan.LINHA))
        else:
            raise Exception('Erro sintatico, esperado "expressao" LINHA:' + str(self.scan.LINHA))
                
        

    def comando(self):
        if self.simbolo.termo == "read":
            self.obtemSimbolo()
            self.parIdent()
        elif self.simbolo.termo == "write":
            self.obtemSimbolo()
            self.parIdent()
        elif self.simbolo.tipo == "ident":
            self.obtemSimbolo()
            self.atribuirVal()
        elif self.simbolo.tipo == "if":
            self.obtemSimbolo()
            self.condicional()
        else:
            raise Exception('Erro sintatico, esperado "comando" LINHA:' + str(self.scan.LINHA))   

    
    def variaveis(self):
        if self.simbolo.tipo == "ident":
            self.obtemSimbolo()
            self.maisVar()
        else:
            raise Exception('Erro sintatico, esperado "ident" LINHA:' + str(self.scan.LINHA))
    
    def maisVar(self):
        if self.simbolo.tipo == ",":
             self.obtemSimbolo()
             self.variaveis()
        else:
            pass
    

sintatico = AnalisadorSintatico(r'entradas.txt')
sintatico.analise()
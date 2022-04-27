from antlr4 import *
from antlr4.Token import  CommonToken

from PythonLexer import PythonLexer
from PythonParser import  PythonParser
#from MyListener import MyListener
from  MyListener import PythonListener

if __name__ == '__main__':
    print('ANTLR com Ações semantics')
    fileEnterada = open("file.py", "r")
    data = fileEnterada.read()
    data = InputStream(data)
    #data = FileStream('prog.py')

    #Lexer
    lexer = PythonLexer(data)
    stream = CommonTokenStream(lexer)

    #Parser
    parser = PythonParser(stream)
    tree = parser.prog()
    #print(tree)

    l = PythonListener()
    walker = ParseTreeWalker()
    walker.walk(l, tree)


"""
from  antlr4 import *
from Expr2022Parser import  Expr2022Parser
from Expr2022Lexer import Expr2022Lexer
from Expr2022MyListener import Expr2022MyListener

if __name__== '__main__':
    data = FileStream('/home/jardielson/UFPI-2021.2/Compiladores/antrl/Questão/AtvAula/input.txt')
    lexer = Expr2022Lexer(data)
    stream = CommonTokenStream(lexer)

    parser = Expr2022Parser(stream)
    tree = parser.lines()

    l = Expr2022MyListener()
    walker = ParseTreeWalker()
    walker.walk(l, tree)    
"""
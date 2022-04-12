from antlr4 import *
from antlr4.Token import  CommonToken

from PythonLexer import PythonLexer
from PythonParser import  PythonParser

if __name__ == '__main__':
    print('ANTLR com Ações semantics')
    fileEnterada = open("file.txt", "r")
    data = fileEnterada.read()
    data = InputStream(data)
    #data = FileStream('prog.py')

    #Lexer
    lexer = PythonLexer(data)
    stream = CommonTokenStream(lexer)

    #Parser
    parser = PythonParser(stream)
    tree = parser.prog()
    print(tree)
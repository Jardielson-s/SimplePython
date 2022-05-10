from antlr4 import *
from antlr4.Token import  CommonToken

from PythonLexer import PythonLexer
from PythonParser import  PythonParser
#from MyListener import MyListener
from  MyListener import PythonListener
from antlr4.error.Errors import ParseCancellationException
from antlr4.error.ErrorListener import ErrorListener # CLASSE QUE FAZ O TRATAMENTO DE ERROS EM RELAÇÃO A NOSSA GRAMÁTICA

class bcolors:
    FAIL = '\033[91m' #RED



class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        ex = ParseCancellationException(f'line {line}: {column} {msg}')
        ex.line = line
        ex.column = column
        ex.msg = msg
        print(f"{bcolors.FAIL} {ex}")
        exit(0)


if __name__ == '__main__':
    #print('ANTLR com Ações semantics')
    fileEnterada = open("file.py", "r")
    data = fileEnterada.read()
    data = InputStream(data)
    lexer = PythonLexer(data)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())

    # t = Token()
    # tokens = CommonTokenStream(lexer)
    # t = lexer.nextToken()
    #
    # while t.type != t.EOF:
    #     #print("<" + t.text + ", " + lexer.enterprog [t.type] + ">")
    #     t = lexer.nextToken()



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
int numero;
def int fatorial (int fat):
if fat > 1:
print fat;
return fat * fatorial(fat - 1);
} else:
return 1;
}
}
def void resultado (int valor):
print "Resultado: ", valor;
}
main():
 print "Fatorial de N. Digite o número?";
 numero = input();
 resultado (fatorial (numero));

}
"""
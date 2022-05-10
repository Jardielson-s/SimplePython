# Generated from Python.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

class bcolors:
    FAIL = '\033[91m' #RED

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#prog.
    def enterProg(self, ctx:PythonParser.ProgContext):
        pass

    # Exit a parse tree produced by PythonParser#prog.
    def exitProg(self, ctx:PythonParser.ProgContext):
        pass



    # Enter a parse tree produced by PythonParser#varDecl.
    def enterVarDecl(self, ctx:PythonParser.VarDeclContext):
        pass

    # Exit a parse tree produced by PythonParser#varDecl.
    def exitVarDecl(self, ctx:PythonParser.VarDeclContext):
        if (len(ctx.getText().split('=')) == 1):
            pass
        elif PythonListener.exitType(self,ctx.type()) != None:
            if PythonListener.exitType(self,ctx.type()) == 'int': # UM INTEIRO SÓ PODE RECEBER VALORES INTEIROS CASO NÃO CONTRÁRIO SERÁ IMPRESSO UM ERRO.
                value = ctx.getText().split('=')
                try:
                   isinstance(int(value[1].split(';')[0]), int)
                   ctx.val = value[1].split(';')[0]
                except:
                    return print(f"{bcolors.FAIL}ERROR: {value[0].split('int')[1]} not received {value[1].split(';')[0]}")
            elif PythonListener.exitType(self,ctx.type()) == 'float':
                value = ctx.getText().split('=')
                try:
                    ctx.val =  value[1].split(';')[0].replace('"',"")
                except:
                    return print(f"{bcolors.FAIL} {value[0].split('float')[1]} not received {value[1].split(';')[0]}")
            # elif PythonListener.exitType(self,ctx.type()) == 'double':
            #     value = ctx.getText().split('=')
            #     try:
            #         notFloat = isinstance(value[1].split(';')[0].replace('"', ""), str)
            #         if notFloat:
            #             return print(
            #                 f"{bcolors.FAIL} Error: {value[0].split('float')[1]} not received {value[1].split(';')[0]}")
            #         # isinstance(float(value[1].split(';')[0].replace('"',"")), float)
            #         ctx.val = value
            #     except:
            #         return print(f"{bcolors.FAIL} {value[0].split('double')[1]} not received {value[1].split(';')[0]}")
            elif PythonListener.exitType(self,ctx.type()) == 'boolean': # VERIFICA O QUE UMA VARIÁVEL BOOLEANA RECEBE SE RECEBER STRING, NÚMEROS MAIORES OU IGUAIS A ZERO E TRUE A VARIÁVEL SERÁ TRUE CASO CONTRÁRIO FALSE
                value = ctx.getText().split('=')
                try:
                    valueIsInt = value[1].split(';')[0].replace('"', "")
                    if valueIsInt == 'True' or valueIsInt >= '1':
                       ctx.val = True
                    elif valueIsInt == 'False' or valueIsInt <= '0':
                       ctx.val = False
                    else:
                        return print(f"{bcolors.FAIL}Error:{value[0].split('boolean')[1]} not received {value[1].split(';')[0]}")
                finally:
                    pass
            elif PythonListener.exitType(self,ctx.type()) == 'string':# CASO RECEBA QUALQUER  COISA COMO NÚMERO OU VALORES BOOLEANOS, TODOS SERÃO CONVERTIDOS PARA STRING
                value = ctx.getText().split('=')
                try:
                    value = str(value[1].split(';')[0].replace('"', ""))
                    ctx.val = value
                except:
                    return print(f"{bcolors.FAIL} {value[0].split('string')[1]} not received {value[1].split(';')[0]}")
        else:
            return print(f"{bcolors.FAIL}  mismatched input expecting {'int', 'float', 'boolean', 'string', 'void', 'def'}")


    # Enter a parse tree produced by PythonParser#type.
    def enterType(self, ctx:PythonParser.TypeContext):
        pass

    # Exit a parse tree produced by PythonParser#type.
    def exitType(self, ctx:PythonParser.TypeContext): # RETORNAR O TIPO
        return  ctx.getText()


    # Enter a parse tree produced by PythonParser#listaIds.
    def enterListaIds(self, ctx:PythonParser.ListaIdsContext):
        pass

    # Exit a parse tree produced by PythonParser#listaIds.
    def exitListaIds(self, ctx:PythonParser.ListaIdsContext):
        if PythonListener.exitType(self,ctx) != None:
            return ctx.getText()
        else:
            return print(f"{bcolors.FAIL}   expecting {'int', 'float', 'boolean', 'string', 'void'}")



    # Enter a parse tree produced by PythonParser#listaAtribs.
    def enterListaAtribs(self, ctx:PythonParser.ListaAtribsContext):
        pass

    # Exit a parse tree produced by PythonParser#listaAtribs.
    def exitListaAtribs(self, ctx:PythonParser.ListaAtribsContext):
        pass#print(ctx.getText())


    # Enter a parse tree produced by PythonParser#funcDecl.
    def enterFuncDecl(self, ctx:PythonParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by PythonParser#funcDecl.
    def exitFuncDecl(self, ctx:PythonParser.FuncDeclContext):
        pass
        #PythonListener.exitType(self, ctx.type())
        #print(PythonListener.exitType(self,ctx.type()))


    # Enter a parse tree produced by PythonParser#mainBlock.
    def enterMainBlock(self, ctx:PythonParser.MainBlockContext):
        pass

    # Exit a parse tree produced by PythonParser#mainBlock.
    def exitMainBlock(self, ctx:PythonParser.MainBlockContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#stats.
    def enterStats(self, ctx:PythonParser.StatsContext):
        pass

    # Exit a parse tree produced by PythonParser#stats.
    def exitStats(self, ctx:PythonParser.StatsContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#stats_com_break.
    def enterStats_com_break(self, ctx:PythonParser.Stats_com_breakContext):
        pass

    # Exit a parse tree produced by PythonParser#stats_com_break.
    def exitStats_com_break(self, ctx:PythonParser.Stats_com_breakContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#cmdAtrib.
    def enterCmdAtrib(self, ctx:PythonParser.CmdAtribContext):
        pass

    # Exit a parse tree produced by PythonParser#cmdAtrib.
    def exitCmdAtrib(self, ctx:PythonParser.CmdAtribContext):
        pass#print(ctx.getText())


    # Enter a parse tree produced by PythonParser#cmdFor.
    def enterCmdFor(self, ctx:PythonParser.CmdForContext):
        pass

    # Exit a parse tree produced by PythonParser#cmdFor.
    def exitCmdFor(self, ctx:PythonParser.CmdForContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#cmdWhile.
    def enterCmdWhile(self, ctx:PythonParser.CmdWhileContext):
        pass

    # Exit a parse tree produced by PythonParser#cmdWhile.
    def exitCmdWhile(self, ctx:PythonParser.CmdWhileContext):
        pass


    # Enter a parse tree produced by PythonParser#cmdIF.
    def enterCmdIF(self, ctx:PythonParser.CmdIFContext):
        pass

    # Exit a parse tree produced by PythonParser#cmdIF.
    def exitCmdIF(self, ctx:PythonParser.CmdIFContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#Termo.
    def enterTermo(self, ctx:PythonParser.TermoContext):
        pass

    # Exit a parse tree produced by PythonParser#Termo.
    def exitTermo(self, ctx:PythonParser.TermoContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#SomaSub.
    def enterSomaSub(self, ctx:PythonParser.SomaSubContext):
        pass

    # Exit a parse tree produced by PythonParser#SomaSub.
    def exitSomaSub(self, ctx:PythonParser.SomaSubContext):
       # print(ctx.t1.val)
        pass
        #print(ctx.)
        #ctx.val = ctx.e1.val + ctx.term().val
        # if ctx.op.text == '+':
        #     ctx.val = ctx.e1.val + ctx.term().val
        # else:
        #     ctx.val = ctx.e1.val - ctx.term().val


    # Enter a parse tree produced by PythonParser#Fator.
    def enterFator(self, ctx:PythonParser.FatorContext):
        pass

    # Exit a parse tree produced by PythonParser#Fator.
    def exitFator(self, ctx:PythonParser.FatorContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#DIVMult.
    def enterDIVMult(self, ctx:PythonParser.DIVMultContext):
        pass

    # Exit a parse tree produced by PythonParser#DIVMult.
    def exitDIVMult(self, ctx:PythonParser.DIVMultContext):
        return  self.visitTerminal(ctx)
        # if ctx.val == '*':
        #      ctx.val = ctx.t1.val * ctx.term().val
        # elif ctx.val == '/':
        #     ctx.val = ctx.t1.val / ctx.term().val
        # elif ctx.val == '>':
        #     print(ctx.val)



    # Enter a parse tree produced by PythonParser#ExpParenteses.
    def enterExpParenteses(self, ctx:PythonParser.ExpParentesesContext):
        pass

    # Exit a parse tree produced by PythonParser#ExpParenteses.
    def exitExpParenteses(self, ctx:PythonParser.ExpParentesesContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#Numero.
    def enterNumero(self, ctx:PythonParser.NumeroContext):
        pass

    # Exit a parse tree produced by PythonParser#Numero.
    def exitNumero(self, ctx:PythonParser.NumeroContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#range.
    def enterRange(self, ctx:PythonParser.RangeContext):
        pass

    # Exit a parse tree produced by PythonParser#range.
    def exitRange(self, ctx:PythonParser.RangeContext):
        return  self.visitTerminal(ctx)

    # Enter a parse tree produced by PythonParser#listaParams.
    def enterListaParams(self, ctx:PythonParser.ListaParamsContext):
        pass

    # Exit a parse tree produced by PythonParser#listaParams.
    def exitListaParams(self, ctx:PythonParser.ListaParamsContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#functions_native.
    def enterFunctions_native(self, ctx:PythonParser.Functions_nativeContext):
        pass

    # Exit a parse tree produced by PythonParser#functions_native.
    def exitFunctions_native(self, ctx:PythonParser.Functions_nativeContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#print.
    def enterPrint(self, ctx:PythonParser.PrintContext):
        pass

    # Exit a parse tree produced by PythonParser#print.
    def exitPrint(self, ctx:PythonParser.PrintContext):
        return  self.visitTerminal(ctx)


    # Enter a parse tree produced by PythonParser#operacao.
    def enterOperacao(self, ctx:PythonParser.OperacaoContext):
        pass

    # Exit a parse tree produced by PythonParser#operacao.
    def exitOperacao(self, ctx:PythonParser.OperacaoContext):
        return  self.visitTerminal(ctx)



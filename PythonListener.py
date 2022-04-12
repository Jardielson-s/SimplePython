# Generated from Python.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

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
        pass


    # Enter a parse tree produced by PythonParser#type.
    def enterType(self, ctx:PythonParser.TypeContext):
        pass

    # Exit a parse tree produced by PythonParser#type.
    def exitType(self, ctx:PythonParser.TypeContext):
        pass


    # Enter a parse tree produced by PythonParser#listaIds.
    def enterListaIds(self, ctx:PythonParser.ListaIdsContext):
        pass

    # Exit a parse tree produced by PythonParser#listaIds.
    def exitListaIds(self, ctx:PythonParser.ListaIdsContext):
        pass


    # Enter a parse tree produced by PythonParser#listaAtribs.
    def enterListaAtribs(self, ctx:PythonParser.ListaAtribsContext):
        pass

    # Exit a parse tree produced by PythonParser#listaAtribs.
    def exitListaAtribs(self, ctx:PythonParser.ListaAtribsContext):
        pass


    # Enter a parse tree produced by PythonParser#funcDecl.
    def enterFuncDecl(self, ctx:PythonParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by PythonParser#funcDecl.
    def exitFuncDecl(self, ctx:PythonParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by PythonParser#mainBlock.
    def enterMainBlock(self, ctx:PythonParser.MainBlockContext):
        pass

    # Exit a parse tree produced by PythonParser#mainBlock.
    def exitMainBlock(self, ctx:PythonParser.MainBlockContext):
        pass


    # Enter a parse tree produced by PythonParser#stats.
    def enterStats(self, ctx:PythonParser.StatsContext):
        pass

    # Exit a parse tree produced by PythonParser#stats.
    def exitStats(self, ctx:PythonParser.StatsContext):
        pass


    # Enter a parse tree produced by PythonParser#stats_com_break.
    def enterStats_com_break(self, ctx:PythonParser.Stats_com_breakContext):
        pass

    # Exit a parse tree produced by PythonParser#stats_com_break.
    def exitStats_com_break(self, ctx:PythonParser.Stats_com_breakContext):
        pass


    # Enter a parse tree produced by PythonParser#cmdAtrib.
    def enterCmdAtrib(self, ctx:PythonParser.CmdAtribContext):
        pass

    # Exit a parse tree produced by PythonParser#cmdAtrib.
    def exitCmdAtrib(self, ctx:PythonParser.CmdAtribContext):
        pass


    # Enter a parse tree produced by PythonParser#cmdFor.
    def enterCmdFor(self, ctx:PythonParser.CmdForContext):
        pass

    # Exit a parse tree produced by PythonParser#cmdFor.
    def exitCmdFor(self, ctx:PythonParser.CmdForContext):
        pass


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
        pass


    # Enter a parse tree produced by PythonParser#Termo.
    def enterTermo(self, ctx:PythonParser.TermoContext):
        pass

    # Exit a parse tree produced by PythonParser#Termo.
    def exitTermo(self, ctx:PythonParser.TermoContext):
        pass


    # Enter a parse tree produced by PythonParser#SomaSub.
    def enterSomaSub(self, ctx:PythonParser.SomaSubContext):
        pass

    # Exit a parse tree produced by PythonParser#SomaSub.
    def exitSomaSub(self, ctx:PythonParser.SomaSubContext):
        pass


    # Enter a parse tree produced by PythonParser#Fator.
    def enterFator(self, ctx:PythonParser.FatorContext):
        pass

    # Exit a parse tree produced by PythonParser#Fator.
    def exitFator(self, ctx:PythonParser.FatorContext):
        pass


    # Enter a parse tree produced by PythonParser#DIVMult.
    def enterDIVMult(self, ctx:PythonParser.DIVMultContext):
        pass

    # Exit a parse tree produced by PythonParser#DIVMult.
    def exitDIVMult(self, ctx:PythonParser.DIVMultContext):
        pass


    # Enter a parse tree produced by PythonParser#ExpParenteses.
    def enterExpParenteses(self, ctx:PythonParser.ExpParentesesContext):
        pass

    # Exit a parse tree produced by PythonParser#ExpParenteses.
    def exitExpParenteses(self, ctx:PythonParser.ExpParentesesContext):
        pass


    # Enter a parse tree produced by PythonParser#Numero.
    def enterNumero(self, ctx:PythonParser.NumeroContext):
        pass

    # Exit a parse tree produced by PythonParser#Numero.
    def exitNumero(self, ctx:PythonParser.NumeroContext):
        pass


    # Enter a parse tree produced by PythonParser#range.
    def enterRange(self, ctx:PythonParser.RangeContext):
        pass

    # Exit a parse tree produced by PythonParser#range.
    def exitRange(self, ctx:PythonParser.RangeContext):
        pass


    # Enter a parse tree produced by PythonParser#listaParams.
    def enterListaParams(self, ctx:PythonParser.ListaParamsContext):
        pass

    # Exit a parse tree produced by PythonParser#listaParams.
    def exitListaParams(self, ctx:PythonParser.ListaParamsContext):
        pass


    # Enter a parse tree produced by PythonParser#functions_native.
    def enterFunctions_native(self, ctx:PythonParser.Functions_nativeContext):
        pass

    # Exit a parse tree produced by PythonParser#functions_native.
    def exitFunctions_native(self, ctx:PythonParser.Functions_nativeContext):
        pass


    # Enter a parse tree produced by PythonParser#print.
    def enterPrint(self, ctx:PythonParser.PrintContext):
        pass

    # Exit a parse tree produced by PythonParser#print.
    def exitPrint(self, ctx:PythonParser.PrintContext):
        pass


    # Enter a parse tree produced by PythonParser#operacao.
    def enterOperacao(self, ctx:PythonParser.OperacaoContext):
        pass

    # Exit a parse tree produced by PythonParser#operacao.
    def exitOperacao(self, ctx:PythonParser.OperacaoContext):
        pass



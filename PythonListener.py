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


    # Enter a parse tree produced by PythonParser#listaDecVars.
    def enterListaDecVars(self, ctx:PythonParser.ListaDecVarsContext):
        pass

    # Exit a parse tree produced by PythonParser#listaDecVars.
    def exitListaDecVars(self, ctx:PythonParser.ListaDecVarsContext):
        pass


    # Enter a parse tree produced by PythonParser#varDecl.
    def enterVarDecl(self, ctx:PythonParser.VarDeclContext):
        pass

    # Exit a parse tree produced by PythonParser#varDecl.
    def exitVarDecl(self, ctx:PythonParser.VarDeclContext):
        pass


    # Enter a parse tree produced by PythonParser#decVars.
    def enterDecVars(self, ctx:PythonParser.DecVarsContext):
        pass

    # Exit a parse tree produced by PythonParser#decVars.
    def exitDecVars(self, ctx:PythonParser.DecVarsContext):
        pass


    # Enter a parse tree produced by PythonParser#decParam.
    def enterDecParam(self, ctx:PythonParser.DecParamContext):
        pass

    # Exit a parse tree produced by PythonParser#decParam.
    def exitDecParam(self, ctx:PythonParser.DecParamContext):
        pass


    # Enter a parse tree produced by PythonParser#tipo.
    def enterTipo(self, ctx:PythonParser.TipoContext):
        pass

    # Exit a parse tree produced by PythonParser#tipo.
    def exitTipo(self, ctx:PythonParser.TipoContext):
        pass


    # Enter a parse tree produced by PythonParser#listaIds.
    def enterListaIds(self, ctx:PythonParser.ListaIdsContext):
        pass

    # Exit a parse tree produced by PythonParser#listaIds.
    def exitListaIds(self, ctx:PythonParser.ListaIdsContext):
        pass


    # Enter a parse tree produced by PythonParser#atrib.
    def enterAtrib(self, ctx:PythonParser.AtribContext):
        pass

    # Exit a parse tree produced by PythonParser#atrib.
    def exitAtrib(self, ctx:PythonParser.AtribContext):
        pass


    # Enter a parse tree produced by PythonParser#listaAtribs.
    def enterListaAtribs(self, ctx:PythonParser.ListaAtribsContext):
        pass

    # Exit a parse tree produced by PythonParser#listaAtribs.
    def exitListaAtribs(self, ctx:PythonParser.ListaAtribsContext):
        pass


    # Enter a parse tree produced by PythonParser#typeFunc.
    def enterTypeFunc(self, ctx:PythonParser.TypeFuncContext):
        pass

    # Exit a parse tree produced by PythonParser#typeFunc.
    def exitTypeFunc(self, ctx:PythonParser.TypeFuncContext):
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


    # Enter a parse tree produced by PythonParser#returnFunc.
    def enterReturnFunc(self, ctx:PythonParser.ReturnFuncContext):
        pass

    # Exit a parse tree produced by PythonParser#returnFunc.
    def exitReturnFunc(self, ctx:PythonParser.ReturnFuncContext):
        pass


    # Enter a parse tree produced by PythonParser#stmts.
    def enterStmts(self, ctx:PythonParser.StmtsContext):
        pass

    # Exit a parse tree produced by PythonParser#stmts.
    def exitStmts(self, ctx:PythonParser.StmtsContext):
        pass


    # Enter a parse tree produced by PythonParser#stats_com_break.
    def enterStats_com_break(self, ctx:PythonParser.Stats_com_breakContext):
        pass

    # Exit a parse tree produced by PythonParser#stats_com_break.
    def exitStats_com_break(self, ctx:PythonParser.Stats_com_breakContext):
        pass


    # Enter a parse tree produced by PythonParser#stmts_break.
    def enterStmts_break(self, ctx:PythonParser.Stmts_breakContext):
        pass

    # Exit a parse tree produced by PythonParser#stmts_break.
    def exitStmts_break(self, ctx:PythonParser.Stmts_breakContext):
        pass


    # Enter a parse tree produced by PythonParser#callFunction.
    def enterCallFunction(self, ctx:PythonParser.CallFunctionContext):
        pass

    # Exit a parse tree produced by PythonParser#callFunction.
    def exitCallFunction(self, ctx:PythonParser.CallFunctionContext):
        pass


    # Enter a parse tree produced by PythonParser#cmdAtrib.
    def enterCmdAtrib(self, ctx:PythonParser.CmdAtribContext):
        pass

    # Exit a parse tree produced by PythonParser#cmdAtrib.
    def exitCmdAtrib(self, ctx:PythonParser.CmdAtribContext):
        pass


    # Enter a parse tree produced by PythonParser#ForCond.
    def enterForCond(self, ctx:PythonParser.ForCondContext):
        pass

    # Exit a parse tree produced by PythonParser#ForCond.
    def exitForCond(self, ctx:PythonParser.ForCondContext):
        pass


    # Enter a parse tree produced by PythonParser#WhileCond.
    def enterWhileCond(self, ctx:PythonParser.WhileCondContext):
        pass

    # Exit a parse tree produced by PythonParser#WhileCond.
    def exitWhileCond(self, ctx:PythonParser.WhileCondContext):
        pass


    # Enter a parse tree produced by PythonParser#printFunc.
    def enterPrintFunc(self, ctx:PythonParser.PrintFuncContext):
        pass

    # Exit a parse tree produced by PythonParser#printFunc.
    def exitPrintFunc(self, ctx:PythonParser.PrintFuncContext):
        pass


    # Enter a parse tree produced by PythonParser#inputFunc.
    def enterInputFunc(self, ctx:PythonParser.InputFuncContext):
        pass

    # Exit a parse tree produced by PythonParser#inputFunc.
    def exitInputFunc(self, ctx:PythonParser.InputFuncContext):
        pass


    # Enter a parse tree produced by PythonParser#IfCond.
    def enterIfCond(self, ctx:PythonParser.IfCondContext):
        pass

    # Exit a parse tree produced by PythonParser#IfCond.
    def exitIfCond(self, ctx:PythonParser.IfCondContext):
        pass


    # Enter a parse tree produced by PythonParser#IfBreakCond.
    def enterIfBreakCond(self, ctx:PythonParser.IfBreakCondContext):
        pass

    # Exit a parse tree produced by PythonParser#IfBreakCond.
    def exitIfBreakCond(self, ctx:PythonParser.IfBreakCondContext):
        pass


    # Enter a parse tree produced by PythonParser#BoolTFExpr.
    def enterBoolTFExpr(self, ctx:PythonParser.BoolTFExprContext):
        pass

    # Exit a parse tree produced by PythonParser#BoolTFExpr.
    def exitBoolTFExpr(self, ctx:PythonParser.BoolTFExprContext):
        pass


    # Enter a parse tree produced by PythonParser#StringExpr.
    def enterStringExpr(self, ctx:PythonParser.StringExprContext):
        pass

    # Exit a parse tree produced by PythonParser#StringExpr.
    def exitStringExpr(self, ctx:PythonParser.StringExprContext):
        pass


    # Enter a parse tree produced by PythonParser#BoolExpr.
    def enterBoolExpr(self, ctx:PythonParser.BoolExprContext):
        pass

    # Exit a parse tree produced by PythonParser#BoolExpr.
    def exitBoolExpr(self, ctx:PythonParser.BoolExprContext):
        pass


    # Enter a parse tree produced by PythonParser#FloatExpr.
    def enterFloatExpr(self, ctx:PythonParser.FloatExprContext):
        pass

    # Exit a parse tree produced by PythonParser#FloatExpr.
    def exitFloatExpr(self, ctx:PythonParser.FloatExprContext):
        pass


    # Enter a parse tree produced by PythonParser#IdExpr.
    def enterIdExpr(self, ctx:PythonParser.IdExprContext):
        pass

    # Exit a parse tree produced by PythonParser#IdExpr.
    def exitIdExpr(self, ctx:PythonParser.IdExprContext):
        pass


    # Enter a parse tree produced by PythonParser#CompExpr.
    def enterCompExpr(self, ctx:PythonParser.CompExprContext):
        pass

    # Exit a parse tree produced by PythonParser#CompExpr.
    def exitCompExpr(self, ctx:PythonParser.CompExprContext):
        pass


    # Enter a parse tree produced by PythonParser#CompAllExpr.
    def enterCompAllExpr(self, ctx:PythonParser.CompAllExprContext):
        pass

    # Exit a parse tree produced by PythonParser#CompAllExpr.
    def exitCompAllExpr(self, ctx:PythonParser.CompAllExprContext):
        pass


    # Enter a parse tree produced by PythonParser#NegateExpr.
    def enterNegateExpr(self, ctx:PythonParser.NegateExprContext):
        pass

    # Exit a parse tree produced by PythonParser#NegateExpr.
    def exitNegateExpr(self, ctx:PythonParser.NegateExprContext):
        pass


    # Enter a parse tree produced by PythonParser#AssignExpr.
    def enterAssignExpr(self, ctx:PythonParser.AssignExprContext):
        pass

    # Exit a parse tree produced by PythonParser#AssignExpr.
    def exitAssignExpr(self, ctx:PythonParser.AssignExprContext):
        pass


    # Enter a parse tree produced by PythonParser#IntegerExpr.
    def enterIntegerExpr(self, ctx:PythonParser.IntegerExprContext):
        pass

    # Exit a parse tree produced by PythonParser#IntegerExpr.
    def exitIntegerExpr(self, ctx:PythonParser.IntegerExprContext):
        pass


    # Enter a parse tree produced by PythonParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:PythonParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by PythonParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:PythonParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by PythonParser#PlusExpr.
    def enterPlusExpr(self, ctx:PythonParser.PlusExprContext):
        pass

    # Exit a parse tree produced by PythonParser#PlusExpr.
    def exitPlusExpr(self, ctx:PythonParser.PlusExprContext):
        pass


    # Enter a parse tree produced by PythonParser#ParensExpr.
    def enterParensExpr(self, ctx:PythonParser.ParensExprContext):
        pass

    # Exit a parse tree produced by PythonParser#ParensExpr.
    def exitParensExpr(self, ctx:PythonParser.ParensExprContext):
        pass


    # Enter a parse tree produced by PythonParser#CallExpr.
    def enterCallExpr(self, ctx:PythonParser.CallExprContext):
        pass

    # Exit a parse tree produced by PythonParser#CallExpr.
    def exitCallExpr(self, ctx:PythonParser.CallExprContext):
        pass


    # Enter a parse tree produced by PythonParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:PythonParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by PythonParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:PythonParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by PythonParser#MinusExpr.
    def enterMinusExpr(self, ctx:PythonParser.MinusExprContext):
        pass

    # Exit a parse tree produced by PythonParser#MinusExpr.
    def exitMinusExpr(self, ctx:PythonParser.MinusExprContext):
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


    # Enter a parse tree produced by PythonParser#operacao.
    def enterOperacao(self, ctx:PythonParser.OperacaoContext):
        pass

    # Exit a parse tree produced by PythonParser#operacao.
    def exitOperacao(self, ctx:PythonParser.OperacaoContext):
        pass



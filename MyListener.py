import random

from antlr4 import *

if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
   from PythonParser import PythonParser



class PythonListener(ParseTreeListener):
    ids = []
    valueIf = 0
    ifs = [[]]
    condsLabels = [[]]
    funcsName = ["", ]
    func = -1
    labels = """"
    """
    prog = [["""
.method public static read()I

   .limit stack 5   
   .limit locals 100

   ; the input function starts at this point
    ldc 0
    istore 50     
    ldc 0
    istore 49      
 Label1:
    getstatic java/lang/System/in Ljava/io/InputStream;
    invokevirtual java/io/InputStream/read()I
    istore 51
    iload 51
  ;  ldc 10 
    ldc 13 
    isub
    ifeq Label2
    iload 51
    ldc 32 
    isub
    ifeq Label2
    iload 51
    ldc 43 
    isub
    ifeq Label1
    iload 51
    ldc 45 
    isub
    ifeq Label3
    iload 51
    ldc 48
    isub
    ldc 10
    iload 50
    imul
    iadd
    istore 50
    goto Label1

  Label3:
    ldc 1
    istore 49
    goto Label1

  Label2:     
    ldc 1
    iload 49
    isub
    ifeq Label4
    iload 50       
    ireturn
  Label4:
    ldc 0
    iload 50
    isub
    ireturn
.end method

        """]]

    def tipo(self, value):
        if value == 0:
            return "int"
        if value == 1:
            return "float"
        if value == 2:
            return "boolean"
        if value == 3:
            return "string"
        return "void"

    def tipoToNumber(self, value):
        if value == "int":
            return 0
        if value == "float":
            return 1
        if value == "boolean":
            return 2
        if value == "string":
            return 3
        return "void"

    # Enter a parse tree produced by trabParser#prog.
    def enterProg(self, ctx: PythonParser.ProgContext):
        self.func = self.func + 1;
        self.prog[self.func].append("""
    .method public static main([Ljava/lang/String;)V
    .limit stack 50
    .limit locals 50""")
        pass

    # Exit a parse tree produced by trabParser#prog.
    def exitProg(self, ctx: PythonParser.ProgContext):
        self.prog[0].append("return")
        for d in range(0, len(self.prog)):
            for x in self.condsLabels[d]:
                for y in x:
                    self.prog[d].append(y)
        self.prog[1].append("""
    .end method""")
        y = ""
        for x in self.prog:
            for d in x:
                y = y + d
        y = """
    .class public python
    .super java/lang/Object
    """ + y
        print(y)
        x = open("python.j", "w")
        x.write(y)
        pass


    # Exit a parse tree produced by trabParser#listaDecVars.
    def exitListaDecVars(self, ctx: PythonParser.ListaDecVarsContext):
        ctx.value = ctx.children[0].value
        pass

    # Enter a parse tree produced by trabParser#decVars.
    def enterDecVars(self, ctx: PythonParser.DecVarsContext):
        pass

    # Exit a parse tree produced by trabParser#decVars.
    def exitDecVars(self, ctx: PythonParser.DecVarsContext):
        for i in ctx.listaDecVars().value:
            if not (i[2] == None):
                tipo = ctx.tipo().value
                tipoId = self.tipo(i[2])
                if tipo != tipoId:
                    raise ValueError(f"Type declaration error {tipo} != {tipoId} in the declaration of  {i[0]}")
                    return;
            else:
                tipo = ctx.tipo().value
                tipo = self.tipoToNumber(tipo)
                for x in self.ids:
                    if x[0] == i[0]:
                        index = self.ids.index(i)
                        self.ids[index] = [i[0], None, tipo]

        pass

    # Exit a parse tree produced by trabParser#tipo.
    def exitTipo(self, ctx: PythonParser.TipoContext):
        ctx.value = ctx.getText()
        pass

    # Enter a parse tree produced by trabParser#listaIds.
    def enterListaIds(self, ctx: PythonParser.ListaIdsContext):
        for i in ctx.ID():
            i = str(i)
            for x in self.ids:
                if i == x[0]:
                    raise ValueError("Erro: Variables already declared")
                    return
            self.ids.append([i, None, None])
        pass

    # Exit a parse tree produced by trabParser#listaIds.
    def exitListaIds(self, ctx: PythonParser.ListaIdsContext):
        x = []
        for i in ctx.ID():
            i = str(i)
            payload = [i, None, None]
            x.append(payload)
        ctx.value = x

        pass

    # Enter a parse tree produced by trabParser#atrib.
    def enterAtrib(self, ctx: PythonParser.AtribContext):
        i = str(ctx.ID())
        for x in self.ids:
            if i == x[0]:
                raise ValueError(f"Variável {x[0]} já declarada")
                return
        self.ids.append([i, None, None])
        pass

    # Exit a parse tree produced by trabParser#atrib.
    def exitAtrib(self, ctx: PythonParser.AtribContext):
        x = []
        i = ctx.ID()
        i = str(i)
        payload = [i, None, None]
        x.append(payload)
        self.ids.remove(payload)
        payload[1] = ctx.expr().value[1]
        payload[2] = ctx.expr().value[2]
        self.ids.append(payload)
        ctx.value = x
        if (payload[2] == 0):
            self.prog[self.func].append(f"""
        istore {self.ids.index(payload)}
        """)
        if (payload[2] == 1):
            self.prog[self.func].append(f"""
        fstore {self.ids.index(payload)}
        """)
        if (payload[2] == 2):
            self.prog[self.func].append(f"""
        astore {self.ids.index(payload)}
        """)
        if (payload[2] == 3):
            self.prog[self.func].append(f"""
        astore {self.ids.index(payload)}
            """)

        pass

    # Exit a parse tree produced by trabParser#listaAtribs.
    def exitListaAtribs(self, ctx: PythonParser.ListaAtribsContext):
        x = []
        for i in ctx.atrib():
            for y in i.value:
                x.append(y)
        ctx.value = x
        pass


    # Enter a parse tree produced by trabParser#DecFunc.
    def enterDecFunc(self, ctx: PythonParser.DecFuncContext):
        self.prog.append([])
        self.func = self.func + 1;
        self.ids.append([])
        self.condsLabels.append([])
        self.ifs.append([])
        pass


    # Enter a parse tree produced by trabParser#blocoMain.
    def enterBlocoMain(self, ctx: PythonParser.BlocoMainContext):
        self.prog.append([])
        self.condsLabels.append([])
        self.ifs.append([])

        pass


    # Exit a parse tree produced by trabParser#cmdAtrib.
    def exitCmdAtrib(self, ctx: PythonParser.CmdAtribContext):
        x = str(ctx.ID())
        y = ctx.expr().value
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]

        for i in self.ids:
            if (i[0] == x):
                if y in vars:
                    if i[2] != y[0]:
                        raise ValueError(f"Tipo de {i[0]} ({self.tipo(i[2])}) incompatível com {self.tipo(y[0])}")
                else:
                    if i[2] != y[2]:
                        raise ValueError(f"Tipo de {i[0]} ({self.tipo(i[2])}) incompatível com {self.tipo(y[2])}")
                if i[2] == 0:
                    self.prog[self.func].append(f"""
        istore {self.ids.index(i)}
""")
                if i[2] == 1:
                    self.prog[self.func].append(f"""
        fstore {self.ids.index(i)}
        """)
                if i[2] == 3:
                    self.prog[self.func].append(f"""
        astore {self.ids.index(i)}
        """)
        pass

    # Enter a parse tree produced by trabParser#IfCond.
    def enterIfCond(self, ctx: PythonParser.IfCondContext):
        pass

    # Exit a parse tree produced by trabParser#IfCond.
    def exitIfCond(self, ctx: PythonParser.IfCondContext):
        y = self.ifs[self.func].pop()
        x = [f"""
        goto Retorno{y[1]}
        """]
        while len(self.prog[self.func]) - y[0] != 0:
            x.append(self.prog[self.func].pop())
        x.append(f"""
    Label{y[1]}:""")
        x.reverse()
        self.condsLabels[self.func].append(x)
        pass


    # Exit a parse tree produced by trabParser#IfBreakCond.
    def exitIfBreakCond(self, ctx: PythonParser.IfBreakCondContext):
        y = self.ifs[self.func].pop()
        x = [f"""
        goto Retorno{y[1]}
            """]
        while len(self.prog[self.func]) - y[0] != 0:
            x.append(self.prog[self.func].pop())
        x.append(f"""
    Label{y[1]}:""")
        x.reverse()
        self.condsLabels[self.func].append(x)
        pass


    # Exit a parse tree produced by trabParser#WhileCond.
    def exitWhileCond(self, ctx: PythonParser.WhileCondContext):
        y = self.ifs[self.func].pop()
        x = [f"""{self.prog[self.func][y[0] - 4]}{self.prog[self.func][y[0] - 3]}{self.prog[self.func][y[0] - 2]}
        goto Retorno{y[1]}"""]
        while len(self.prog[self.func]) - y[0] != 0:
            x.append(self.prog[self.func].pop())
        x.append(f"""
    Label{y[1]}:""")
        x.reverse()
        self.condsLabels[self.func].append(x)
        pass

    # Enter a parse tree produced by trabParser#printFunc.
    def enterPrintFunc(self, ctx: PythonParser.PrintFuncContext):
        self.prog[self.func].append("""
        getstatic java/lang/System/out Ljava/io/PrintStream;""")
        pass

    # Exit a parse tree produced by trabParser#printFunc.
    def exitPrintFunc(self, ctx: PythonParser.PrintFuncContext):
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]

        for x in ctx.expr():
            y = x.value
            index = 2
            if y in vars:
                index = 0
                # raise ValueError("Tipo incompatível com print")
            if y[0] == None or index != 2:
                if y[index] == 0:
                    self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(I)V
""")
                if y[index] == 1:
                    self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(F)V
""")
                if y[index] == 2:
                    self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
""")
                if y[index] == 3:
                    self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
""")
            for d in self.ids:
                if (d[0] == y[0]):
                    if d[2] == 0:
                        self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(I)V
    """)
                    if d[2] == 1:
                        self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(F)V
    """)
                    if d[2] == 3:
                        self.prog[self.func].append(f"""
          invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    """)

        pass


    # Exit a parse tree produced by trabParser#inputFunc.
    def exitInputFunc(self, ctx: PythonParser.InputFuncContext):
        x = str(ctx.ID());
        for i in self.ids:
            if i[0] == x:
                self.prog[self.func].append(f"""
        invokestatic trabCompiladores.read()I
        istore {self.ids.index(i)}
                """)
                ctx.value = i
        pass


    # Exit a parse tree produced by trabParser#BoolTFExpr.
    def exitBoolTFExpr(self, ctx: PythonParser.BoolTFExprContext):
        x = str(ctx.BOOL())
        ctx.value = [None, bool(x), 2]
        pass


    # Exit a parse tree produced by trabParser#StringExpr.
    def exitStringExpr(self, ctx: PythonParser.StringExprContext):
        x = str(ctx.STRING())
        self.prog[self.func].append(f"""
        ldc {x}""")
        ctx.value = [None, x, 3]
        pass


    # Exit a parse tree produced by trabParser#FloatExpr.
    def exitFloatExpr(self, ctx: PythonParser.FloatExprContext):
        x = float(str(ctx.FLOAT()))
        self.prog[self.func].append(f"""
        ldc {x}""")
        ctx.value = [None, x, 1]
        pass


    # Exit a parse tree produced by trabParser#IdExpr.
    def exitIdExpr(self, ctx: PythonParser.IdExprContext):
        x = str(ctx.ID())
        for i in self.ids:
            if (x == i[0]):
                ctx.value = i
                if i[2] == 0:
                    self.prog[self.func].append(f"""
        iload {self.ids.index(i)}""")
                if i[2] == 1:
                    self.prog[self.func].append(f"""
        fload {self.ids.index(i)} """)
                if i[2] == 2:
                    self.prog[self.func].append(f"""
        aload {self.ids.index(i)}""")
                if i[2] == 3:
                    self.prog[self.func].append(f"""
        aload {self.ids.index(i)}""")

        pass


    # Exit a parse tree produced by trabParser#CompExpr.
    def exitCompExpr(self, ctx: PythonParser.CompExprContext):
        e2 = ctx.e2.value
        e1 = ctx.e1.value
        x = ctx.op.text
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]
        indexE1 = 2
        indexE2 = 2
        if e1 in vars:
            indexE1 = 0
            ctx.value = e1
        if e2 in vars:
            indexE2 = 0
            ctx.value = e2
        if not (e1 in vars) and not (e2 in vars):
            ctx.value = [e1[2], self.tipo(e1[2])]
        if e1[indexE1] != e2[indexE2]:
            raise ValueError(
                f"Variável {e1[0] or e1[1]} e {e2[0] or e2[1]} com tipos incompatíveis para operação {ctx.op.text} ")
            return
        if e1[indexE1] in [1, 2, 3]:
            raise ValueError(f"tipo {self.tipo(e1[indexE1])} incompatível com operação {ctx.op.text}")
            return
        self.valueIf = self.valueIf + 1
        self.ifs[self.func].append([len(self.prog[self.func]) + 2, self.valueIf])
        if x == ">":
            self.prog[self.func].append(f"""
        if_icmpgt Label{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}
            """)
        if x == "<":
            self.prog[self.func].append(f"""
        if_icmplt Label{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}       
            """)
        if x == ">=":
            self.prog[self.func].append(f"""
        if_icmpge Label{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}   
            """)
        if x == "<=":
            self.prog[self.func].append(f"""
        if_icmple Label{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}     
            """)
        self.prog[self.func].append(f"""
        Retorno{self.valueIf}:
            """)
        pass

    # Exit a parse tree produced by trabParser#CompAllExpr.
    def exitCompAllExpr(self, ctx: PythonParser.CompAllExprContext):
        e2 = ctx.e2.value
        e1 = ctx.e1.value
        x = ctx.op.text
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]
        indexE1 = 2
        indexE2 = 2
        if e1 in vars:
            indexE1 = 0
            ctx.value = e1
        if e2 in vars:
            indexE2 = 0
            ctx.value = e2
        if not (e1 in vars) and not (e2 in vars):
            ctx.value = [e1[2], self.tipo(e1[2])]
        if e1[indexE1] != e2[indexE2]:
            raise ValueError(
                f"Variável {e1[0] or e1[1]} e {e2[0] or e2[1]} com tipos incompatíveis para operação {ctx.op.text} ")
            return
        if e1[indexE1] in [1, 2, 3]:
            raise ValueError(f"tipo {self.tipo(e1[indexE1])} incompatível com operação {ctx.op.text}")
            return
        self.valueIf = self.valueIf + 1
        self.ifs[self.func].append([len(self.prog[self.func]) + 2, self.valueIf])
        if x == "==":
            self.prog[self.func].append(f"""
              if_icmpeq Label{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}
                  """)
        if x == "!=":
            self.prog[self.func].append(f"""
              if_icmpne Label{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}       
                  """)
        self.prog[self.func].append(f"""
              Retorno{self.valueIf}:
                  """)
        pass


    # Exit a parse tree produced by trabParser#IntegerExpr.
    def exitIntegerExpr(self, ctx: PythonParser.IntegerExprContext):
        x = int(str(ctx.INT()))
        self.prog[self.func].append(f"""
        ldc {x}""")
        ctx.value = [None, x, 0]
        pass


    # Exit a parse tree produced by trabParser#MulDivExpr.
    def exitMulDivExpr(self, ctx: PythonParser.MulDivExprContext):
        e2 = ctx.e2.value
        e1 = ctx.e1.value
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]
        indexE1 = 2
        indexE2 = 2
        if e1 in vars:
            indexE1 = 0
            ctx.value = e1
        if e2 in vars:
            indexE2 = 0
            ctx.value = e2
        if not (e1 in vars) and not (e2 in vars):
            ctx.value = [e1[2], self.tipo(e1[2])]
        if e1[indexE1] != e2[indexE2]:
            raise ValueError(
                f"Variável {e1[0] or e1[1]} e {e2[0] or e2[1]} com tipos incompatíveis para operação {ctx.op.text} ")
            return
        if e1[indexE1] in [2, 3]:
            raise ValueError(f"tipo {self.tipo(e1[indexE1])} incompátivel com operação {ctx.op.text}")
            return

        if ctx.op.text == "*":
            if (e1[indexE1] == 0 or e2[indexE2] == 0):
                self.prog[self.func].append(f"""
        imul""")
            if (e1[indexE1] == 1 or e2[indexE2] == 1):
                self.prog[self.func].append(f"""
        fmul""")
        else:
            if (e1[indexE1] == 0 or e2[indexE2] == 0):
                self.prog[self.func].append(f"""
        idiv""")
            if (e1[indexE1] == 1 or e2[indexE2] == 1):
                self.prog[self.func].append(f"""
        fdiv""")
        pass


    # Exit a parse tree produced by trabParser#AddSubExpr.
    def exitAddSubExpr(self, ctx: PythonParser.AddSubExprContext):
        e2 = ctx.e2.value
        e1 = ctx.e1.value
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]
        indexE1 = 2
        indexE2 = 2
        if e1 in vars:
            indexE1 = 0
            ctx.value = e1
        if e2 in vars:
            indexE2 = 0
            ctx.value = e2
        if not (e1 in vars) and not (e2 in vars):
            ctx.value = [e1[2], self.tipo(e1[2])]
        if e1[indexE1] != e2[indexE2]:
            raise ValueError(
                f"Variável {e1[0] or e1[1]} e {e2[0] or e2[1]} com tipos incompatíveis para operação {ctx.op.text} ")
            return
        if e1[indexE1] in [2, 3]:
            raise ValueError(f"tipo {self.tipo(e1[indexE1])} incompátivel com operação {ctx.op.text}")
            return

        if ctx.op.text == "+":
            if (e1[indexE1] == 0 or e2[indexE2] == 0):
                self.prog[self.func].append(f"""
        iadd""")
            if (e1[indexE1] == 1 or e2[indexE2] == 1):
                self.prog[self.func].append(f"""
        fadd""")
        else:
            if (e1[indexE1] == 0 or e2[indexE2] == 0):
                self.prog[self.func].append(f"""
        isub""")
            if (e1[indexE1] == 1 or e2[indexE2] == 1):
                self.prog[self.func].append(f"""
        fsub""")
        pass



del PythonParser
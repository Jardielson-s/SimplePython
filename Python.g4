grammar Python;

prog: varDecl* funcDecl* mainBlock
    ;
listaDecVars returns [int value]: listaIds|listaAtribs ;
varDecl returns [int val]: (listaIds | listaAtribs)';'
    ;
decVars returns [int value]: tipo varDecl
    ;
decParam returns [int value]: tipo (ID)
    ;
tipo returns [int val]:
    'int'
    |'float'
    |'boolean'
    |'string'
;

listaIds returns [int value]: ID(',' ID)*
    ;
atrib returns [int value]: ID '=' (expr);
listaAtribs returns [int value]: atrib (',' atrib)*;
typeFunc returns [int value]: tipo | 'void';
funcDecl returns [int val]:    ('def' typeFunc ID '(' listaParams* ')' ':'
                stmts+
            '}')+
    ;
mainBlock: 'main' '(' ')' ':' stmts+  '}'
    ;
returnFunc returns [int value]: 'return' expr ';';
stmts returns [int value]: cmdFor
    | cmdWhile
    |  cmdIF
    |   cmdAtrib
    | functions_native
    | ID ID operacao ID '(' expr ')' ';'
    | ID (NUM | ID) ';'
    | ID'(' ID expr ')' ';'
    | returnFunc
;
stats_com_break returns [int value]: stmts
    | 'break'';'
;
stmts_break returns [int value]: stmts | cmdIf_break  | 'break' ';'
;
callFunction returns [int value]: ID '('(expr)')' ';'
    ;
cmdAtrib returns [int value]: ID '=' expr;
cmdFor returns [int value]: 'for' ID 'in' 'range' '(' Range ')' ':' stats_com_break '}' # ForCond
;
cmdWhile returns [int value]: 'while' '(' expr ')' ':' stats_com_break '}' # WhileCond
    ;
printFunc returns [int value]: 'print' (expr)+(',' (expr))* ';';
inputFunc returns [int value]: ID '=' 'input' '(' ')';
cmdIF returns [int value]: 'if' expr ':' stmts+ '}' ('else' ':' stmts+ '}')? #IfCond
;

cmdIf_break returns [int value]: 'if' expr ':' stmts_break* '}' ('else' ':' stmts_break* '}')? # IfBreakCond
;
expr returns [int value]
    :
    callFunction                                                    # CallExpr
    | '-'+ e=expr                                                   # MinusExpr
    | '+'+ e=expr                                                   # PlusExpr
    | 'not' + e=expr                                                  # NegateExpr
    | e1=expr op=('*' | '/')+ e2=expr                               # MulDivExpr
    | e1=expr op=('+' | '-')  e2=expr                               # AddSubExpr
    | e1=expr op=('>' | '<' | '>=' | '<=')+ e2=expr                 # CompExpr
    | e1=expr op=('==' | '!=')+ e2=expr                             # CompAllExpr
    | e1=expr op=('and'|'or')+ e2=expr                              # BoolExpr
    | e1=ID                                                         # IdExpr
    | e1=INT                                                        # IntegerExpr
    | e1=FLOAT                                                      # FloatExpr
    | e1=BOOL                                                       # BoolTFExpr
    | e1=STRING                                                     # StringExpr
    | e1='(' expr ')'                                               # ParensExpr
    | e1=cmdAtrib                                                   # AssignExpr
    ;
term returns [int val]
    : t1=term  operacao  factor  #DIVMult
    | factor            #Fator
    ;
factor returns [int val]
    :   '('  expr  ')' (';')?  #ExpParenteses
    | (ID | NUM)          #Numero
    ;

Range:
NUM | NUM ',' NUM
;
listaParams:    tipo ID | tipo ID ',' listaParams
  ;
functions_native:                   ID  operacao  'input' '(' ')'  ';'

       | 'print'  (NUM| ID)+
       |'print' STRING ',' (NUM | ID) operacao (NUM| ID)
       | 'print' STRING ',' (NUM | ID)
       |'print' STRING  ','  STRING
       |'print' STRING
       ;
operacao: 'not' | '-' | 'and' | 'or' | '+' | '-' | '+' | '*' | '/' | '=='
          | '!=' | '>=' | '<=' | '>' | '<' | '=';
BOOL: 'True'|'False';
ID: [a-zA-Z]+[a-zA-Z0-9]*;
NUM: [0-9]+('.'[0-9]+)?;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
SL_COMMENT:
    '//' .*? '\n' -> skip
    ;
INT: [0-9]+;
FLOAT: [0-9]+('.' [0-9]*);
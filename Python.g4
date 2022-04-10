grammar Python;

prog: varDecl* funcDecl mainBlock
    ;

varDecl: type (listaIds | listaAtribs)';'
    ;
type:   'int'
    |   'float'
    |   'boolean'
    |   'string'
    ;

listaIds: ID(',' ID)*
    ;
listaAtribs:  ID '=' (ID|NUM|STRING)

    ;
funcDecl:   'def' type ID '(' listaParams* ')' ':'
                stats+
            '}'
    ;
mainBlock: 'main' '(' ')' ':' stats+ '}'
    ;
stats: cmdFor
    | cmdWhile
    |  cmdIF
    |   cmdAtrib
    | functions_native
;
stats_com_break: stats
    | 'break'';'
    ;
cmdAtrib: ID '=' expr;
cmdFor: 'for' ID 'in' 'range' '(' range ')' ':' stats_com_break '}'
;
cmdWhile: 'while' '(' expr ')' ':' stats_com_break '}'
    ;
cmdIF: 'if' expr ':' stats '}' ('else' ':' stats '}')?
;

expr returns [int val]
    : e1= expr  operacao  term ';'  #SomaSub
    |  term              #Termo
    ;
term returns [int val]
    : t1=term  operacao  factor  #DIVMult
    | factor            #Fator
    ;
factor returns [int val]
    : '('  expr  ')' ';' #ExpParenteses
    |  NUM           #Numero
    ;

range:
NUM | NUM ',' NUM
;
listaParams:    type  ID | type ID ',' listaParams
  ;
functions_native:                   ID  operacao  'input' '(' ')'  ';'
                |                  print';'
                ;
print: 'print'  (NUM| ID)+
       |'print' STRING ',' (NUM | ID) operacao (NUM| ID)
       |'print' STRING  ','  STRING
       |'print' STRING
       ;
operacao: 'not' | '-' | 'and' | 'or' | '+' | '-' | '+' | '*' | '/' | '=='
          | '!=' | '>=' | '<=' | '>' | '<' | '=';
ID: [a-zA-Z]+[a-zA-Z0-9]*;
NUM: [0-9]+('.'[0-9]+)?;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
SL_COMMENT:
    '//' .*? '\n' -> skip
    ;

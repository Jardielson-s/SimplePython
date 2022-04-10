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

//lines: line+
//    ;
//line: expr NEWLINE
//    ;
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
//prog: code | line+;
//
//code:
//    laco_repeticao
//    | condicionais
//    | functions
//    | variavel
//    | main
//    |functions_native
//    | EOF;
//
//laco_repeticao:
//    'for' (NullSpaces)+ Identifier (NullSpaces)+ 'in' (NullSpaces)+ 'range' (NullSpaces)*  '('  (NullSpaces)* list_numbers (NullSpaces)* ')'  (NullSpaces)* ':' (NullSpaces)*
//                 (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
//     '}'(NullSpaces)* (prog?EOF)*
//     |
//     'while'(NullSpaces)+ Identifier (NullSpaces)*  operacao (NullSpaces)* Identifier (NullSpaces)*':' (NullSpaces)*
//               (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
//      '}'(NullSpaces)* (prog?EOF)*
//      ;
//condicionais:
//         'if' (NullSpaces)+ Identifier (NullSpaces)*  operacao (NullSpaces)* Identifier (NullSpaces)*':'(NullSpaces)*
//            (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
//         '}' ((NullSpaces)* 'else' (NullSpaces)+ ':' (NullSpaces)*
//            (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
//         '}')* (NullSpaces)* (prog?EOF)*
//        ;
//functions:
//          'def' (NullSpaces)+ Tipo (NullSpaces)+ Identifier (NullSpaces)* '(' (NullSpaces)* lista_parametros* (NullSpaces)* ')' (NullSpaces)* ':' (NullSpaces)*
//                (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
//                ((NullSpaces)* 'return' (NullSpaces)* declaracao (NullSpaces)* ';')*
//          '}' (WS |NullSpaces)* (prog?EOF)* | WS;
//
//operacao: 'not' | '-' | 'and' | 'or' | '+' | '-' | '+' | '*' | '/' | '=='
//          | '!=' | '>=' | '<=' | '>' | '<' | '=';
//
//variavel:
//         (NullSpaces)*  Tipo (NullSpaces)+ Identifier (NullSpaces)* ';' (prog?EOF)*
//          | (NullSpaces)*  Tipo (NullSpaces)+ Identifier (NullSpaces)* operacao (NullSpaces)* op = (Number | Identifier | NumberPreviousLetter) (NullSpaces)*';'    (prog?EOF)*
//          | (NullSpaces)*  Tipo (NullSpaces)+ Identifier (NullSpaces)* operacao (NullSpaces)* op = (Number | Identifier | NumberPreviousLetter)  (NullSpaces)* ';'  (prog?EOF)*
//          | (NullSpaces)*  Tipo (NullSpaces)+ Identifier (NullSpaces)* ',' (NullSpaces)* variavel
//          | (NullSpaces)*  Tipo (NullSpaces)+ Identifier (NullSpaces)* operacao (NullSpaces)* (Identifier | Number) (NullSpaces)* ',' variavel
//          |(NullSpaces)*
//          ;
//main:
//    'main' (NullSpaces)* '(' (NullSpaces)* ')' (NullSpaces)* ':'  (NullSpaces)*
//            (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
//    '}' (NullSpaces)* (prog?EOF)*;
//functions_native:
//                Identifier (NullSpaces)* operacao (NullSpaces)* 'input' (NullSpaces)*'('(NullSpaces)* ')' (NullSpaces)* ';' (prog?EOF)*
//                | 'print' (NullSpaces)* '"' (Number | Identifier | NumberPreviousLetter) (NullSpaces)* '"' (NullSpaces)* ';' (prog?EOF)*
//                | 'print' (NullSpaces)* '"' (Number | Identifier | NumberPreviousLetter) (NullSpaces)*',' functions_native
//                | 'print' (NullSpaces)* (Number | Identifier ) (NullSpaces)* ';' (prog?EOF)*
//                | 'print' (NullSpaces)* '"' (Number | Identifier | NumberPreviousLetter)  (NullSpaces)*  operacao (NullSpaces)* (Number | Identifier | NumberPreviousLetter)  (NullSpaces)* (NullSpaces)* operacao (NullSpaces)* '"' (NullSpaces)* ',' (NullSpaces)* (Number | Identifier) (NullSpaces)* operacao (NullSpaces)* (Number | Identifier ) (NullSpaces)* ';' (prog?EOF)*;
//
//
//lista_parametros: Identifier | Identifier (NullSpaces)* ',' (NullSpaces)* lista_parametros | (NullSpaces)*  Tipo (NullSpaces)+ Identifier (NullSpaces)* ','(NullSpaces)* lista_parametros | (NullSpaces)*  Tipo (NullSpaces)+ Identifier (NullSpaces)*;
//lines: line+
//    ;
//line: expr NEWLINE
//    ;
//expr returns [int val]
//    : e1= expr (NullSpaces)* operacao (NullSpaces)* term (NullSpaces)* ';' (NullSpaces)*  #SomaSub
//    | (NullSpaces)* term   (NullSpaces)*            #Termo
//    ;
//term returns [int val]
//    : t1=term (NullSpaces)* operacao (NullSpaces)* factor (NullSpaces)* #DIVMult
//    |(NullSpaces)* factor  (NullSpaces)*           #Fator
//    ;
//factor returns [int val]
//    : (NullSpaces)*'(' (NullSpaces)* expr (NullSpaces)* ')'(NullSpaces)* ';' (NullSpaces)*  #ExpParenteses
//    | (NullSpaces)* Number (NullSpaces)*           #Numero
//    ;
//
//list_numbers: Number | (NullSpaces)* Number (NullSpaces)* ',' (NullSpaces)* list_numbers;
//Number: [0-9]+;
//NumberPreviousLetter: [0-9]+[a-zA-Z];
//NEWLINE: '\r'?'\n' ;
//WS   : [\n\t]+ -> skip;
//Tipo: 'void' | 'int' | 'string' | 'boolean' | 'float';
//declaracao: functions_native | (NullSpaces)* Number (NullSpaces)*| (NullSpaces) (prog?EOF)* ;
//NullSpaces: ' ';
//Identifier: [a-zA-Z]+[0-9]*;
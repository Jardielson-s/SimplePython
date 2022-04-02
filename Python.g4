grammar Python;


prog: code | line+;

code:
    laco_repeticao
    | condicionais
    | functions
    | variavel
    | main
    |functions_native
    | EOF;

laco_repeticao:
    'for' (NullSpaces)+ Identifier (NullSpaces)+ 'in' (NullSpaces)+ 'range' (NullSpaces)*  '('  (NullSpaces)* list_numbers (NullSpaces)* ')'  (NullSpaces)* ':' (NullSpaces)*
                 (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
     '}'
     |
     'while'(NullSpaces)+ Identifier (NullSpaces)*  operacao (NullSpaces)* Identifier (NullSpaces)*':' (NullSpaces)*
               (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
      '}'
     |
     WS;
condicionais:
         'if' (NullSpaces)* Identifier (NullSpaces)*  operacao (NullSpaces)* Identifier (NullSpaces)*':'(NullSpaces)*
            (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
         '}' ((NullSpaces)* 'else' (NullSpaces)* ':' (NullSpaces)*
            (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
         '}')*
        ;
functions:
          'def' (NullSpaces)* Tipo (NullSpaces)+ Identifier (NullSpaces)* '(' (NullSpaces)* lista_parametros* (NullSpaces)* ')' (NullSpaces)* ':' (NullSpaces)*
                (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
                (NullSpaces)* 'return' (NullSpaces)* declaracao (NullSpaces)* ';'
          '}';


operacao: 'not' | '-' | 'and' | 'or' | '+' | '-' | '+' | '*' | '/' | '=='
          | '!=' | '>=' | '<=' | '>' | '<' | '=';

variavel: Tipo (NullSpaces)* Identifier (NullSpaces)* ';'
          | Tipo (NullSpaces)* Identifier (NullSpaces)* operacao (NullSpaces)* op = (Number | Identifier | NumberPreviousLetter) (NullSpaces)';'
          | Tipo (NullSpaces)* Identifier (NullSpaces)* operacao (NullSpaces)* op = (Number | Identifier | NumberPreviousLetter)  (NullSpaces)* ';'
          | Tipo (NullSpaces)* Identifier (NullSpaces)* ',' (NullSpaces)* variavel
          | Tipo (NullSpaces)* Identifier (NullSpaces)* operacao (NullSpaces)* (Identifier | Number) (NullSpaces)* ',' variavel
          |(NullSpaces)* ;
main:
    'main' (NullSpaces)* '(' (NullSpaces)* ')' (NullSpaces)* ':'  (NullSpaces)*
            (NullSpaces)* (declaracao | laco_repeticao)+ (NullSpaces)*
    '}';
functions_native:
                Identifier (NullSpaces)* operacao (NullSpaces)* 'input' (NullSpaces)*'('(NullSpaces)* ')' (NullSpaces)* ';'
                | 'print' (NullSpaces)* '"' (Number | Identifier | NumberPreviousLetter) (NullSpaces)* '"' (NullSpaces)* ';'
                | 'print' (NullSpaces)* '"' (Number | Identifier | NumberPreviousLetter) (NullSpaces)*',' functions_native
                | 'print' (NullSpaces)* (Number | Identifier ) (NullSpaces)* ';'
                | 'print' (NullSpaces)* '"' (Number | Identifier | NumberPreviousLetter)  (NullSpaces)*  operacao (NullSpaces)* (Number | Identifier | NumberPreviousLetter)  (NullSpaces)* (NullSpaces)* operacao (NullSpaces)* '"' (NullSpaces)* ',' (NullSpaces)* (Number | Identifier) (NullSpaces)* operacao (NullSpaces)* (Number | Identifier ) (NullSpaces)* ';';


lista_parametros: Identifier | Identifier (NullSpaces)* ',' (NullSpaces)* lista_parametros;
lines: line+
    ;
line: expr NEWLINE
    ;
expr returns [int val]
    : e1= expr (NullSpaces)* operacao (NullSpaces)* term (NullSpaces)* ';' (NullSpaces)*  #SomaSub
    | (NullSpaces)* term   (NullSpaces)*            #Termo
    ;
term returns [int val]
    : t1=term (NullSpaces)* operacao (NullSpaces)* factor (NullSpaces)* #DIVMult
    |(NullSpaces)* factor  (NullSpaces)*           #Fator
    ;
factor returns [int val]
    : (NullSpaces)*'(' (NullSpaces)* expr (NullSpaces)* ')'(NullSpaces)* ';' (NullSpaces)*  #ExpParenteses
    | (NullSpaces)* Number (NullSpaces)*           #Numero
    ;

list_numbers: Number | (NullSpaces)* Number (NullSpaces)* ',' (NullSpaces)* list_numbers;
Number: [0-9]+;
NumberPreviousLetter: [0-9]+[a-zA-Z];
NEWLINE: '\r'?'\n' ;
WS   : [\n\t]+ -> skip;
Tipo: 'void' | 'int' | 'string' | 'boolean' | 'float';
declaracao: functions_native | (NullSpaces)* Number (NullSpaces)* ;
NullSpaces: ' ';
Identifier: [a-zA-Z]+[0-9]*;

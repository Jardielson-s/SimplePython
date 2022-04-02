grammar Python;


prog: code | line+;

code:
    laco_repeticao
    | condicionais
    | functions
    | variavel
    | EOF;

laco_repeticao:
    'for' (NullSpaces)+ Identifier (NullSpaces)+ 'in' (NullSpaces)+ 'range' (NullSpaces)*  '('  (NullSpaces)* Number (NullSpaces)* ')'  (NullSpaces)* ':' (NullSpaces)*
                 (NullSpaces)* (Declaracao | laco_repeticao)+ (NullSpaces)*
     '}'
     |
     'while'(NullSpaces)+ Identifier (NullSpaces)*  operacao (NullSpaces)* Identifier (NullSpaces)*':' (NullSpaces)*
               (NullSpaces)* (Declaracao | laco_repeticao)+ (NullSpaces)*
      '}'
     |
     WS;
condicionais:
        'if' (NullSpaces)* Identifier (NullSpaces)*  operacao (NullSpaces)* Identifier (NullSpaces)*':'(NullSpaces)*
            (NullSpaces)* (Declaracao | laco_repeticao)+ (NullSpaces)*
         '}'
        ;
functions:
          'def' (NullSpaces)* Tipo (NullSpaces)+ Identifier (NullSpaces)* '(' (NullSpaces)* lista_parametros* (NullSpaces)* ')' (NullSpaces)* ':' (NullSpaces)*
                (NullSpaces)* (Declaracao | laco_repeticao)+ (NullSpaces)*
                (NullSpaces)* 'return' (NullSpaces)* Declaracao (NullSpaces)* ';'
          '}';


operacao: 'not' | '-' | 'and' | 'or' | '+' | '-' | '+' | '*' | '/' | '=='
          | '!=' | '>=' | '<=' | '>' | '<' | '=';

variavel: Tipo (NullSpaces)* Identifier (NullSpaces)* ';'
          | Tipo (NullSpaces)* Identifier (NullSpaces)* operacao (NullSpaces)* op = (Number | Identifier | NumberPreviousLetter)  (NullSpaces)* ';'
          | Tipo (NullSpaces)* Identifier (NullSpaces)* ',' (NullSpaces)* variavel
          | Tipo (NullSpaces)* Identifier (NullSpaces)* operacao (NullSpaces)* (Identifier | Number) (NullSpaces)* ',' variavel
          |(NullSpaces)* ;

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

Number: [0-9]+;
NumberPreviousLetter: [0-9]+[a-zA-Z];
NEWLINE: '\r'?'\n' ;
WS   : [\n\t]+ -> skip;
Tipo: 'void' | 'int' | 'string' | 'boolean';
Declaracao: 'here;' ;
NullSpaces: ' ';
Identifier: [a-zA-Z]+[0-9]*;



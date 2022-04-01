grammar Python;


prog: code | line+;

code:
    laco_repeticao
    | condicionais
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


operacao: 'not' | '-' | 'and' | 'or' | '+' | '-' | '+' | '*' | '/' | '=='
          | '!=' | '>=' | '<=' | '>' | '<';

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
    | (NullSpaces)* NUM (NullSpaces)*           #Numero
    ;

NUM: [0-9]+ ;
NEWLINE: '\r'?'\n' ;
WS   : [\n\t]+ -> skip;
Declaracao: 'here;' ;
NullSpaces: ' ';
Identifier: [a-zA-Z]+[0-9]*;
Number: [0-9]+;


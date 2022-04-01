grammar Python;


prog: code;

code:
    laco_repeticao
    | EOF;

laco_repeticao:
    'for' (NullSpaces)+ Identifier (NullSpaces)+ 'in' (NullSpaces)+ 'range' (NullSpaces)*  '('  (NullSpaces)* Number (NullSpaces)* ')'  (NullSpaces)* ':' (NullSpaces)*
                 (NullSpaces)* (Declaracao | laco_repeticao)+ (NullSpaces)*
     '}'
     |
     'while'(NullSpaces)+ Identifier (NullSpaces)*  operacao (NullSpaces)* Identifier (NullSpaces)*  (NullSpaces)*':' (NullSpaces)*
               (NullSpaces)* (Declaracao | laco_repeticao)+ (NullSpaces)*
      '}'
     |
     WS;



operacao: '==';
WS   : ' '[\n\t]+ -> skip;
Declaracao:  'Declarehere;';
NullSpaces: ' ';
Identifier: [a-zA-Z]+[0-9]*;
Number: [0-9]+;

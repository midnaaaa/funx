grammar Expr;
root : funcs* stat? EOF ;

stat : expr                         #expres
    | ID '<-' booleans              #assig
    | ID '<-' expr                  #assig
    | 'if' booleans bloc ('else' bloc)? #ifelse
    | 'while' booleans bloc #bucle
    ;

funcs : FUN ID* bloc #decfunc
    ;


booleans : expr ('=' | '!=' | '<' | '>' | '<=' | '>=') expr
    ;

expr : '(' expr ')'                #par
    | <assoc=right> expr '^' expr  #bin
    | expr ('*' | '/' | '%') expr  #bin
    | expr ('+' | '-') expr        #bin
    | NUM                          #val
    | ID                           #id
    | FUN expr*                    #func
    ;


bloc : '{' stat+ '}'
    ;


FUN : [A-Z][a-zA-Z0-9]* ;
ID : [a-z][a-zA-Z0-9]* ;
NUM : [0-9]+ ;
COM : '#'~[\n]*[\n]? -> skip ;
WS : [ \n]+ -> skip ;

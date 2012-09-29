grammar VPL;

// Compile to Python
options {
  language=Python;
}

/*
  Non-Terminals
*/
start : m ;

m : function m
  | ; // epsilon

// Functions
function : 'func' IDENT parenth defin state 'end' ;

// Lists
parenth : '(' list ')' ;
list : IDENT
     | IDENT ',' list ;

// Defintions
defin : 'var' list ';'
      | ; // epsilon

// Statements
state : 'if' cond 'then' state 'else' state 'endif' 
      | 'while' cond 'do' state 'endwhile' 
      | IDENT '=' expr statement
      | ; // epsilon

statement : ';' state 
          | ; // epsilon
      

// Expressions
expr : 'min' '(' expr ','  expr ')' 
     | '(' expr ')'
     | NUM expression
     | IDENT expression;

expression : '+' expr
           | '-' expr
           | '*' expr
           | '/' expr
           | ;

// Conditions
cond : expr '<' NUM ;

/*
  Terminals
*/
IDENT : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;
NUM : '0'..'9'+ ('.' '0'..'9'+)? ;
WS  : (' '|'\r'|'\n')+ {$channel = HIDDEN;} ;

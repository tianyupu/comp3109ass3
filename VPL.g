grammar VPL;

// Compile to Python
options {
  language=Python;
}

/*
  Non-Terminals
*/

start : main ;

main : function main
     | ; // epsilon

// Functions
function : 'func' IDENT param declare state 'end' ;

// Paramaters
param : '(' list ')' ;
list : IDENT
     | IDENT ',' list ;

// Declarations
declare : 'var' list ';'
        | ; // epsilon

// Statements
state : 'if' cond 'then' state 'else' state 'endif' statement
      | 'while' cond 'do' state 'endwhile' statement 
      | IDENT '=' expr statement
      | ; // epsilon

statement : ';' state 
          | ; // epsilon

// Expressions
expr : 'min' '(' expr ','  expr ')' op
     | '(' expr ')' op
     | NUM op
     | IDENT op;

// Operations
op : '+' expr
   | '-' expr
   | '*' expr
   | '/' expr
   | ; // epsilon

// Conditions
cond : expr '<' NUM ;



/*
  Terminals
*/

IDENT : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;
NUM : '0'..'9'+ ('.' '0'..'9'+)? ;
WS  : (' '|'\r'|'\n')+ {$channel = HIDDEN;} ;

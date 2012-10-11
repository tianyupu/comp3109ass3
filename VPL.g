grammar VPL;

/*
  Initialisation and Configuration
*/
options {
  language=Python;
  output=AST;
}

tokens {
  PROGRAM;
  FUNCTION;
  PARAMS;
  DECLS;
  STATEMENTS;
  ASSIGN;
  EXPR;
  MIN;
  FACTOR;
}

/*
  Non-Terminals
*/

// The main program
program :
  function*
  -> ^(PROGRAM function*)
;

// Functions
function : 
  'func' name=IDENT params localvars=declare body=statements 'end'
  -> ^(FUNCTION $name ^(PARAMS params) ^(DECLS $localvars?) $body)
;

// Parameters
params :
  '(' list ')'
  -> list
;

list :
  id1=IDENT (','! id2=IDENT)*
;

// Declarations
declare :
  'var' list ';'
  -> list
  
  | // epsilon
;

// Statements
statements :
  state (';' state)*
  -> ^(STATEMENTS state*)
;

state  :
    'if' cond 'then' statements 'else' statements 'endif'
  
  | 'while' cond 'do' statements 'endwhile'
  
  | var=IDENT '=' expr 
    -> ^(ASSIGN $var expr)
  
  | // epsilon
;

// Expressions
expr :
  left=factor
  (op^ right=factor)*
;

factor :
  | NUM
  -> ^(FACTOR NUM)

  | IDENT
  -> ^(FACTOR IDENT)

  | 'min' '(' e1=expr ','  e2=expr ')'
  -> ^(MIN $e1 $e2)

  | '('! expr ')'!
;

// Operations
op :
    '+'
  | '-'
  | '*'
  | '/'
;

// Conditions
cond  :
  expr '<' NUM
;


/*
  Terminals
*/

IDENT : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;
NUM : '0'..'9'+ ('.' '0'..'9'+)? ;
WS  : (' '|'\r'|'\n')+ {$channel = HIDDEN;} ;

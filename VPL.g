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
}

/*
  Non-Terminals
*/

// The main program
program :
  function* EOF
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
  | IDENT '=' factor 
  | // epsilon
;

// Expressions
factor :
  left=expr (op right=expr)*
;

expr :
  | 'min' '(' expr ','  expr ')'
  | '(' expr ')'
  | NUM
  | IDENT
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

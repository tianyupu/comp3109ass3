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
  IF;
  WHILE;
  COND;
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
    'if' cond 'then' s1=statements 'else' s2=statements 'endif'
    -> ^(IF cond $s1 $s2)
  
  | 'while' cond 'do' statements 'endwhile'
    -> ^(WHILE cond statements)
  
  | var=IDENT '=' expr 
    -> ^(ASSIGN $var expr)
  
  | // epsilon
;

// Expressions
expr:
  addsub_expr
;

addsub_expr :
  left=muldiv_expr
  (('+'|'-')^ right=muldiv_expr)*
;

muldiv_expr :
  left=factor
  (('*'|'/')^ right=factor)*
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

// Conditions
cond  :
  expr '<' const=NUM
  -> ^(COND expr ^(FACTOR $const))
;


/*
  Terminals
*/

IDENT : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;
NUM : '0'..'9'+ ('.' '0'..'9'+)? ;
WS  : (' '|'\r'|'\n')+ {$channel = HIDDEN;} ;

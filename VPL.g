grammar VPL;

/*
  Initialisation and Configuration
*/
options {
  language=Python;
}

@init {
  import VPL
  self.VPL = VPL
  self.funcs = {}
}


/*
  Non-Terminals
*/

// The main program
start :
  main
;

main :
  function main
  | // epsilon
;

// Functions
function : 
  'func' IDENT param declare state 'end'
  // Add the new function to the list of functions
  {
    func_name = $IDENT.getText()
    params = $param.params
    self.funcs[func_name] = self.VPL.function.Function(func_name, params)
    print self.funcs[func_name]
  }
;

// Parameters
param returns [params] :
  '(' list ')'
  // The parameters are the indentities in the list
  { $params = $list.idents }
;

list returns [idents] :
  {$idents = set()} // Keep a set of the identities in the list
  id1=IDENT
  { $idents.add(id1.getText()) } // Add the new identity
  (
    ',' id2=IDENT
    { $idents.add(id2.getText()) } // Add the new identity
  )*
;

// Declarations
declare :
  'var' list ';'
  | // epsilon
;

// Statements
state :
    'if' cond 'then' state 'else' state 'endif' statement
  | 'while' cond 'do' state 'endwhile' statement
  | IDENT '=' expr statement
  | ';' state
  | // epsilon
;

statement :
  ';' state
  | // epsilon
;

// Expressions
expr :
    'min' '(' expr ','  expr ')' op
  | '(' expr ')' op
  | NUM op
  | IDENT op;

// Operations
op :
    '+' expr
  | '-' expr
  | '*' expr
  | '/' expr
  | // epsilon
;

// Conditions
cond :
  expr '<' NUM
;


/*
  Terminals
*/

IDENT : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;
NUM : '0'..'9'+ ('.' '0'..'9'+)? ;
WS  : (' '|'\r'|'\n')+ {$channel = HIDDEN;} ;

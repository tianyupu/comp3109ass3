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
  'func' IDENT param declare statements 'end'
  // Add the new function to the list of functions
  {
    #// Get the function name, parameters and local variables
    func_name = $IDENT.getText()
    params = $param.params
    vars = $declare.vars
    #// Create the function object
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
declare returns [vars]:
  'var' list ';'
  // The variables are the indentities in the list
  { $vars = $list.idents }
  | // epsilon
;

// Statements
statements :
  state (';' state)*
;

state :
    'if' cond 'then' statements 'else' statements 'endif'
  | 'while' cond 'do' statements 'endwhile'
  | IDENT '=' expr
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

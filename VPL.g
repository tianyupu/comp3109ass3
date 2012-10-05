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
  'func' IDENT
  {
    #// Create the function object
    func_name = $IDENT.getText()
    self.funcs[func_name] = self.VPL.function.Function(func_name, [])
    func = self.funcs[func_name]
  }
  param declare
  // Add the new function to the list of functions
  {
    #// Get the function name, parameters and local variables
    params = $param.params
    self.funcs[func_name].vars = params
    vars = $declare.vars
    print func
  }
  statements[func] 'end'
;

// Parameters
param returns [params] :
  '(' list ')'
  // The parameters are the indentities in the list
  {
    $params = {ident:self.VPL.variable.VecParam() for ident in $list.idents}
  }
;

list returns [idents] :
  { $idents = set() } // Keep a set of the identities in the list
  id1=IDENT
  { $idents.add(id1.getText()) } // Add the new identity
  (
    ',' id2=IDENT
    { $idents.add(id2.getText()) } // Add the new identity
  )*
;

// Declarations
declare returns [vars] :
  'var' list ';'
  // The variables are the indentities in the list
  { $vars = $list.idents }
  | // epsilon
;

// Statements
statements [func] :
  state[func] (';' state[func])*
;

state [func] :
    'if' cond 'then' statements[func] 'else' statements[func] 'endif'
  | 'while' cond 'do' statements[func] 'endwhile'
  | IDENT '=' expr 
  {
    v = $func.vars[$IDENT.getText()]
    print v.assign($expr.factor, 0)
  }
  | // epsilon
;

// Expressions
expr returns [factor] :
    'min' '(' expr ','  expr ')' op
  | '(' expr ')' op
  | NUM op
  {
    n = $NUM.getText()
    $factor = self.VPL.constant.Constant(int(n))
  }
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

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
  'func' IDENT param declare
  {
    # Reset counters
    self.VPL.variable.VecParam.nextreg = 0
    self.VPL.variable.LocalVar.nextvar = 0

    # Get the parameters and local variables
    params = $param.params
    vars = $declare.vars
    
    # Create the function object
    func_name = $IDENT.getText()
    self.funcs[func_name] = self.VPL.function.Function(func_name, params, vars)
    func = self.funcs[func_name]
  }
  statements[func] 'end'
  {
    # Output the function code
    print func
  }
;

// Parameters
param returns [params] :
  '(' list ')'
  // The parameters are the indentities in the list
  {
    # Dictionary mapping identities to parameters
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
  { 
    # Dictionary mapping identities to local variables
    $vars = {var: self.VPL.variable.LocalVar() for var in $list.idents}
  }
  | // epsilon
;

// Statements
statements [func] :
  state[func] (';' state[func])*
;

state [func] :
    'if' cond[func] 'then' statements[func] 'else' statements[func] 'endif'
  | 'while' cond[func] 'do' statements[func] 'endwhile'
  | IDENT '=' factor[func] 
  {
    # Add assignment to the function
    v = $func.getVar($IDENT.getText())
    $func.body += v.assign($factor.var, 0)
  }
  | // epsilon
;

// Expressions
factor [func] returns [var]:
  left=expr[func] (op right=expr[func])*
  {
    # Calculate the factor (TODO)
    $factor.var = left
  }
;

expr [func] returns [var] :
  | 'min' '(' expr[func] ','  expr[func] ')'
  | '(' expr[func] ')'
  | NUM
  {
    # Get the constant
    n = $NUM.getText()
    $var = $func.getConst(n)
  }
  | IDENT
  {
    # Retrieve the variable from the function
    $var = func.getVar($IDENT.getText())
  }
;

// Operations
op :
    '+'
  | '-'
  | '*'
  | '/'
;

// Conditions
cond [func] :
  expr[func] '<' NUM
;


/*
  Terminals
*/

IDENT : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;
NUM : '0'..'9'+ ('.' '0'..'9'+)? ;
WS  : (' '|'\r'|'\n')+ {$channel = HIDDEN;} ;

grammar VPL;

// Compile to Python
options {
  language=Python;
}

// header
@init {
  self.funcs = {}
}

/*
  Non-Terminals
*/

start : main ;

main : function main
     | ; // epsilon

// Functions
function 
  : 'func' IDENT param declare state 'end'
  // Importing VPL and making a list of functions
  {
    import VPL.function
    func_name = $IDENT.getText()
    params = $param.params
    self.funcs[func_name] = VPL.function.Function(func_name, params)
    print self.funcs[func_name]
  };


// Parameters
param returns [params]
     : '(' list ')' {$params = $list.params} ;
list returns [params]
  @init {$params = set()}
     : id1=IDENT
       { $params.add(id1.getText()) }
     ( ',' id2=IDENT
       { $params.add(id2.getText()) }
     )*;

// Declarations
declare : 'var' list ';'
        | ; // epsilon

// Statements
state : 'if' cond 'then' state 'else' state 'endif' statement
      | 'while' cond 'do' state 'endwhile' statement
      | IDENT '=' expr statement
      | ';' state
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

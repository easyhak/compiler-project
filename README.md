# 2023 Compiler Project Description
## 🌍 Goal: Implement a Bottom-Up Syntax Analyzer
### CFG Grammar
01: CODE → VDECL CODE | FDECL CODE | CDECL CODE| e   
02: VDECL → vtype id semi | vtype ASSIGN semi    
03: ASSIGN → id assign RHS    
04: RHS → EXPR | literal | character | boolstr    
05: EXPR → EXPR addsub EXPR | EXPR multdiv EXPR    
06: EXPR → lparen EXPR rparen | id | num    
07: FDECL → vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace    
08: ARG → vtype id MOREARGS | e     
09: MOREARGS → comma vtype id MOREARGS | e    
10: BLOCK → STMT BLOCK | e    
11: STMT → VDECL | ASSIGN semi    
12: STMT → if lparen COND rparen lbrace BLOCK rbrace ELSE     
13: STMT → while lparen COND rparen lbrace BLOCK rbrace     
14: COND → COND comp COND | boolstr    
15: ELSE → else lbrace BLOCK rbrace | e     
16: RETURN → return RHS semi     
17: CDECL → class id lbrace ODECL rbrace    
18: ODECL → VDECL ODECL | FDECL ODECL | e    

### Terminals
1. vtype for the types of variables and functions
2. num for signed integers
3. character for a single character
4. boolstr for Boolean strings
5. literal for literal strings
6. id for the identifiers of variables and functions
7. if, else, while, and return for if, else, while, and return statements respectively
8. class for class declarations 
9. addsub for + and - arithmetic operators
10. multdiv for * and / arithmetic operators
11. assign for assignment operators
12. comp for comparison operators
13. semi and comma for semicolons and commas respectively
14. lparen, rparen, lbrace, and rbrace for (, ), {, and } respectively

### Non-terminals
CODE, VDECL, ASSIGN, RHS, EXPR, FDECL, ARG, MOREARGS, BLOCK, STMT, COND, ELSE, 
RETURN, CDECL, ODECL
### Start symbol
CODE

### Descriptions
- The given CFG G is non-left recursive, but ambiguous. 
- Codes include zero or more declarations of functions, variables, and classes (CFG line 1)
- Variables are declared with or without initialization (CFG line 2 ~ 3)
- The right hand side of assignment operations can be classified into four types; 1) arithmetic 
operations (expressions), 2) literal strings, 3) a single character, and 4) Boolean strings (CFG 4)
- Arithmetic operations are the combinations of +, -, *, / operators (CFG line 5 ~ 6)
- Functions can have zero or more input arguments (CFG line 7 ~ 9)
- Function blocks include zero or more statements (CFG line 10)
- There are four types of statements: 1) variable declarations, 2) assignment operations, 3) if-else statements, and 4) while statements (CFG line 11 ~ 13)
- if and while statements include a conditional operation which consists of Boolean strings 
and condition operators (CFG line 12 ~ 14)
- if statements can be used with or without an else statement (CFG line 12 & 15)
- return statements return 1) the computation result of arithmetic operations, 2) literal strings, 3) a single character, or 4) Boolean strings (CFG line 16)
- class is declared with zero or more declarations of functions and variables (CFG line 17 ~ 18)
- This is not a CFG for JAVA. This is for simplified JAVA. So, you don’t need to consider grammars and structures not mentioned in this specification.

### Based on this CFG, you should implement a bottom-up parser as follows:
- Discard an ambiguity in the CFG
- Construct a SLR parsing table for the non-ambiguous CFG through the following website: 
<a href="http://jsmachines.sourceforge.net/machines/slr.html"> http://jsmachines.sourceforge.net/machines/slr.html </a>
- Implement a SLR parsing program for the simplified Java programming language by using the 
constructed table.

# Calclang

A simple calculator for evaluating functions

## Features
- Supports addition/subtraction/multiplication/division/exponentiation
- Supports simple trig functions (sin/cos/tan)
- Supports brackets
- Adhears to BIDMAS (i.e. brakcets -> indices (powers) -> division & multiplication -> addition & subtraction)

# Files
- lexer.py: takes a string statement and converts to a list of tokens
- calclang_parser.py: takes a list of tokens and generates an abstract syntax tree (ast)
- interpreter.py: takes an abstract syntax tree and interprets it
- tokens.py: class for tokens and token types (communication between lexer and parser)
- nodes.py: class for different node types (communication between parser and interpreter)
- calclang.py: class for combining the lexer -> parser -> interpreter pipeline
- shell.py: a simple shell script that runs a calclang REPL
- grammar.txt: description of the language's syntax

# Demo
To run the REPL, run `python shell.py` in a terminal. Requires python3.8 or above, but no additional dependencies needed.
REPL keywords are:
- \q - exit the REPL
- \h - help for the REPL

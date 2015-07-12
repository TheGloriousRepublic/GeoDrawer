import sys
import math
import operator

pyver = sys.version_info[0]
try:
    from pyparsing import *
except ImportError:
    print(pyver)
    if pyver == 2:
        import tkMessageBox
        tkMessageBox.showwarning('No Expressions', 'Pyparsing module not found! Expression parsing will not work! To install pyparsing, do "pip install pyparsing"in the command prompt')
    elif pyver == 3:
        import Tkinter.messagebox
        Tkinter.messagebox.showwarning('No Expressions', 'Pyparsing module not found! Expression parsing will not work! To install pyparsing, do"pip install pyparsing" in the command prompt')

# fourFn.py
#
# Demonstration of the pyparsing module, implementing a simple 4-function expression parser,
# with support for scientific notation, and symbols for e and pi.
# Extended to add exponentiation and simple built-in functions.
# Extended test cases, simplified pushFirst method.
#
# Copyright 2003-2006 by Paul McGuire
#

exprStack = []

if pyver == 3:
    def cmp(x, y):
        if x<y:
            return -1
        elif x == y:
            return 0
        elif x > y:
            return 1

class NumericStringParser(object):
    '''
    Most of this code comes from the fourFn.py pyparsing example

    '''
    def pushFirst(self, strg, loc, toks ):
        self.exprStack.append( toks[0] )
    def pushUMinus(self, strg, loc, toks ):
        if toks and toks[0]=='-': 
            self.exprStack.append( 'unary -' )
    def __init__(self):
        '''
        expop   :: '^'
        multop  :: '*' | '/'
        addop   :: '+' | '-'
        integer :: ['+' | '-'] '0'..'9'+
        atom    :: PI | E | real | fn '(' expr ')' | '(' expr ')'
        factor  :: atom [ expop factor ]*
        term    :: factor [ multop factor ]*
        expr    :: term [ addop term ]*
        '''
        point = Literal( '.' )
        e     = CaselessLiteral( 'E' )
        fnumber = Combine( Word( '+-'+nums, nums ) + 
                           Optional( point + Optional( Word( nums ) ) ) +
                           Optional( e + Word( '+-'+nums, nums ) ) )
        ident = Word(alphas, alphas+nums+'_$')       
        plus  = Literal( '+' )
        minus = Literal( '-' )
        mult  = Literal( '*' )
        div   = Literal( '/' )
        lpar  = Literal( '(' ).suppress()
        rpar  = Literal( ')' ).suppress()
        addop  = plus | minus
        multop = mult | div
        expop = Literal( '^' )
        pi    = CaselessLiteral( 'PI' )
        expr = Forward()
        atom = ((Optional(oneOf('- +')) +
                 (pi|e|fnumber|ident+lpar+expr+rpar).setParseAction(self.pushFirst))
                | Optional(oneOf('- +')) + Group(lpar+expr+rpar)
                ).setParseAction(self.pushUMinus)       
        # by defining exponentiation as 'atom [ ^ factor ]...' instead of 
        # 'atom [ ^ atom ]...', we get right-to-left exponents, instead of left-to-right
        # that is, 2^3^2 = 2^(3^2), not (2^3)^2.
        factor = Forward()
        factor << atom + ZeroOrMore( ( expop + factor ).setParseAction( self.pushFirst ) )
        term = factor + ZeroOrMore( ( multop + factor ).setParseAction( self.pushFirst ) )
        expr << term + ZeroOrMore( ( addop + term ).setParseAction( self.pushFirst ) )
        # addop_term = ( addop + term ).setParseAction( self.pushFirst )
        # general_term = term + ZeroOrMore( addop_term ) | OneOrMore( addop_term)
        # expr <<  general_term       
        self.bnf = expr
        # map operator symbols to corresponding arithmetic operations
        epsilon = 1e-12
        self.opn = {
                '+' : operator.add,
                '-' : operator.sub,
                '*' : operator.mul,
                '/' : operator.truediv,
                '^' : operator.pow
                     }
        self.fn  = {
                'ceil': math.ceil,
                'fact': math.factorial,
                'floor':math.floor,
                #'log' : math.log,
                'sin' : math.sin,
                'cos' : math.cos,
                'tan' : math.tan,
                'asin': math.asin,
                'acos': math.acos,
                'atan': math.atan,
                'abs' : abs,
                'trunc' : lambda a: int(a),
                'round' : round,
                'sgn' : lambda a: abs(a)>epsilon and cmp(a,0) or 0
                }
    def evaluateStack(self, s ):
        op = s.pop()
        if op == 'unary -':
            return -self.evaluateStack( s )
        if op in '+-*/^':
            op2 = self.evaluateStack( s )
            op1 = self.evaluateStack( s )
            return self.opn[op]( op1, op2 )
        elif op == 'PI':
            return math.pi # 3.1415926535
        elif op == 'E':
            return math.e  # 2.718281828
        elif op in self.fn:
            return self.fn[op]( self.evaluateStack( s ) )
        elif op[0].isalpha():
            return 0
        else:
            return float( op )
    def eval(self,num_string,parseAll=True):
        self.exprStack=[]
        results=self.bnf.parseString(num_string,parseAll)
        val=self.evaluateStack( self.exprStack[:] )
        return val

def evalexp(s):
    BNF = NumericStringParser()
    return BNF.eval( s )

if __name__ == '__main__':
    BNF = NumericStringParser()
    values = []
    def test( s, expVal ):
        global BNF
        result = BNF.eval( s )
        if result == expVal:
            print(s+'='+str(result)+'=>'+str(expVal))
            values.append(True)
        else:
            print(s+'!!!'+str(result)+'!='+str(expval))
            values.append(False)

    #test( 'log(8, 2)', 3 )
    test( '9', 9 )
    test( '-9', -9 )
    test( '--9', 9 )
    test( '-E', -math.e )
    test( '9 + 3 + 6', 9 + 3 + 6 )
    test( '9 + 3 / 11', 9 + 3.0 / 11 )
    test( '(9 + 3)', (9 + 3) )
    test( '(9+3) / 11', (9+3.0) / 11 )
    test( '9 - 12 - 6', 9 - 12 - 6 )
    test( '9 - (12 - 6)', 9 - (12 - 6) )
    test( '2*3.14159', 2*3.14159 )
    test( '3.1415926535*3.1415926535 / 10', 3.1415926535*3.1415926535 / 10 )
    test( 'PI * PI / 10', math.pi * math.pi / 10 )
    test( 'PI*PI/10', math.pi*math.pi/10 )
    test( 'PI^2', math.pi**2 )
    test( 'round(PI^2)', round(math.pi**2) )
    test( '6.02E23 * 8.048', 6.02E23 * 8.048 )
    test( 'e / 3', math.e / 3 )
    test( 'sin(PI/2)', math.sin(math.pi/2) )
    test( 'trunc(E)', int(math.e) )
    test( 'trunc(-E)', int(-math.e) )
    test( 'round(E)', round(math.e) )
    test( 'round(-E)', round(-math.e) )
    test( 'E^PI', math.e**math.pi )
    test( '2^3^2', 2**3**2 )
    test( '2^3+2', 2**3+2 )
    test( '2^9', 2**9 )
    test( 'sgn(-2)', -1 )
    test( 'sgn(0)', 0 )
    test( 'sgn(0.1)', 1 )

    print(all(values))


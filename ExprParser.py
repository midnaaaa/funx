# Generated from Expr.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\2\5\2\26\n\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3&\n")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3,\n\3\3\4\3\4\7\4\60\n\4\f\4\16")
        buf.write("\4\63\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\7\6D\n\6\f\6\16\6G\13\6\5\6I\n\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6T\n\6\f\6\16\6W\13")
        buf.write("\6\3\7\3\7\6\7[\n\7\r\7\16\7\\\3\7\3\7\3\7\2\3\n\b\2\4")
        buf.write("\6\b\n\f\2\5\3\2\7\f\3\2\20\22\3\2\23\24\2j\2\21\3\2\2")
        buf.write("\2\4+\3\2\2\2\6-\3\2\2\2\b\66\3\2\2\2\nH\3\2\2\2\fX\3")
        buf.write("\2\2\2\16\20\5\6\4\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17")
        buf.write("\3\2\2\2\21\22\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\24")
        buf.write("\26\5\4\3\2\25\24\3\2\2\2\25\26\3\2\2\2\26\27\3\2\2\2")
        buf.write("\27\30\7\2\2\3\30\3\3\2\2\2\31,\5\n\6\2\32\33\7\30\2\2")
        buf.write("\33\34\7\3\2\2\34,\5\b\5\2\35\36\7\30\2\2\36\37\7\3\2")
        buf.write("\2\37,\5\n\6\2 !\7\4\2\2!\"\5\b\5\2\"%\5\f\7\2#$\7\5\2")
        buf.write("\2$&\5\f\7\2%#\3\2\2\2%&\3\2\2\2&,\3\2\2\2\'(\7\6\2\2")
        buf.write("()\5\b\5\2)*\5\f\7\2*,\3\2\2\2+\31\3\2\2\2+\32\3\2\2\2")
        buf.write("+\35\3\2\2\2+ \3\2\2\2+\'\3\2\2\2,\5\3\2\2\2-\61\7\27")
        buf.write("\2\2.\60\7\30\2\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2")
        buf.write("\61\62\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\5\f\7")
        buf.write("\2\65\7\3\2\2\2\66\67\5\n\6\2\678\t\2\2\289\5\n\6\29\t")
        buf.write("\3\2\2\2:;\b\6\1\2;<\7\r\2\2<=\5\n\6\2=>\7\16\2\2>I\3")
        buf.write("\2\2\2?I\7\31\2\2@I\7\30\2\2AE\7\27\2\2BD\5\n\6\2CB\3")
        buf.write("\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2FI\3\2\2\2GE\3\2\2")
        buf.write("\2H:\3\2\2\2H?\3\2\2\2H@\3\2\2\2HA\3\2\2\2IU\3\2\2\2J")
        buf.write("K\f\b\2\2KL\7\17\2\2LT\5\n\6\bMN\f\7\2\2NO\t\3\2\2OT\5")
        buf.write("\n\6\bPQ\f\6\2\2QR\t\4\2\2RT\5\n\6\7SJ\3\2\2\2SM\3\2\2")
        buf.write("\2SP\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V\13\3\2\2\2")
        buf.write("WU\3\2\2\2XZ\7\25\2\2Y[\5\4\3\2ZY\3\2\2\2[\\\3\2\2\2\\")
        buf.write("Z\3\2\2\2\\]\3\2\2\2]^\3\2\2\2^_\7\26\2\2_\r\3\2\2\2\f")
        buf.write("\21\25%+\61EHSU\\")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "'if'", "'else'", "'while'", "'='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'('", "')'", 
                     "'^'", "'*'", "'/'", "'%'", "'+'", "'-'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "FUN", "ID", "NUM", "COM", "WS" ]

    RULE_root = 0
    RULE_stat = 1
    RULE_funcs = 2
    RULE_booleans = 3
    RULE_expr = 4
    RULE_bloc = 5

    ruleNames =  [ "root", "stat", "funcs", "booleans", "expr", "bloc" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    FUN=21
    ID=22
    NUM=23
    COM=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.FuncsContext)
            else:
                return self.getTypedRuleContext(ExprParser.FuncsContext,i)


        def stat(self):
            return self.getTypedRuleContext(ExprParser.StatContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 12
                    self.funcs() 
                self.state = 17
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__1) | (1 << ExprParser.T__3) | (1 << ExprParser.T__10) | (1 << ExprParser.FUN) | (1 << ExprParser.ID) | (1 << ExprParser.NUM))) != 0):
                self.state = 18
                self.stat()


            self.state = 21
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BucleContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleans(self):
            return self.getTypedRuleContext(ExprParser.BooleansContext,0)

        def bloc(self):
            return self.getTypedRuleContext(ExprParser.BlocContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBucle" ):
                return visitor.visitBucle(self)
            else:
                return visitor.visitChildren(self)


    class AssigContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def booleans(self):
            return self.getTypedRuleContext(ExprParser.BooleansContext,0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)


    class ExpresContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpres" ):
                return visitor.visitExpres(self)
            else:
                return visitor.visitChildren(self)


    class IfelseContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleans(self):
            return self.getTypedRuleContext(ExprParser.BooleansContext,0)

        def bloc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BlocContext)
            else:
                return self.getTypedRuleContext(ExprParser.BlocContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse" ):
                return visitor.visitIfelse(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = ExprParser.ExpresContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.AssigContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(ExprParser.ID)
                self.state = 25
                self.match(ExprParser.T__0)
                self.state = 26
                self.booleans()
                pass

            elif la_ == 3:
                localctx = ExprParser.AssigContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(ExprParser.ID)
                self.state = 28
                self.match(ExprParser.T__0)
                self.state = 29
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = ExprParser.IfelseContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.match(ExprParser.T__1)
                self.state = 31
                self.booleans()
                self.state = 32
                self.bloc()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ExprParser.T__2:
                    self.state = 33
                    self.match(ExprParser.T__2)
                    self.state = 34
                    self.bloc()


                pass

            elif la_ == 5:
                localctx = ExprParser.BucleContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.match(ExprParser.T__3)
                self.state = 38
                self.booleans()
                self.state = 39
                self.bloc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_funcs

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DecfuncContext(FuncsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.FuncsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUN(self):
            return self.getToken(ExprParser.FUN, 0)
        def bloc(self):
            return self.getTypedRuleContext(ExprParser.BlocContext,0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecfunc" ):
                return visitor.visitDecfunc(self)
            else:
                return visitor.visitChildren(self)



    def funcs(self):

        localctx = ExprParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            localctx = ExprParser.DecfuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ExprParser.FUN)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExprParser.ID:
                self.state = 44
                self.match(ExprParser.ID)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.bloc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BooleansContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_booleans

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleans" ):
                return visitor.visitBooleans(self)
            else:
                return visitor.visitChildren(self)




    def booleans(self):

        localctx = ExprParser.BooleansContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_booleans)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.expr(0)
            self.state = 53
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__4) | (1 << ExprParser.T__5) | (1 << ExprParser.T__6) | (1 << ExprParser.T__7) | (1 << ExprParser.T__8) | (1 << ExprParser.T__9))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 54
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar" ):
                return visitor.visitPar(self)
            else:
                return visitor.visitChildren(self)


    class ValContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal" ):
                return visitor.visitVal(self)
            else:
                return visitor.visitChildren(self)


    class FuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUN(self):
            return self.getToken(ExprParser.FUN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)


    class BinContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBin" ):
                return visitor.visitBin(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.T__10]:
                localctx = ExprParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 57
                self.match(ExprParser.T__10)
                self.state = 58
                self.expr(0)
                self.state = 59
                self.match(ExprParser.T__11)
                pass
            elif token in [ExprParser.NUM]:
                localctx = ExprParser.ValContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(ExprParser.NUM)
                pass
            elif token in [ExprParser.ID]:
                localctx = ExprParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.match(ExprParser.ID)
                pass
            elif token in [ExprParser.FUN]:
                localctx = ExprParser.FuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(ExprParser.FUN)
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 64
                        self.expr(0) 
                    self.state = 69
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 81
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.BinContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 73
                        self.match(ExprParser.T__12)
                        self.state = 74
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.BinContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 76
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__13) | (1 << ExprParser.T__14) | (1 << ExprParser.T__15))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.BinContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 79
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.T__16 or _la==ExprParser.T__17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        self.expr(5)
                        pass

             
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BlocContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_bloc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloc" ):
                return visitor.visitBloc(self)
            else:
                return visitor.visitChildren(self)




    def bloc(self):

        localctx = ExprParser.BlocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bloc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(ExprParser.T__18)
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 87
                self.stat()
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__1) | (1 << ExprParser.T__3) | (1 << ExprParser.T__10) | (1 << ExprParser.FUN) | (1 << ExprParser.ID) | (1 << ExprParser.NUM))) != 0)):
                    break

            self.state = 92
            self.match(ExprParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         





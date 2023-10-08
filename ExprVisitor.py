# Generated from Expr.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expres.
    def visitExpres(self, ctx:ExprParser.ExpresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assig.
    def visitAssig(self, ctx:ExprParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifelse.
    def visitIfelse(self, ctx:ExprParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bucle.
    def visitBucle(self, ctx:ExprParser.BucleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#decfunc.
    def visitDecfunc(self, ctx:ExprParser.DecfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#booleans.
    def visitBooleans(self, ctx:ExprParser.BooleansContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#par.
    def visitPar(self, ctx:ExprParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#val.
    def visitVal(self, ctx:ExprParser.ValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#func.
    def visitFunc(self, ctx:ExprParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bin.
    def visitBin(self, ctx:ExprParser.BinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, ctx:ExprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloc.
    def visitBloc(self, ctx:ExprParser.BlocContext):
        return self.visitChildren(ctx)



del ExprParser
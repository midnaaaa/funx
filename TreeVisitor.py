if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

class TreeVisitor(ExprVisitor):
    def __init__(self):
        self.nivell = 0

    def visitBin(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + l[1].getText())
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1


    def visitVal(self, ctx):
        l = list(ctx.getChildren())
        print("  " * self.nivell + l[0].getText() )
        
    
    def visitPar(self, ctx):
        l = list(ctx.getChildren())
        print("  " * self.nivell + l[0].getText())
        self.nivell += 1
        self.visit(l[1])
        self.nivell -= 1
        print("  " * self.nivell + l[2].getText())


if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

d = {'+' : lambda x, y: x + y, '-' : lambda x, y: x - y, '*' : lambda x, y: x * y, '/' : lambda x, y: x // y, '%' : lambda x, y: x % y, '^' : lambda x, y: x ** y}
dB = {'=' : lambda x, y: x == y, '!=' : lambda x, y: x != y, '<' : lambda x, y: x < y, '>' : lambda x, y: x > y, '<=' : lambda x, y: x <= y, '>=' : lambda x, y: x >= y}

class EvalVisitor(ExprVisitor):


    def __init__(self, ts, tf):
        self.ts = ts
        self.tf = tf

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0])


    def visitPar(self,ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1])


    def visitVal(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())


    def visitBin(self, ctx):
        l = list(ctx.getChildren())
        operador = l[1].getText()
        operandD = self.visit(l[2])
        operandE = self.visit(l[0])
        if operador == '/' and operandD == 0:
            raise Exception(f"Division by 0")
        else:
            return (d[operador])(operandE, operandD)

    def visitId(self, ctx):
        l = list(ctx.getChildren())
        taulaSimbols = self.ts.pop()
        self.ts.append(taulaSimbols)
        if l[0].getText() not in taulaSimbols:
            return 0
        return int(taulaSimbols[l[0].getText()])

    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        exp = self.visit(l[2])
        taulaSimbols = self.ts.pop()
        taulaSimbols[l[0].getText()] = exp
        self.ts.append(taulaSimbols)
        return None


    def visitBooleans(self,ctx):
        l = list(ctx.getChildren())
        operador = l[1].getText()
        bools = (dB[operador])(int(self.visit(l[0])), int(self.visit(l[2])))
        if bools: return 1
        return 0


    def visitBloc(self,ctx):
        l = list(ctx.getChildren())
        for x in l:
            if(x.getText() != '{' and x.getText() != '}'):
                stat = self.visit(x)
                if(stat != None):
                    return stat


    def visitIfelse(self, ctx):
        l = list(ctx.getChildren())
        condition = self.visit(l[1])
        if condition == 1:
            return self.visit(l[2])
        else:
            if(len(l) > 4):
                return self.visit(l[4])


    def visitBucle(self, ctx):
        l = list(ctx.getChildren())
        while(self.visit(l[1])):
            stat = self.visit(l[2])
            if(stat != None): return stat

    def visitDecfunc(self, ctx):
        l = list(ctx.getChildren())
        name = l[0].getText()
        if name in self.tf:
            raise Exception(f"Function is already declared")
        params = []
        if len(l) > 2:
            params = [x.getText() for x in l[1:-1]]
        if(len(set(params)) != len(params)): raise Exception(f"Duplicate parameters in function declaration")
        self.tf[name] = {"params": params, "content": l[-1]}
        return None


    def visitFunc(self, ctx):
        l = list(ctx.getChildren())
        name = l[0].getText()
        if name not in self.tf:
            raise Exception(f"Function '{name}' is not defined")
        func_def = self.tf[name]
        params = func_def["params"]
        if len(params) != len(l[1:]):
            raise Exception(f"Incorrect number of arguments for function '{name}'")

        symbol_table = {}
        for i, param in enumerate(params):
            symbol_table[param] = self.visit(l[i+1])

        self.ts.append(symbol_table)
        result = self.visit(func_def["content"])
        self.ts.pop()
        return result






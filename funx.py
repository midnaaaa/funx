from flask import Flask, render_template, request
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor

app = Flask(__name__)

# Lista de funciones declaradas
tf = {}
ts = [{}]
history = []

@app.route('/')
def index():
    history_slice = history[-5:]
    return render_template('base.html', tfs=tf, history=history_slice)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    # Obtener la expresión del formulario
    try:
        expression = request.form['expression']
        input_stream = InputStream(expression)
        lexer = ExprLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)
        tree = parser.root()
        visitor = EvalVisitor(ts, tf)
        result = visitor.visit(tree)
        history.append((expression, result))

        # Renderizar la plantilla con el resultado de la evaluación
        history_slice = history[-5:]
        history_slice.reverse()
        return render_template('base.html', input=expression, result=result, tfs=tf, history=history_slice)
    except Exception as e:
        return render_template('base.html', error=str(e), input=expression, tfs=tf)

if __name__ == '__main__':
    app.run()

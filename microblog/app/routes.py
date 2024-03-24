from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Guilherme"
    dados = {"profissao": "Estudante", "canal": "Guilherme B. Costa"}
    return render_template('index.html', nome = nome, dados = dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

    # return '''
    # <html>
    #     <head><title>Página Inicial</title></head>
    #     <body>
    #         <h2>Hello '''+nome+'''</h2>
    #     </body>
    # </html>
    
    # '''
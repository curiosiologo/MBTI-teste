from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nome = request.form['nome']
    idade = request.form['idade']
    genero = request.form['genero']

    extroversao_introversao = request.form['extroversao_introversao']
    sensacao_intuicao = request.form['sensacao_intuicao']
    pensamento_sentimento = request.form['pensamento_sentimento']
    julgamento_percepcao = request.form['julgamento_percepcao']

    mbti = extroversao_introversao + sensacao_intuicao + pensamento_sentimento + julgamento_percepcao

    return f"""
    <h1>Resultado do MBTI</h1>
    <p>Nome: {nome}</p>
    <p>Idade: {idade}</p>
    <p>Gênero: {genero}</p>
    <p>Seu tipo MBTI é: {mbti}</p>
    """

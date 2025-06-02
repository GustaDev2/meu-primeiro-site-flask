# Importa a classe Flask do módulo flask, e datetime para datas
from flask import Flask, render_template, request, redirect, url_for
import datetime

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Rota para a página inicial (URL: /)
@app.route('/')
def home():
    nome_usuario = "Visitante"
    data_atual = datetime.date.today().strftime("%d/%m/%Y")
    logado = True # Mude para False para testar a outra condição
    return render_template('home.html', usuario=nome_usuario, hoje=data_atual, logado=logado)

# Rota para a página "Sobre" (URL: /sobre)
@app.route('/sobre')
def sobre():
    equipe = [
        {"nome": "Alice", "cargo": "Desenvolvedora Frontend"},
        {"nome": "Bob", "cargo": "Desenvolvedor Backend"},
        {"nome": "Charlie", "cargo": "Designer UX/UI"}
    ]
    return render_template('sobre.html', membros_da_equipe=equipe)

# Rota para a página de contato (URL: /contato)
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        print(f"Dados do Contato Recebidos:")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"Mensagem: {mensagem}")

        return render_template('contato.html', mensagem_sucesso="Sua mensagem foi enviada com sucesso! Logo entraremos em contato.")
    else:
        return render_template('contato.html')

# Rota para a página "Serviços" (URL: /servicos)
# ESTA É A ROTA QUE PRECISAMOS TER CERTEZA QUE ESTÁ PERFEITA
@app.route('/servicos')
def servicos():
    lista_de_servicos = [
        {"nome": "Desenvolvimento de Sites", "descricao": "Criamos sites modernos e responsivos.", "preco": 1500.00},
        {"nome": "Manutenção de Sistemas", "descricao": "Suporte e atualização para seus sistemas.", "preco": 500.00},
        {"nome": "Consultoria em TI", "descricao": "Orientação especializada para seus projetos.", "preco": 300.50},
        {"nome": "Hospedagem Web", "descricao": "Hospedagem segura e rápida para seu site."}
    ]
    return render_template('servicos.html', servicos=lista_de_servicos)

# Ponto de entrada para a execução do aplicativo Flask
if __name__ == "__main__":
    app.run(debug=True)
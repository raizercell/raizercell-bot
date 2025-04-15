from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Leonardo bot da RaizerCell está online!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data or 'message' not in data:
        return jsonify({'error': 'Mensagem inválida'}), 400

    msg = data['message'].lower()
    if "redmi 14c" in msg:
        resposta = "O Redmi 14C é um modelo de entrada da Xiaomi. Serve bem para tarefas do dia a dia e jogos leves!"
    elif "tem celular" in msg or "comprar" in msg:
        resposta = "Temos várias opções de celulares! Me diz o que você procura que eu te ajudo!"
    else:
        resposta = "Oi! Sou o Leonardo, posso te ajudar com informações sobre celulares. Manda sua dúvida!"

    return jsonify({"response": resposta})

if __name__ == '__main__':
    app.run()
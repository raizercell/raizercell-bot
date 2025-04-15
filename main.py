from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("message", "").lower()

    if "redmi" in message:
        return jsonify({"reply": "O Redmi 14C é ótimo para jogos leves! E sim, temos ele aqui na RaizerCell!"})
    elif "horário" in message or "funciona" in message:
        return jsonify({"reply": "Funcionamos de segunda a sexta das 9h às 18h e aos sábados das 9h às 14h!"})
    elif "pagamento" in message or "pagar" in message:
        return jsonify({"reply": "Aceitamos PIX, cartão em até 10x sem juros, boleto e PayJoy (com entrada + parcelas quinzenais)."})
    else:
        return jsonify({"reply": "Oi! Aqui é o Leonardo da RaizerCell. Me fala o que você procura que eu te ajudo!"})

@app.route("/", methods=["GET"])
def home():
    return "Leonardo bot da RaizerCell está online!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

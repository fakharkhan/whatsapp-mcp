from flask import Flask, request, jsonify
from whatsapp import send_message

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    recipient = data.get('recipient')
    message = data.get('message')

    if not recipient or not message:
        return jsonify({'success': False, 'message': 'Missing recipient or message'}), 400

    result = send_message(recipient, message)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=8080)
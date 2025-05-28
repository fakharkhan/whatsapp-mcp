from flask import Flask, request, jsonify
from whatsapp import send_message
from whatsapp import list_contacts
from whatsapp import get_contact_chats

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

@app.route('/contacts', methods=['GET'])
def contacts():
    contacts = list_contacts()
    # Convert dataclass objects to dicts for JSON serialization
    contacts_dicts = [c.__dict__ for c in contacts]
    return jsonify({'success': True, 'contacts': contacts_dicts})

@app.route('/contact_chats', methods=['GET'])
def contact_chats():
    jid = request.args.get('jid')
    if not jid:
        return jsonify({'success': False, 'message': 'Missing jid'}), 400
    chats = get_contact_chats(jid)
    chats_dicts = [c.__dict__ for c in chats]
    return jsonify({'success': True, 'chats': chats_dicts})

if __name__ == '__main__':
    app.run(port=8080)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    amount = data.get('amount')
    rate = data.get('rate')

    if amount is None or rate is None:
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        amount = int(amount)
        rate = float(rate)
    except ValueError:
        return jsonify({'error': 'Invalid input data'}), 400

    converted_amount = amount * rate
    return jsonify({'converted_amount': converted_amount})

if __name__ == '__main__':
    app.run(debug=True)

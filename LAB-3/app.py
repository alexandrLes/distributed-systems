from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

word_list = [
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('search')
    results = [word for word in word_list if word.startswith(search)]
    return jsonify(matching_results=results)

if __name__ == '__main__':
    app.run(debug=True)

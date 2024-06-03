import os
from flask import jsonify, request, Flask, render_template

from services import Query_matching

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/uiCore.html')


@app.route('/queryMatch', methods=['POST'])
def textProcess():
    data = request.get_json()
    if not data or 'text' not in data or 'dataset' not in data:
        return jsonify({'error': 'No text provided'}), 400

    try:
        queryMatch = Query_matching.query_matching(data['text'],data['dataset'])
        print('1111111111110')
        print(queryMatch)
        return jsonify(queryMatch)
    except Exception as e:
        app.logger.error(f'Error matching Query: {e}')
        return jsonify({'error': 'An error occurred while Matching Query'}), 500


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 8015))
    app.run(port=PORT)

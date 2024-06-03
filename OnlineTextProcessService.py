import os
from flask import jsonify, request, Flask, render_template
from services.TextProccesing import TextProcessingService

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/uiCore.html')

@app.route('/TextProcess', methods=['POST'])
def textProcess():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    print(data['text'])
    try:
        text_processing_service = TextProcessingService()
        processed_text = text_processing_service.process(data['text'])
        return jsonify({'TextProcess': processed_text})
    except Exception as e:
        app.logger.error(f'Error processing text: {e}')
        return jsonify({'error': 'An error occurred while processing the text'}), 500

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 8011))
    app.run(port=PORT)
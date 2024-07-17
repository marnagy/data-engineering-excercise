# pip
from flask import Flask, send_file, request
import numpy as np

# custom
from custom_lib import load_phrases, load_vectors, load_normalized_phrases
from any_input import get_closest_phrases

# standard lib
import logging
logger = logging.getLogger(__name__)
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

flask_app = Flask("Closest phrase")

phrases = load_phrases()
word_to_index, master_arr = load_vectors()
normalized_phrases = load_normalized_phrases()

@flask_app.get('/')
def index():
    return send_file('index.html')

@flask_app.get('/test')
def test():
    return {"message": "This is a test endpoint."}

@flask_app.post('/api')
def get_closest_phrase():
    logger.info("Received a request on API")
    form = request.form
    user_input = form["user_input"]
    logger.info(form)
    if len(user_input) == 0:
        return "Invalid input: Empty string is not a valid phrase."

    distances = get_closest_phrases(
        user_input,
        phrases=phrases,
        normalized_phrases=normalized_phrases,
        word_to_index=word_to_index,
        master_arr=master_arr,
    )
    closest_phrase = ' '.join(phrases[np.argmin(distances)])
    logger.info(f"Found phrase: {closest_phrase}")
    return {
        "closest_phrase": closest_phrase,
        "distance": min(distances)
    }

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8000, debug=True)
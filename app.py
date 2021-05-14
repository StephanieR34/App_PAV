from flask import Flask
from flask_cors import CORS
import logging
import os
from .functions import user_account



template_dir = os.path.abspath('./templates')
app = Flask(__name__, template_folder=template_dir)

app.add_url_rule('/hello', view_func=user_account.hello)
CORS(app)
user_account.hello()


if __name__ == '__main__':
    logging.basicConfig(filename="prog.log", level=logging.DEBUG)
    app.run(host='0.0.0.0',port=5000, debug=True, use_reloader=True)
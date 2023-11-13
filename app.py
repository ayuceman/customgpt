# app.py

import os
import sys
import constants
from flask import Flask, render_template, request,render_template_string
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

os.environ["OPENAI_API_KEY"] = constants.APIKEY

app = Flask(__name__)

storage_context = StorageContext.from_defaults(persist_dir="storage")
index = load_index_from_storage(storage_context, index_id="vector_index")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query ='write in html table, sku, name and image of all the products or documents best matching or having word like: '+ request.form['query']
        query_engine = index.as_query_engine(response_mode="tree_summarize")
        response = query_engine.query(query)
        return render_template('index.html', message=response, query= query)
    # return render_template_string('index.html')

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000, debug=True)


hostedApp = Flask(__name__)
hostedApp.wsgi_app = DispatcherMiddleware(NotFound(),{"/myapp":app})

hostedApp.run(host="0.0.0.0",port=5000,debug=True)

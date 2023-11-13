import os
import sys
import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY

from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage


query = sys.argv[1]
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
index.set_index_id("vector_index")
index.storage_context.persist("./storage")
storage_context = StorageContext.from_defaults(persist_dir="storage")
# load index
index = load_index_from_storage(storage_context, index_id="vector_index")

query_engine = index.as_query_engine(response_mode="tree_summarize")
response = query_engine.query(query)

print('Content-Type: text/plain')
print('')
print(response)
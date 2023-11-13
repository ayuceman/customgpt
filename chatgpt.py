import os
import sys
import openai # Import the openai module
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

# Import the constants module, assuming it's in the same directory
import constants

# Set the API key using constants.APIKEY
os.environ["OPENAI_API_KEY"] = constants.APIKEY

if len(sys.argv) < 2:
    print("Please provide a query as a command line argument.")
    sys.exit(1)

query = sys.argv[1]

# Read the text from 'data.txt' using Python's built-in file handling
# Check if the file and the folder exist
data_folder = 'data'
data_file = 'data.txt'
data_path = os.path.join(data_folder, data_file)
if not os.path.exists(data_folder):
    print(f"The folder '{data_folder}' does not exist.")
    sys.exit(1)
if not os.path.exists(data_path):
    print(f"The file '{data_file}' does not exist in the folder '{data_folder}'.")
    sys.exit(1)

# Read the file content
with open(data_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Create a TextLoader and load the text
# Specify the language of the text
loader = TextLoader(text)

# Create an index from the loaded text
index = VectorstoreIndexCreator().from_loaders([loader])

# Query the index and print the results
response = index.query(query)
print(response)

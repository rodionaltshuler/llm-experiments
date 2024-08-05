import ollama

response = ollama.generate(model='llama3.1:8b',
prompt='Compare python and rust programming languages')
print(response['response'])

#I have the following script handling the response from the LLM, 
#response expected to contain creation of multiple files with some content. 
#I need a prompt example from you that will generate response this script will create files with.

# Format the response as a list of strings, where each string represents a file to be created with its name and 
# contents separated by ': '. For example:
# 'Create file: filename.txt : This is a README file.'"

class DR_TS_Agent():
    def __init__(self):
        super().__init__()

    def handle(self, response):
        # Parse the response to extract file creation information
        files_to_create = []
        for line in response.split('\n'):
            if 'Create file' in line:
                lines = line.split(': ')
                file_info = {}
                if len(lines) == 3:
                    file_info['file_name'] = lines[1]
                    file_info['content'] = '\n'.join(lines[2:])
                    files_to_create.append(file_info)

        # Create the files
        for file_info in files_to_create:
            with open(file_info['file_name'], 'w') as f:
                f.write(file_info['content'])

agent = DR_TS_Agent()
with open("./src/create_files_prompt.txt") as input:
  data = input.read()
agent.handle(data)
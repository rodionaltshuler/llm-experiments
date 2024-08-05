import langchain
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
import os

class ProjectFile(BaseModel):
    filename: str = Field(description="Relative path to the file, with the filename as last segment")
    contents: str = Field(description="File contents, for example executable file, configuration file")

parser = JsonOutputParser(pydantic_object=ProjectFile)

prompt = PromptTemplate(
    template="Create software solution which can be run and fulfill the requirements.\n{requirements}\n. Format instruction for your respone is the following: \n{format_instructions}",
    input_variables=["requirements"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

api_key = os.environ.get('OPENAI_API_KEY')
model = ChatOpenAI(temperature=0,
                   openai_api_key=api_key)


with open("./DR_Requirements/requirements.txt") as input:
  data = input.read()

format_instructions =  parser.get_format_instructions()
requirements = data
print(f"Create software solution which can be run and fulfill the requirements.\n Format instruction for your respone is the following:\n{format_instructions}\n Solution requirements: \n{requirements}\n\n\n\n\n")

chain = prompt | model | parser

output = chain.invoke({"requirements": data})

print(output)
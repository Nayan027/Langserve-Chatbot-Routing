from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_perplexity import ChatPerplexity
from langserve import add_routes
from langchain_community.llms import Ollama

from fastapi import FastAPI
import uvicorn as uv

import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")          # Best practice


app = FastAPI(title="LangChain Server")

# Base route: Providing with basic info.
add_routes(app, ChatPerplexity(), path="/perplexity")


# Defining Prompts and Models so that different routings hit different api.
prompt1 = ChatPromptTemplate.from_template("Write a summary on this {subject} in 300 words")
model1 = Ollama(model="tinyllama")


prompt2 = ChatPromptTemplate.from_template("point 5 characteristics on {subject} in 150 words")
model2 = ChatPerplexity(model="sonar") 

# Common for both chains
parser = StrOutputParser()



# Routing using langserve for different llms that work in a flow.
add_routes(app,  prompt1|model1|parser,  path="/summary")

add_routes(app, prompt2|model2|parser,  path="/highlights")


# Run app
if __name__=="__main__":
    uv.run(app=app, host="localhost", port=8000)
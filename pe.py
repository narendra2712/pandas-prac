'''import warnings
warnings.filterwarnings("ignore")
from getpass import getpass
from langchain import HuggingFaceHub
import os
os.environ["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"] = getpass()
#place your huggingface API key after running this cell
#Import an LLM model from LangChain.
repo_id1 = "google/flan-t5-xxl"
llm = HuggingFaceHub(repo_id=repo_id1, model_kwargs={"temperature":0.3, "max_length":264})
prompt = "What is a constellation"
print(llm(prompt))'''

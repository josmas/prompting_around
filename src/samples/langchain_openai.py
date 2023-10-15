#%%
import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from aimstack.langchain_debugger.callback_handlers import GenericCallbackHandler

#%%
# Make sure you have copied sample.env into .env and added your API key to that file.
load_dotenv()

#%%
prompt = ChatPromptTemplate.from_template("tell me a joke about {foo}")

#%%
aim_cb = GenericCallbackHandler()
model = ChatOpenAI(callbacks=[aim_cb])
chain = prompt | model

#%%
response = chain.invoke({"foo": "beavers"})
aim_cb.flush()

print(response)

# %%
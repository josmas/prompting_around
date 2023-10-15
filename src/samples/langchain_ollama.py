#%%
import os
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOllama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from local_generic_callback_handler import LocalGenericCallbackHandler 

#%%
prompt = ChatPromptTemplate.from_template("tell me a joke about {foo}")

#%%
aim_cb = LocalGenericCallbackHandler()
callback_manager = CallbackManager([aim_cb, StreamingStdOutCallbackHandler()])

#%%
model = ChatOllama(model="mistral",
               temperature=0.9,
               verbose=True,
               callback_manager=callback_manager,
               callbacks=[aim_cb])
chain = prompt | model

#%%
response = chain.invoke({"foo": "beavers"})
aim_cb.flush()

# %%

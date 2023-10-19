from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOllama

# TODO : I also need a decorator to send the data to the DB
def generate_text(model: str, temperature: float, prompt_input: str):
    prompt = ChatPromptTemplate.from_template("tell me a joke about {prompt_input}")

    model = ChatOllama(model=model,
               temperature=temperature,
               verbose=False,)
    chain = prompt | model

    response = chain.invoke({"prompt_input": prompt_input})

    return response

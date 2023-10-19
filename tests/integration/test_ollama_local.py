from promptingaround.ollama_local import generate_text
from langchain.schema import AIMessage

def test_generate_text():
    model = "mistral"
    temperature = 0.5
    prompt_input = "beavers"
    response = generate_text(model, temperature, prompt_input)
    assert isinstance(response, AIMessage)
    assert len(response.content) > 0

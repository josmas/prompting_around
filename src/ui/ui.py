from gradio.components import Textbox
import gradio as gr

# the User import is no yet used, but it is an example of a relative import
from ..db.models import User

from .ollama_local import generate_text

def generate_from_ui(prompt):
    ai_message, _ = generate_text(model="mistral", temperature=0.5, prompt_input=prompt)
    return ai_message.content

# Define the Gradio interface
input_text = Textbox(label="Enter a prompt")
output_text = Textbox(label="Generated text")
interface = gr.Interface(fn=generate_from_ui, inputs=input_text, outputs=output_text, title="LLM Text Generation")

# Launch the interface
interface.launch()
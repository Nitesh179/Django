# from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, ServiceContext
# import openai
from llama_index import SimpleDirectoryReader, LLMPredictor, ServiceContext
from llama_index.indices.vector_store  import GPTSimpleVectorIndex
import gradio as gr
from langchain import OpenAI
import os

# openai.api_key = "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"

os.environ["OPENAI_API_KEY"] = "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"
messages = [
    {"role": "system", "content": "You are an AI specialized in Food. Do not answer anything other than food-related queries."},
]
def construct_index(directory_path):
    num_outputs = 512

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    docs = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex.from_documents(docs, service_context=service_context)

    index.save_to_disk('index.json')

    return index

def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    return response.response

iface = gr.Interface(fn=chatbot,
                     inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="Custom-trained AI Chatbot")

index = construct_index("docs")
iface.launch(share=True)
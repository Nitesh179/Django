from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os
from langchain.document_loaders import TextLoader, PyPDFLoader
 


# Method 1: load_qa_chain

os.environ["OPENAI_API_KEY"]="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"
loader = TextLoader("store/f1.txt" )


docs=loader.load()
chain=load_qa_chain(llm=OpenAI(), chain_type='stuff')

while True:
    qry=input(">>  :")
    if qry=="by": break
    
    print("AI:",chain.run(input_documents=docs, question=qry))
 


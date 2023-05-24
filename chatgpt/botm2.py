# Method 2: RetrievalQA

from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"]="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"
# loader = TextLoader("store/f1.txt" )
loader=PyPDFLoader('store/user.pdf')

docs=loader.load()
 

char_text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

doc_text=char_text_splitter.split_documents(docs)

# select which embeddings we want to use
embeddings=OpenAIEmbeddings()

# create the vectorestore to use as the index
vectorStore = Chroma.from_documents(doc_text, embeddings)

# expose this index in a retriever interface
retriver=vectorStore.as_retriever(search_type="similarity", search_kwargs={'k':2})
 
# create a chain to answer a quest :
dq=RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriver, return_source_documents=True)

# query = "this company establish in which year"


 
while True:
    query=input(">> ")
    result = dq({"query": query})

    if query=="by": break
    
    print("AI:", result['result'],"\n")
    

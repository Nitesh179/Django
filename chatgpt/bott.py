from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA, VectorDBQAWithSourcesChain
from langchain.document_loaders import DirectoryLoader
import magic
import os
import nltk 
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA, RetrievalQAWithSourcesChain
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"]="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"

# access data file :
# nltk.download()
loader = TextLoader("store/f1.txt" )
# loader= DirectoryLoader('store', glob='**/*.txt')
 
docs=loader.load()
chain=load_qa_chain(llm=OpenAI(), chain_type='stuff')

while True:
    qry=input(">>  :")
    if qry=="by": break
    
    print("AI:",chain.run(input_documents=docs, question=qry))
    




















 
# char_text_splitter=CharacterTextSplitter(chunk_size=100, chunk_overlap=0)

# doc_text=char_text_splitter.split_documents(docs)
 
'''
embeddings = HuggingFaceEmbeddings()

vStore=FAISS.from_documents(doc_text, embeddings)

question="what is the oldname of indore"
# model.run(question)

doc_ans = vStore.similarity_search(question)
 
# print(docs[0].page_content)
# print(doc_text)

vStore.save_local("faiss_index")
new_db = FAISS.load_local("faiss_index", embeddings)
docs = new_db.similarity_search(question)
print(docs)
'''

# openAI_embeddings=OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])
# vStore = Chroma.from_texts(doc_text, openAI_embeddings)

# model=RetrievalQA.from_chain_type(llm=OpenAI( openai_api_key=os.environ['OPENAI_API_KEY'],model_name="text-davinci-003", temperature=0,max_tokens=100), chain_type="stuff", retriever=vStore.as_retriever())
# # model=VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorestore=vStore, return_source_documents=True)

# question="what is the oldname of indore"
# model.run(question)



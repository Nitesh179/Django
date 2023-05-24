import os
import streamlit as st
from PyPDF2 import PdfReader 
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.vectorstores import FAISS
from langchain.vectorstores import Chroma

def main():
    
    os.environ["OPENAI_API_KEY"]="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"

    # Header design :
    
    st.header("BrainPDF 💬")

    # file upload :
    pdf=st.file_uploader("Upload Your Pdf", type="pdf")

    #  read pdf :
    if pdf is not None:
        read_pdf=PdfReader(pdf)
        doc_text=""
        for page in read_pdf.pages:
            doc_text += page.extract_text()
  
        # split into chunks :
        text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
        chunks = text_splitter.split_text(doc_text)
         

        # create embedding :
        embeddings = OpenAIEmbeddings()
        vectorStore = Chroma.from_texts(chunks, embeddings)

        #  show user input :
        quest= st.text_input("Ask a Question about your pdf:")

        if quest:
            # breakpoint()
            # doc=vectorStore.as_retriever(search_type="similarity", search_kwargs={'k':2})
            doc=vectorStore.similarity_search(quest)

            chain=load_qa_chain(llm=OpenAI(), chain_type="stuff")
        
            with get_openai_callback() as cb:
                response=chain.run(input_documents=doc, question=quest)
                print("=> ",cb  )

            st.write(response)
            
     



if __name__ == '__main__':
    main()





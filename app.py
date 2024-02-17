import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def getResponse(input_text, words, style):
    #Download LLAMA Model from here and store in the same folder: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
    llm = CTransformers(model='llama-2-7b-chat.ggmlv3.q8_0.bin', model_type='llama', config={'max_new_tokens': 256, 'temperature': 0.01})

    temp = """
            Write a blog for {style} job profile for a topic {input_text} within {words} words
    """

    prompt = PromptTemplate(input_variables=["style, input_text, words"], template=temp)
    response = llm(prompt.format(style=style, input_text=input_text, words=words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs", layout="centered", initial_sidebar_state="collapsed")

st.header("Generate Blogs")

input_text = st.text_input("Enter the Blog Topic")
co1, co2 = st.columns([5,5])
with co1:
    words = st.text_input('No of Words')
with co2:
    style = st.selectbox("Writing the blog for", ('Researchers', 'Data Scientists', 'Common People', 'A 5 Year old'), index=0)


submit = st.button("Generate")

if submit:
    st.write(getResponse(input_text, words, style))


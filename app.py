# from langchain.llms import OpenAI
# from dotenv import load_dotenv

# load_dotenv()  # load env from .env
# import streamlit as st
# import os

# # Function to load OpenAI model and get response
# def get_openai_response(question):
#     llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo-1106", temperature=0.6)
#     response = llm(question)
#     return response


# # Streamlit app function
# def main():
#     st.set_page_config(page_title="Q&A Demo")
#     st.header("Langchain Application")

#     input_text = st.text_input("Input:", key="input")

#     if st.button("Ask the question"):
#         st.subheader("The response is")
        
#         # Call the function and handle API response
#         response = get_openai_response(input_text)
#         if response:
#             st.write(response)
#         else:
#             st.write("Waiting for response...")

# # Run the app
# if __name__ == "__main__":
#     main()

from openai import OpenAI

from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()  # load env from .env

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# Function to load OpenAI model and get response
def get_openai_response(question):
    
    # print(openai.api_key)
    response = client.chat.completions.create(
        messages=[
        {'role': 'system', 'content': 'You answer questions about what user asks'},
        {'role': 'user', 'content': question},
        ],
        model="gpt-3.5-turbo",      
        temperature=0.6, 
    )
    return (response.choices[0].message.content)

# Streamlit app function
def main():
    st.set_page_config(page_title="Q&A Demo")
    st.header("Langchain Application")

    input_text = st.text_input("Input:", key="input")

    if st.button("Ask the question"):
        st.subheader("The response is")
        
        # Call the function and handle API response
        response = get_openai_response(input_text)
        if response:
            st.write(response)
        else:
            st.write("Waiting for response...")

# Run the app
if __name__ == "__main__":
    main()

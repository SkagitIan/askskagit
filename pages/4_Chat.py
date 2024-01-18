import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

def ask_openai(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4.0-turbo",  # or another model you prefer
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return str(e)

def main():
    st.title('OpenAI Chatbot')

    user_input = st.text_input("Ask a question:")

    if user_input:
        answer = ask_openai(user_input)
        st.text("Answer: ")
        st.write(answer)


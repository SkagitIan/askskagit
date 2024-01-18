import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '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'

def ask_openai(question):
    try:
        response = openai.completions.create(
            model="text-davinci-003",  # or another model you prefer
            prompt=question,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

def main():
    st.title('OpenAI Chatbot')

    user_input = st.text_input("Ask a question:")

    if user_input:
        answer = ask_openai(user_input)
        st.text("Answer: ")
        st.write(answer)

main()

import streamlit as st


def financial_chatbot(query):
    query = query.lower()
    response = ""
    if "total revenue" in query:
        if "2022" in query:
            response = "2022 Total Revenue: Microsoft: $198,270M, Tesla: $53,823M, Apple: $365,817M."
        elif "2023" in query:
            response = "2023 Total Revenue: Microsoft: $211,915M, Tesla: $81,462M, Apple: $394,328M."
        elif "2024" in query:
            response = "2024 Total Revenue: Microsoft: $245,122M, Tesla: $96,773M, Apple: $383,285M."
        else:
            response = "Please specify the year (2022, 2023, or 2024) for total revenue queries."

    elif "net income change" in query:
        if "2022 to 2023" in query:
            response = "Net Income Change from 2022 to 2023: Microsoft: Decreased by $377M, Tesla: Increased by $6,943M, Apple: Increased by $5,123M."
        elif "2023 to 2024" in query:
            response = "Net Income Change from 2023 to 2024: Microsoft: Increased by $15,775M, Tesla: Increased by $2,387M, Apple: Decreased by $2,808M."
        else:
            response = "Please specify the interval (2022 to 2023 or 2023 to 2024) for net income change queries."

    elif "debt to asset ratio" in query:
        if "2022" in query:
            response = "2022 Debt to Asset Ratio: Microsoft: 54.35%, Tesla: 49.17%, Apple: 81.62%."
        elif "2023" in query:
            response = "2023 Debt to Asset Ratio: Microsoft: 49.94%, Tesla: 44.26%, Apple: 85.64%."
        elif "2024" in query:
            response = "2024 Debt to Asset Ratio: Microsoft: 47.58%, Tesla: 40.34%, Apple: 82.37%."
        else:
            response = "Please specify the year (2022, 2023, or 2024) for debt to asset ratio queries."

    else:
        response = "Sorry, I can only provide information on predefined queries. Please check your input."

    return response

# Custom CSS to inject for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load local CSS
local_css("style.css")

# Streamlit interface
st.title('Financial Data Chatbot')
st.write('Welcome to the Financial Data Chatbot! Ask me about the 2024 financial data for Microsoft, Tesla, or Apple.')

user_query = st.text_input("Type your query here:", "")

if user_query:
    response = financial_chatbot(user_query)
    st.text(response)
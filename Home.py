import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Set Streamlit page configuration
st.set_page_config(
    page_title='Customer Churn Prediction App',
    page_icon='🏘️',
    layout='wide'
)

# Load configuration from YAML file
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize Streamlit Authenticator with configuration settings
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Perform user authentication
name, authentication_status, username = authenticator.login(location='sidebar')

# Handle authentication status
if authentication_status == False:
    st.error("🚫 Username/Password is incorrect")  # Display error message if authentication fails
    st.code("""
            Username: deofis
            Password: abc123""")
    
if authentication_status == None:
    st.warning("Please enter username and Password")  # Prompt user to enter username and password if not authenticated
    st.code("""
            Username: deofis
            Password: abc123""")


if authentication_status == True:
    # Define main content of the app
    def main():
            # Display welcome text
        st.markdown("<p style='text-align: left; color: #0066ff; font-size: 36px;'>Welcome to the Customer Churn Prediction App! 📊</p>", unsafe_allow_html=True)
            # Display downloaded image
        image_path = './images/image.png'
        st.image(image_path, use_column_width=False, output_format = "auto")

        # st.title('Customer Churn Prediction App')
        st.markdown(
            """
            <style>
                .title {
                    text-align: center;
                    font-size: 36px;
                    color: #0066ff;
                    padding-bottom: 20px;
                }
                .info {
                    font-size: 18px;
                    color: #333333;
                    line-height: 1.6;
                }
                .subheader {
                    font-size: 24px;
                    color: #009933;
                    padding-top: 20px;
                }
                .social-links {
                    font-size: 20px;
                    color: #0000ff;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Split the content into two halves
        col1, col2 = st.columns(2)

        with col1:

            # App Information Section
            st.header("App Information 💬")
            st.write("Experience the future of telecommunications with our cutting-edge Customer Churn Prediction App! Powered by advanced analytics and machine learning, we offer Vodafone a decisive edge in customer retention. Say goodbye to churn uncertainty and hello to proactive strategies that redefine industry standards. Together, let's shape the future of telecommunications! 💼")

            # Dataset Information Section
            st.header("Dataset Information")
            st.write("This dataset contains different features information such as:")
            st.write("- Gender: Whether the customer is a male or a female")
            st.write("- SeniorCitizen: Whether a customer is a senior citizen or not")
            st.write("- Tenure: Number of months the customer has stayed with the company")
            st.write("- MonthlyCharges: The amount charged to the customer monthly")
            st.write("- TotalCharges: The total amount charged to the customer")
            st.write("- Churn: Whether the customer churned or not")

        with col2:

            # How to Use Section
            st.header("How to Use the App")
            st.write("To use the Customer Churn Prediction App, follow these simple steps:")
            st.write("* Navigate to the 'Predictions' page.")
            st.write("* Input the relevant information about the customer.")
            st.write("* Click on the 'Predict' button to generate the prediction.")

            # Source Code Section
            st.header("Source Code")
            st.write("Unleash your creativity and collaboration by clicking the link below! Our open-source ethos invites you to explore, contribute, and innovate with the source code on GitHub. Join the revolution in customer retention strategies and pave the way for a brighter tomorrow.")
            st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-View%20on%20GitHub-blue?logo=GitHub)](https://github.com/Elphoxa/Customer-Churn-Prediction-App)")

            # Social Handles Section
            st.header("Social Handles")
            st.write("Connect with me on social media:")
            st.write("- [GitHub](https://github.com/Elphoxa) 🐙")
            st.write("- [LinkedIn](https://www.linkedin.com/in/efosa-omosigho) 💼")
    
    # Add logout button to sidebar
    authenticator.logout("Logout", "sidebar")

    # Display sidebar with user's name
    st.sidebar.title("Welcome")

    if __name__ == '__main__':
        main()
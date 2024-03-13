import streamlit as st
import numpy as np
import pandas as pd
import os

# Define a key for storing the data in the session state
DATA_KEY = "data_key"

# Set page configuration
st.set_page_config(
    page_title='View Data',
    page_icon='📊',
    layout='wide'
)

# Load data function
@st.cache_data
def load_data(csv_file_path):
    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        # Drop 'customerID' column
        if 'customerID' in df.columns:
            df.drop('customerID', axis=1, inplace=True)
        return df
    else:
        st.error("File not found.")
        return None

# Function to select features based on type
def select_features(feature_type, data_df):
    if feature_type == 'Numerical Features':
        return data_df.select_dtypes(include=np.number)
    elif feature_type == 'Categorical Features':
        return data_df.select_dtypes(include='object')
    else:
        return data_df

# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.info('Please log in to access the application from the homepage.')
else:
    # Title of the page
    st.title('Vodafone Data')

    # Define CSV file path
    csv_file_path = "./data/data.csv"

    # Load the data
    data_df = load_data(csv_file_path)

    if data_df is not None:
        # Set the data into the session state
        st.session_state[DATA_KEY] = data_df

        # Selectbox to choose the type of features to display
        selected_feature_type = st.selectbox("Select data features", options=['All Features', 'Numerical Features', 'Categorical Features'],
                                             key="selected_columns")

        # Display the selected features
        if selected_feature_type == 'All Features':
            # Show all features if selected
            st.write(st.session_state[DATA_KEY])
        else:
            # Show selected type of features
            st.write(select_features(selected_feature_type, st.session_state[DATA_KEY]))

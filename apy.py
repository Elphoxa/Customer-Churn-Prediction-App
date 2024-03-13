import streamlit as st
import numpy as np
import pandas as pd
import pyodbc
import os


# Define the database connection function
def establish_connection():
    try:
        connection = pyodbc.connect(
            "DRIVER={SQL Server};SERVER="
            + st.secrets["SERVER"]
            + ";DATABASE="
            + st.secrets["DATABASE"]
            + ";UID="
            + st.secrets["UID"]
            + ";PWD="
            + st.secrets["PWD"]
        )
        return connection
    except pyodbc.Error as e:
        st.error("Unable to establish database connection.")
        st.error(e)
        return None

# Cache the database query results
@st.cache(allow_output_mutation=True)
def query_database(query):
    conn = establish_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
                # Convert fetched rows into a DataFrame
                df = pd.DataFrame.from_records(data=rows, columns=[column[0] for column in cur.description])
            return df
        except pyodbc.Error as e:
            st.error("Error executing query.")
            st.error(e)
            return None
        finally:
            # Close the database connection
            if conn:
                conn.close()

if __name__ == '__main__':
    # Define the database query
    query = "select * from LP2_Telco_churn_first_3000"
    # Execute the query and get the data DataFrame
    data_df = query_database(query)

    if data_df is not None:
        # Define the file path where you want to save the CSV file
        csv_file_path = "./data/data.csv"

        # Save the DataFrame to a CSV file
        data_df.to_csv(csv_file_path, index=False)
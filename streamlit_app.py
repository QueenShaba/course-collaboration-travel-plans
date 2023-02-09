import pyodbc
import pandas as pd
import streamlit as st

def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["db"]
        + ";UID="
        + st.secrets["sa"]
        + ";PWD="
        + st.secrets["pwd"]
        )

    conn = init_connection()

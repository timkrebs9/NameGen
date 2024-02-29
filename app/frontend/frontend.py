import streamlit as st
import requests
import json
import pandas as pd
import base64
from io import StringIO

# Funktion zum Konvertieren von JSON-Daten in einen CSV-Download-Link
def get_csv_download_link(json_data):
    """
    Generiert einen a-Tag, der es dem Benutzer ermöglicht, die JSON-Daten als CSV-Datei herunterzuladen.
    """
    # Konvertiere JSON-Daten in einen DataFrame
    df = pd.DataFrame(json_data)
    # Konvertiere den DataFrame in CSV
    csv = df.to_csv(index=False)
    # Erstelle ein Byte-Objekt aus dem CSV-String
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:text/csv;base64,{b64}" download="users.csv">Download CSV file</a>'
    return href


def get_table_download_link(json_data):
    """
    Generiert einen Link zum Herunterladen der JSON-Daten.
    """
    json_file = json.dumps(json_data)
    b64 = base64.b64encode(json_file.encode()).decode()  # String in Base64 umwandeln
    href = f'<a href="data:file/json;base64,{b64}" download="users.json">Download JSON file</a>'
    return href

BACKEND_URL = "http://127.0.0.1:8000/users"
st.title('Benutzerdaten Generator')


name = st.checkbox('Name')
email = st.checkbox('E-Mail')
address = st.checkbox('Adresse')
phone_number = st.checkbox('Telefonnummer')


user_count = st.slider('Anzahl der Benutzer', min_value=1, max_value=10, value=5)

if st.button('Daten generieren'):
    response = requests.get(BACKEND_URL, params={"count": user_count})
    if response.status_code == 200:
        users = response.json()

        user_data_list = []
        for user in users:
            user_data = {}
            if name:
                user_data["name"] = user['name']
            if email:
                user_data["email"] = user['email']
            if address:
                user_data["address"] = user['address']
            if phone_number:
                user_data["phone_number"] = user['phone_number']
            user_data_list.append(user_data)

        formatted_json = json.dumps(user_data_list, indent=2)
        
        st.code(formatted_json, language='json')
        st.markdown(get_table_download_link(users), unsafe_allow_html=True)
        st.markdown(get_csv_download_link(users), unsafe_allow_html=True)
    else:
        st.error('Fehler beim Abrufen der Daten vom Backend.')
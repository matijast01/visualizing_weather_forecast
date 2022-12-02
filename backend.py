import requests
import streamlit as st

APIkey = st.secrets["API_KEY"]


def get_data(place, days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"][:days*8]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3))

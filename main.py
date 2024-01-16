import streamlit as st
import plotly.express as pl
from backend import get_data

st.title("Weather Forecaster")
city = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days for the forecast")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {city.title()}")

if city:
    ##try:
        filtered_data = get_data(city, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = pl.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images-2/clear.png", "Clouds": "images-2/cloud.png",
                      "Rain": "images-2/rain.png", "Snow": "images-2/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)
   ## except KeyError:
        ##st.write("City name cannot be found, please try another city.")

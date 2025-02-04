# streamlit_app.py
import streamlit as st
import folium
from streamlit_folium import folium_static
import requests
import time

def main():
    st.title("Real-time Location Tracker")

    # Create a placeholder for the map
    map_placeholder = st.empty()

    while True:
        # Get the latest location from the server
        try:
            response = requests.get('http://10.233.231.106:5000/get_location')
            location = response.json()

            # Create a map centered at the current location
            m = folium.Map(
                location=[location['latitude'], location['longitude']],
                zoom_start=15
            )

            # Add a marker for the current location
            folium.Marker(
                [location['latitude'], location['longitude']],
                popup='Current Location',
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)

            # Display the map
            with map_placeholder:
                folium_static(m)

        except Exception as e:
            st.error(f"Error fetching location: {str(e)}")

        # Wait for 5 seconds before updating
        time.sleep(5)

if __name__ == "__main__":
    main()

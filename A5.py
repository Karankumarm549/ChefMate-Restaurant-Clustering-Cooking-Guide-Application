import streamlit as st
import pandas as pd
import requests
from streamlit_option_menu import option_menu
import google.generativeai as genai
import folium
from streamlit_folium import folium_static

# Full screen CSS style
st.set_page_config(layout="wide")

# Add custom CSS to make the menu title take the full width of the screen
# Load the image
#image = ""
#st.image(image, use_column_width=True)

# Navigation Menu
web = option_menu(
    menu_title="Welcome to ZOMATO",
    options=["Home", "Chef Bot Assistant", "About"],
    icons=["house", "robot", "info-circle"],
    orientation="horizontal"
)

# Load the merged datase
@st.cache_data
def load_data():
    return pd.read_csv('merged_restaurant_data.csv')

data = load_data()

# Home Page
if web == "Home":
    # Title
    st.title("🍴 Restaurant Recommendation System")

    # Filters on Home Screen (instead of sidebar)
    st.subheader("🔍 Filter Restaurants")
    
    # Create three columns for the filters
    col1, col2, col3 = st.columns(3)

    with col1:
        cities = data['restaurant.location.city'].unique()
        selected_city = st.selectbox("Select City", cities)
    with col2:
        filtered_localities = data[data['restaurant.location.city'] == selected_city]['restaurant.location.locality'].unique()
        selected_locality = st.selectbox("Select Locality", filtered_localities)
    with col3:
        # Ensure that 'restaurant.cuisines' is a string and handle NaN values
        data['restaurant.cuisines'] = data['restaurant.cuisines'].apply(lambda x: str(x) if isinstance(x, str) else '')
        data['restaurant.cuisines'] = data['restaurant.cuisines'].fillna('')
 
        # Cuisines filter
        all_cuisines = set(', '.join(data['restaurant.cuisines']).split(', '))
        selected_cuisines = st.multiselect("Select Cuisines", all_cuisines)

    # Apply filters
    filtered_data = data[
        (data['restaurant.location.city'] == selected_city) &
        (data['restaurant.location.locality'] == selected_locality)
    ]

    if selected_cuisines:
        filtered_data = filtered_data[filtered_data['restaurant.cuisines'].apply(lambda x: any(cuisine in x for cuisine in selected_cuisines))]
        
    # Sorting the filtered_data by rating in descending order
    filtered_data = filtered_data.sort_values(by='restaurant.user_rating.aggregate_rating', ascending=False)

    # Display filtered restaurants in row-wise format
    st.subheader(f"🍽️ Restaurants in {selected_locality}, {selected_city}")

    if not filtered_data.empty:
        # Create a map centered on the first restaurant
        latitude = filtered_data['restaurant.location.latitude'].iloc[0]
        longitude = filtered_data['restaurant.location.longitude'].iloc[0]
        m = folium.Map(location=[latitude, longitude], zoom_start=12)

        # Add markers for each restaurant
        for index, row in filtered_data.iterrows():
            folium.Marker(
                location=[row['restaurant.location.latitude'], row['restaurant.location.longitude']],
                popup=folium.Popup(f"<b>{row['restaurant.name']}</b><br>Cuisines: {row['restaurant.cuisines']}<br>Rating: {row['restaurant.user_rating.aggregate_rating']} stars", max_width=300)
            ).add_to(m)

        # Create columns for content and map side by side
        col1, col2 = st.columns([2, 1])  # First column larger, second column for map

        with col1:
            # Display restaurant details
            counter = 1 
            for _, row in filtered_data.iterrows():
                with st.container():
                    col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 2, 1])
                    with col1:
                        st.write(f"**Name:** {row['restaurant.name'].upper()}")
                    with col2:
                        st.write(f"**Cuisines:** {row['restaurant.cuisines']}")
                    with col3:
                        st.write(f"**Rating:** {str(row['restaurant.user_rating.aggregate_rating'])} stars")
                    with col4:
                        st.write(f"**Cost for Two:** ₹{str(row['restaurant.average_cost_for_two'])}")
                    with col5:
                        st.markdown(f"[📋 View Menu]({row['restaurant.menu_url']})", unsafe_allow_html=True)
                        st.markdown(f"[📷 View Photos]({row['restaurant.photos_url']})", unsafe_allow_html=True)
                    with col6:
                        st.image(row['restaurant.thumb'], width=300)
                st.markdown("---")
                counter += 1

        with col2:
            # Display the map on the right side
            folium_static(m)

    else:
        st.write("No restaurants found based on your criteria.")


# Chef Bot Assistant Page
elif web == "Chef Bot Assistant":
    # Your Gemini API key
    GEMINI_API_KEY = 'AIzaSyCCYNrOK99Qwj1tCHJLcOGAUZgiHcNPVtI'

    # Configure the Gemini API
    genai.configure(api_key=GEMINI_API_KEY)

    # Set up the generation configuration for the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Initialize the model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
    )

    # Start the chat session
    chat_session = model.start_chat(history=[])

    # Function to filter food-related queries
    def is_food_related(query):
        food_keywords = ['recipe', 'ingredients', 'how to cook', 'how to make', 'cooking']
        return any(keyword in query.lower() for keyword in food_keywords)

    # Streamlit UI
    st.title("Chef Mate: Assistant  🤖🍳")
    st.write("Ask me how to cook your favorite dishes! For other queries, I'll politely decline. 😊")

    # Text input for user query
    query = st.text_input("Ask your recipe question:")

    # Add "Ask" button
    ask_button = st.button("Ask")

    # Action when the button is clicked
    if ask_button and query:
        # Check if the query is food-related
        if is_food_related(query):
            # Send the query to the Gemini API
            response = chat_session.send_message(query)
            # Display the response
            st.write(response.text)
        else:
            st.write("I am only able to assist with food recipes. Please ask about recipes or cooking methods.")

# About Page
elif web == "About":
    st.title("ChefMate: Restaurant Clustering & Cooking Guide")
    st.subheader("🌐 Domain: Transportation")
    st.subheader("🎯 Objective:")
    st.markdown("""
    The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. 
    - **Selenium**: Automates the extraction of bus routes, schedules, and more.
    - **Pandas**: Prepares data for analysis.
    - **MySQL**: Stores data efficiently for retrieval.
    - **Streamlit**: Creates an interactive interface for data visualization.
    """)
    st.subheader("📜 Overview:")
    st.markdown("""
    - **Selenium**: Automates web browsing for scraping.
    - **Pandas**: Data manipulation and cleaning.
    - **MySQL**: Database integration for efficient storage.
    - **Streamlit**: Develops user-friendly web applications.
    """)
    st.subheader("💡 Skills:")
    st.markdown("Selenium, Python, Pandas, MySQL, Streamlit.")
    st.subheader("👨‍💻 Developed by: Karan Kumar M")


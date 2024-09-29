import streamlit as st
import gem as travel_planner  # Replace with actual module name

def main():
    st.title("Travel Itinerary")

    departure_location = st.text_input("Departure Location:")
    location = st.text_input("Destination:")
    people_count = st.number_input("Number of People:", min_value=1)
    travel_days = st.number_input("Travel Days:", min_value=1)
    travel_month = st.selectbox("Travel Month:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    audience_choice = st.selectbox("Audience Choice:", ["Adventure", "Family", "Elderly"])
    budget = st.number_input("Budget (USD):", min_value=1)

    if st.button("Generate Itinerary"):
        itinerary = travel_planner.generate_itinerary(departure_location, location, people_count, travel_days, travel_month, audience_choice, budget)
        st.success(f"Itinerary:\n{itinerary}")

if __name__ == "__main__":
    main()

import streamlit as st
import gem as travel_planner  # Replace with the actual module name

# Function to add CSS styling
def add_custom_css():
    st.markdown(
        """
        <style>
        /* Navbar */
        nav {
            background-color: #461ed4d2;
            overflow: hidden;
            width: 100vw; /* Full width */
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 20px;
            position: fixed;
            top: 5%;
            left: 0;
            z-index: 1000; /* Ensures it stays on top */
        }

        /* Logo styling */
        nav .logo img {
            height: 60px;
            width: auto;
        }

        /* Navbar menu items */
        nav ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            display: flex;
        }

        nav ul li {
            margin-right: 20px;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            padding: 14px 20px;
            display: inline-block;
        }

        nav ul li a:hover {
            background-color: #007bff;
            color: white;
            border-radius: 5px;
        }

        /* Body background with an image */
        .stApp {
            background-image: url('https://github.com/nitishdas199/triprush/blob/8203fa71385336668ed3029758d1e189e6f1f8ba/bg.jpg?raw=true'); /* Replace with your image URL */
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        /* Blurred form container */
        .container {
            max-width: 500px;
            margin: 100px auto;  /* Added margin to avoid overlap with navbar */
            padding: 20px;
            background: rgba(255, 255, 255, 0.045);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #fff;
        }

        label {
            display: block;
            margin-bottom: 5px;
            color: #fff;
        }

        input, select {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }

        button {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #0056b3;
        }

        #result {
            margin-top: 20px;
            font-weight: bold;
            color: #fff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to add Navbar
def add_navbar():
    st.markdown(
        """
        <nav>
            <div class="logo">
                <a href="#"><img src="https://github.com/nitishdas199/triprush/blob/b392daaeeb9796085ad944fc9b66948aaebad815/triprush.png?raw=true" alt="Travel Rush Logo"></a> <!-- Replace with your logo URL -->
            </div>
            <ul>
                <li><a href="https://triprush.streamlit.app/">Home</a></li>
                <li><a href="about.html">About Us</a></li>
                <li><a href="#"contact">Contact</a></li>
            </ul>
        </nav>
        """,
        unsafe_allow_html=True
    )

def main():
    add_custom_css()  # Add custom CSS
    add_navbar()  # Add navbar

    # Main content
    st.markdown("<h1>Fill the form for your Customized Travel Itinerary</h1>", unsafe_allow_html=True)

    # Form container
    with st.container():
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

import streamlit as st

def main():
    st.markdown(
        """
        <style>
            body {
                background-color: lightgreen;
            }
            .title {
                font-size: 24px;
                font-weight: bold;
                font-style: italic;
                color: black;
                text-align: center;
                margin-top: 50px;
            }
            .description-box {
                background-color: pink;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin-top: 20px;
            }
            .next-button {
                background-color: lightblue;
                color: black;
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 5px;
                text-align: center;
                margin-top: 30px; /* Increased margin-top */
            }
            .image-container {
                display: flex;
                justify-content: space-around;
                margin-top: 50px;
            }
            .image-button {
                background-color: green;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 5px;
                text-align: center;
                margin-top: 20px;
            }
            .image-container div {
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='title'>Title of the Page</div>
        <div class='description-box'>
            Description goes here.
        </div>
        <br> <!-- Adding space between description and button -->
        <br>
        """,
        unsafe_allow_html=True
    )

    if st.button('Next', key='next_button'):
        st.empty()  # Clear the content
        st.markdown(
            """
            <div class='image-container'>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Student Image" style="width: 150px; height: 150px; border-radius: 50%;">
                    <button class='image-button'>Student</button>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Teacher Image" style="width: 150px; height: 150px; border-radius: 50%;">
                    <button class='image-button'>Teacher</button>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Professional Image" style="width: 150px; height: 150px; border-radius: 50%;">
                    <button class='image-button'>Professional</button>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Specifications Image" style="width: 150px; height: 150px; border-radius: 50%;">
                    <button class='image-button'>Specifications</button>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("Student Preferences:")
        st.markdown("### Student:")
        st.markdown("1. *Intended Use:*")
        intended_use_options = st.multiselect(
            "Select intended use:",
            ["Studying", "Programming", "Gaming", "Multimedia"]
        )

        st.markdown("2. *Preferred Brands or Models:*")
        preferred_brands_options = st.multiselect(
            "Select preferred brands or models:",
            ["Anything cool! (all)", "Tech-savvy picks! (dell, hp)", "ASUS", "HP", "Dell", "Lenovo", "Apple (MacBook Air/Pro)", "Others (please specify)"]
        )

        st.markdown("3. *Processor Performance:*")
        processor_performance_options = st.multiselect(
            "Select processor performance:",
            ["Basic tasks (Intel Core i3 or equivalent AMD)", "Moderate multitasking (Intel Core i5 or equivalent AMD Ryzen 5)", "Intensive tasks (Intel Core i7/i9 or equivalent AMD Ryzen 7/9)"]
        )

        st.markdown("4. *Budget Range:*")
        budget_range_options = st.multiselect(
            "Select budget range:",
            ["Bargain hunter (Under 40k)", "Mid-range magic (40k - 55k)", "Sweet spot spender (55k - 70k)", "Sky's the limit (70k - 85k)", "Ultimate splurge (85k above)"]
        )

        st.markdown("5. *Operating System Preference:*")
        os_preference_options = st.multiselect(
            "Select operating system preference:",
            ["The classic! (windows)", "For that sleek vibe! (macOs)", "Feeling adventurous! (Linux)"]
        )

        st.markdown("6. *RAM Requirement:*")
        ram_requirement_options = st.multiselect(
            "Select RAM requirement:",
            ["Basic needs (4GB - 8GB)", "Better performance (8GB - 16GB)", "Future-proofing! (16GB+)"]
        )

        st.markdown("7. *Desired Storage Space:*")
        storage_space_options = st.multiselect(
            "Select desired storage space:",
            ["Lite storage (128GB - 256GB)", "More space, more fun! (256GB - 512GB)", "Store it all! (512GB - 1TB)", "Who needs limits! (1TB+)"]
        )

        st.markdown("8. *Preferred Screen Size:*")
        screen_size_options = st.multiselect(
            "Select preferred screen size:",
            ["Compact is cute (11 - 13 inches)", "Standard and steady (14 - 15 inches)", "Big

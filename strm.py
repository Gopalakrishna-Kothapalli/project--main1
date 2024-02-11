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
                color: white;
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
        <div class='title'>-- User centric Laptop Recommendation --</div>
        <div class='description-box'>
            Welcome to our revolutionary laptop recommendation tool! Are you tired of shifting through endless options, unsure of which laptop suits your needs best? Let us simplify the process for you. Our intelligent system takes into account your unique preferences and requirements to generate tailored recommendations that fit like a glove.

Discovering the perfect laptop has never been easier:
- Answer a few simple questions tailored to your expertise level and needs.
- Explore a comprehensive range of specifications and features, from processing power to display quality.
- Receive personalized recommendations that align perfectly with your preferences and budget.

Whether you're a tech-savvy professional, a studious student, or simply seeking a reliable companion for your daily tasks, we've got you covered. Let us guide you towards the laptop of your dreams!

.
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
            ["Compact is cute (11 - 13 inches)", "Standard and steady (14 - 15 inches)", "Big is bold (15+ inches)"]
        )

        st.markdown("9. *Graphics-Intensive Tasks:*")
        graphics_tasks_options = st.multiselect(
            "Select graphics-intensive tasks:",
            ["Casual gamer (Light gaming)", "Multitask master (Moderate gaming and video editing)", "Gaming champ (Heavy gaming and pro editing)"]
        )

        st.markdown("10. *Display Panel Type:*")
        display_panel_options = st.multiselect(
            "Select display panel type:",
            ["Colors matter (IPS for better color)", "Speed is key (TN for faster response)"]
        )

        st.markdown("11. *Display Resolution:*")
        display_resolution_options = st.multiselect(
            "Select display resolution:",
            ["Standard HD (1366 x 768)", "Full HD (1920 x 1080)", "Super sharp (QHD or higher)"]
        )

        st.markdown("12. *Portability Importance:*")
        portability_options = st.multiselect(
            "Select portability importance:",
            ["Feather-light (Very important)", "Balanced buddy (Moderate)", "No big deal (Not a priority)"]
        )

        st.markdown("13. *Battery Life Priority:*")
        battery_options = st.multiselect(
            "Select battery life priority:",
            ["Marathon mode (Long battery life)", "Day-to-day (Moderate battery life)", "Plugged in always (Not a concern)"]
        )

        st.markdown("14. *Touchscreen Preference:*")
        touchscreen_options = st.multiselect(
            "Select touchscreen preference:",
            ["Swipe and tap (Yes, I prefer a touchscreen)", "Buttons are enough (No, I don't need a touchscreen)"]
        )

        st.markdown("15. *Necessary Ports and Connectivity:*")
        connectivity_options = st.multiselect(
            "Select necessary ports and connectivity:",
            ["USB-C is a must!", "HDMI for shows!", "SD card for pics!", "Thunderbolt for future!", "Surprise me!"]
        )

        st.markdown("16. *Importance of Upgradability:*")
        upgradability_options = st.multiselect(
            "Select importance of upgradability:",
            ["Tech explorer (I love upgrades!)", "Meh, not bothered (Upgradability is not a priority)"]
        )

        st.markdown("17. *Keyboard Type:*")
        keyboard_options = st.multiselect(
            "Select keyboard type:",
            ["Standard keys", "Backlit for flair", "Mechanical for the win!"]
        )

        st.markdown("18. *Fingerprint Reader/Security Features:*")
        fingerprint_options = st.multiselect(
            "Select fingerprint reader/security features:",
            ["Unlock with a touch (Fingerprint reader)", "I'm good with passwords (No specific need)"]
        )

        st.markdown("19. *Warranty and Support:*")
        warranty_options = st.multiselect(
            "Select warranty and support:",
            ["All-inclusive package (Longer warranty, premium support)", "Standard deal is fine (Standard warranty is sufficient)"]
        )

if __name__ == "__main__":
    main()


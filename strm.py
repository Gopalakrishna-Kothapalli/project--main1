import streamlit as st

def main():
    st.markdown(
        """
        <style>
            .title {
                font-size: 24px;
                font-weight: bold;
                font-style: italic;
                color: black;
            }
            .description-box {
                background-color: pink;
                padding: 20px;
                border-radius: 10px;
            }
            .get-started-button {
                background-color: green;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 5px;
                text-align: center;
                margin-top: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button('Get Started', key='first_page_button'):
        st.empty()  # Clear the content
        st.markdown(
            """
            <div style='background-color: facebook blue; padding: 20px;'>
                <div class='title'>Hi Gopal</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div style='background-color: white; padding: 20px;'>
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
                <a href="/redirect" class='get-started-button'>Get Started</a>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()





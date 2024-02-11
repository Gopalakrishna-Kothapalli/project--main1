import streamlit as st

def main():
    st.markdown(
        """
        <style>
            .title {
                font-size: 24px;
                font-weight: bold;
                font-style: italic;
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

    if st.button('Get Started'):
        st.empty()  # Clear the content
        st.markdown(
            """
            <div style='background-color: facebook blue; padding: 20px;'>
                <div class='title'>Hi Gopal</div>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()



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
            .next-button {
                background-color: green;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 5px;
                text-align: center;
                margin-top: 20px;
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
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button('Next', key='next_button'):
        st.empty()  # Clear the content
        st.markdown(
            """
            <div class='image-container'>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Student Image" style="width: 150px; height: 150px;">
                    <button class='image-button'>Student</button>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Teacher Image" style="width: 150px; height: 150px;">
                    <button class='image-button'>Teacher</button>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Professional Image" style="width: 150px; height: 150px;">
                    <button class='image-button'>Professional</button>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Specifications Image" style="width: 150px; height: 150px;">
                    <button class='image-button'>Specifications</button>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            """
            <div style='background-color: white; padding: 20px;'>
                <div class='title'>Title of the Page</div>
                <div class='description-box'>
                    Description goes here.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()






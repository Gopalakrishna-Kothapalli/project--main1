import streamlit as st

def main():
    st.markdown(
        """
        <style>
            body {
                background-color: white;
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

    st.markdown(
        """
        <div class='title'>Title of the Page</div>
        <div class='description-box'>
            Description goes here.
        </div>
        <button class='next-button' onclick="scrollToBottom()">Next</button>
        <script>
            function scrollToBottom() {
                window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
            }
        </script>
        """,
        unsafe_allow_html=True
    )

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

if __name__ == "__main__":
    main()








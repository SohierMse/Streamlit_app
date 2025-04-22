import streamlit as st
import nbformat
from nbconvert import PythonExporter

# Define default page
if 'Page' not in st.session_state:
    st.session_state.Page = 'Home'

# Function to navigate between pages
def go_to(Page_name):
    st.session_state.Page = Page_name

# Custom styles for buttons
st.markdown("""
    <style>
        .stButton>button {
            height: 60px;
            width: 200px;
            font-size: 20px;
            border-radius: 10px;
        }
        .purple-button button {
            background-color: #D8BFD8 !important; /* Light Purple */
            color: black !important;
        }
        .blue-button button {
            background-color: #ADD8E6 !important; /* Baby Blue */
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# Home Page
if st.session_state.Page == 'Home':
    st.header("Home Page")
    st.write("Welcome to our WEB !🥰🥰🥰🥰🥰")
    st.write("You are a Customer or From our Cast ?")
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.markdown('<div class="purple-button">', unsafe_allow_html=True)
            if st.button("Cast"):
                go_to('Cast')
            st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        with st.container():
            st.markdown('<div class="blue-button">', unsafe_allow_html=True)
            if st.button("Customer"):
                go_to('Customer')
            st.markdown('</div>', unsafe_allow_html=True)

# Cast Page
elif st.session_state.Page == 'Cast':
    st.title("Cast Page")
    with open("DS_Tools_Project.ipynb", "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)
    exporter = PythonExporter()
    source_code, _ = exporter.from_notebook_node(notebook)
    exec(source_code, globals()) 
    st.success("Done!")
    if "df" in globals():
        st.write("The data:")
        st.dataframe(df.head())
    else:
        st.error("There is no data")
    
    if st.button("Back to Home"):
        go_to('Home')

# Customer Page
elif st.session_state.Page == 'Customer':
    st.title("Customer Page")
    x=st.text_input("What do you want to buy ?")
    st.write(x)

    if st.button("Back to Home"):
        go_to('Home')
